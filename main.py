import tkinter as tk

root = tk.Tk()
root.title("Basic GUI")
root.geometry("300x170")

name_entry = tk.Entry(root)
name_entry.pack(pady=10)


def calculate():
    math = name_entry.get()
    try:
        result = eval(math)
        output_label.config(text=f"Result: {result}")
        error_label.config(text="")
    except Exception as e:
        error_label.config(text="Invalid input")
        output_label.config(text="")

button = tk.Button(root, text="Calculate", command=calculate)
button.pack(pady=10)

output_label = tk.Label(root, text="")
output_label.pack(pady=10)

error_label = tk.Label(root, text="", fg="red", font=("Arial", 10, "bold"))
error_label.pack(pady=10)

root.mainloop()

