import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        label_result.config(text=f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

# Create main window
root = tk.Tk()
root.title("Celsius to Fahrenheit Converter")
root.geometry("300x200")
root.resizable(False, False)

# UI Elements
label_instruction = tk.Label(root, text="Enter temperature in Celsius:", font=("Arial", 12))
label_instruction.pack(pady=10)

entry_celsius = tk.Entry(root, font=("Arial", 14), justify='center')
entry_celsius.pack()

button_convert = tk.Button(root, text="Convert", command=convert, font=("Arial", 12), bg="#4CAF50", fg="white")
button_convert.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 14, "bold"))
label_result.pack()

root.mainloop()
