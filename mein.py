import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Basic GUI")
root.geometry("300x150")

name_entry = tk.Entry(root)
name_entry.pack(pady=10)

def calculate():
    math = name_entry.get()
    result = eval(math)
    messagebox.showinfo("Result", f"Result: {result}")


button = tk.Button(root, text="Calculate", command=calculate)
button.pack(pady=10)

root.mainloop()