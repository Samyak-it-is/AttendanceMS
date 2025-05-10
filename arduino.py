import tkinter as tk
from tkinter import *
import cv2
import torch
import serial
import time
q = 0
persons = []

arduino = serial.Serial(port='COM10', baudrate=9600, timeout=1)

def send_command(command):
    arduino.write(command.encode())  # Send command to Arduino
    time.sleep(0.1)  # Allow some time for Arduino to process


def blend_color(start_color, end_color, steps, step):
    start_r, start_g, start_b = int(start_color[1:3], 16), int(start_color[3:5], 16), int(start_color[5:7], 16)
    end_r, end_g, end_b = int(end_color[1:3], 16), int(end_color[3:5], 16), int(end_color[5:7], 16)

    new_r = int(start_r + (end_r - start_r) * step / steps)
    new_g = int(start_g + (end_g - start_g) * step / steps)
    new_b = int(start_b + (end_b - start_b) * step / steps)

    return f'#{new_r:02x}{new_g:02x}{new_b:02x}'

def transition_color(widgets, steps, step=0):
    if step <= steps:
        for widget, attr, start_color, end_color in widgets:
            new_color = blend_color(start_color, end_color, steps, step)
            widget.config(**{attr: new_color})
        widgets[0][0].after(50, transition_color, widgets, steps, step + 1)

def change(count):
    st = ['#3fde07', '#d6bd1b', '#d6a019', '#eb940e', '#f5650c']
    en = ['#3fde07', '#d6bd1b', '#d6a019', '#eb940e', '#f5650c']

    transition_index = min(int(count/4), len(st) - 1)
    widgets_to_transition = [
        (frame1, 'bg', st[transition_index], en[transition_index])
    ]
    transition_color(widgets_to_transition, 10)


window = tk.Tk()
window.title("Color Transition")
window.geometry("300x200")

frame1 = tk.Frame(window, bg="#3fde07",highlightbackground="white", highlightthickness=2)
frame1.place(relx=0.21, rely=0.17, relwidth=0.39, relheight=0.80)
Label(frame1,text="Room 1",font=("Arial", 15)).place(relx=0.1, rely=0)
time_limit = 10
def load_model():
    global persons

  
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    cap = cv2.VideoCapture(1)
    

    def process_frame():
        global time_limit
        nonlocal cap
        ret, frame = cap.read()
        if not ret:
            cap.release()
            cv2.destroyAllWindows()
            return

  
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = model(rgb_frame)

        detections = results.pandas().xyxy[0]
        persons = detections[detections['name'] == 'person']

        person_count = len(persons)
        
        if person_count == 0:
            time_limit = time_limit - 1
            if time_limit == 0:
                time.sleep(10)
                send_command('0')
                
        
            
        
        
        # if user_input in ['1', '0']:A
        #     send_command(user_input)
        # else:
        #     print("Invalid input. Please enter '1' or '0'.")

        if person_count > 0:
            change(person_count)
            send_command('1')
            time_limit = 10


        for _, row in persons.iterrows():
            x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)


        cv2.putText(frame, f"Count: {person_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Room Monitoring", frame)


        if cv2.waitKey(1) & 0xFF != ord('q'):
            window.after(10, process_frame)
        else:
            cap.release()
            cv2.destroyAllWindows()

    process_frame()

load_model()
window.mainloop()
