import tkinter as tk
from tkinter import messagebox
import math

# Function to perform operations
def calculate(operation):
    try:
        num1 = float(entry1.get())

        # If the operation needs two inputs
        if operation in ("add", "subtract", "multiply", "divide"):
            num2 = float(entry2.get())

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero.")
                return
            result = num1 / num2
        elif operation == "square":
            result = num1 ** 2
        elif operation == "sqrt":
            if num1 < 0:
                messagebox.showerror("Error", "Cannot take square root of negative number.")
                return
            result = math.sqrt(num1)
        else:
            result = "Invalid Operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x350")

# Entry widgets
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Operation buttons
tk.Button(root, text="Add", command=lambda: calculate("add")).pack(pady=3)
tk.Button(root, text="Subtract", command=lambda: calculate("subtract")).pack(pady=3)
tk.Button(root, text="Multiply", command=lambda: calculate("multiply")).pack(pady=3)
tk.Button(root, text="Divide", command=lambda: calculate("divide")).pack(pady=3)

# New: Square and Square Root
tk.Button(root, text="Square (1st number)", command=lambda: calculate("square")).pack(pady=3)
tk.Button(root, text="Square Root (1st number)", command=lambda: calculate("sqrt")).pack(pady=3)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
