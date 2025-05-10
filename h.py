import tkinter as tk

def blend_color(start_color, end_color, steps, step):
    # Interpolate between start and end colors
    start_r, start_g, start_b = int(start_color[1:3], 16), int(start_color[3:5], 16), int(start_color[5:7], 16)
    end_r, end_g, end_b = int(end_color[1:3], 16), int(end_color[3:5], 16), int(end_color[5:7], 16)

    new_r = int(start_r + (end_r - start_r) * step / steps)
    new_g = int(start_g + (end_g - start_g) * step / steps)
    new_b = int(start_b + (end_b - start_b) * step / steps)

    return f'#{new_r:02x}{new_g:02x}{new_b:02x}'

def transition_color(label, start_color, end_color, steps, step=0):
    if step <= steps:
        new_color = blend_color(start_color, end_color, steps, step)
        label.config(bg=new_color)
        label.after(50, transition_color, label, start_color, end_color, steps, step + 1)

root = tk.Tk()
root.geometry("300x200")

label = tk.Label(root, text="Color Transition", bg="#ff0000", fg="white", font=("Helvetica", 16))
label.pack(expand=True, fill="both")

# Start the color transition from red to blue
label.bind("<Button-1>", lambda event: transition_color(label, "#ff0000", "#0000ff", 100))

root.mainloop()