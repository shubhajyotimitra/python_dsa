import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence
import os

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == "shubhajyoti" and password == "1234":
        messagebox.showinfo("Login Success", "Welcome, shubhajyoti!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# ---- Setup window ----
root = tk.Tk()
root.title("Animated Login Page")
root.geometry("500x400")
root.resizable(False, False)

# ---- Load GIF from assets folder ----
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
gif_path = os.path.join(BASE_DIR, "assets", "background.gif")
print("Loading GIF from:", gif_path)


gif = Image.open(gif_path)
frames = [ImageTk.PhotoImage(img.copy().resize((500, 400))) for img in ImageSequence.Iterator(gif)]
frame_count = len(frames)

canvas = tk.Canvas(root, width=500, height=400, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Place first frame
image_container = canvas.create_image(0, 0, anchor="nw", image=frames[0])

# ---- Animate function ----
def animate(counter):
    frame = frames[counter]
    counter = (counter + 1) % frame_count
    canvas.itemconfig(image_container, image=frame)
    root.after(100, animate, counter)

# Start animation
root.after(0, animate, 0)

# ---- Login form UI ----
entry_username = tk.Entry(root, font=("Arial", 12))
canvas.create_window(250, 200, window=entry_username, width=200)

entry_password = tk.Entry(root, show="*", font=("Arial", 12))
canvas.create_window(250, 240, window=entry_password, width=200)

login_button = tk.Button(root, text="Login", command=login)
canvas.create_window(250, 280, window=login_button, width=100)

exit_button = tk.Button(root, text="Exit", command=root.quit)
canvas.create_window(250, 320, window=exit_button, width=100)

root.mainloop()


#venv/bin/python login.py




