import tkinter as tk
from tkinter import messagebox

# Function to perform operations
def calculate(operation):
    try:
        num1 = float(entry1.get())
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
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Entry widgets
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Operation buttons
tk.Button(root, text="Add", command=lambda: calculate("add")).pack(pady=5)
tk.Button(root, text="Subtract", command=lambda: calculate("subtract")).pack(pady=5)
tk.Button(root, text="Multiply", command=lambda: calculate("multiply")).pack(pady=5)
tk.Button(root, text="Divide", command=lambda: calculate("divide")).pack(pady=5)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
