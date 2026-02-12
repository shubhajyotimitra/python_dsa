import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- DATABASE ----------------
conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    disease TEXT
)
""")
conn.commit()

# ---------------- FUNCTIONS ----------------
def add_patient():
    name = entry_name.get()
    age = entry_age.get()
    gender = entry_gender.get()
    disease = entry_disease.get()

    if name == "" or age == "":
        messagebox.showerror("Error", "Name and Age are required")
        return

    cursor.execute("INSERT INTO patients VALUES(NULL,?,?,?,?)",
                   (name, age, gender, disease))
    conn.commit()

    messagebox.showinfo("Success", "Patient Added Successfully")

    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_disease.delete(0, tk.END)

def view_patients():
    view_window = tk.Toplevel(root)
    view_window.title("Patient Records")
    view_window.geometry("500x300")

    text = tk.Text(view_window)
    text.pack(fill=tk.BOTH, expand=True)

    cursor.execute("SELECT * FROM patients")
    records = cursor.fetchall()

    text.insert(tk.END, "ID   Name   Age   Gender   Disease\n")
    text.insert(tk.END, "-"*50 + "\n")

    for row in records:
        text.insert(tk.END, f"{row}\n")

# ---------------- GUI WINDOW ----------------
root = tk.Tk()
root.title("Hospital Management System")
root.geometry("400x450")
root.config(bg="#e8f0fe")

title = tk.Label(root, text="Hospital Management System",
                 font=("Arial", 16, "bold"), bg="#e8f0fe")
title.pack(pady=10)

# ---------------- FORM ----------------
tk.Label(root, text="Patient Name", bg="#e8f0fe").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Age", bg="#e8f0fe").pack()
entry_age = tk.Entry(root)
entry_age.pack()

tk.Label(root, text="Gender", bg="#e8f0fe").pack()
entry_gender = tk.Entry(root)
entry_gender.pack()

tk.Label(root, text="Disease", bg="#e8f0fe").pack()
entry_disease = tk.Entry(root)
entry_disease.pack()

# ---------------- BUTTONS ----------------
tk.Button(root, text="Add Patient", width=20, command=add_patient).pack(pady=10)
tk.Button(root, text="View Patients", width=20, command=view_patients).pack()
tk.Button(root, text="Exit", width=20, command=root.destroy).pack(pady=10)

root.mainloop()