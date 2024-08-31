import tkinter as tk
from tkinter import messagebox

# Define basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Function to evaluate the expression
def evaluate_expression():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        
        result_var.set(result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Input fields
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Labels
tk.Label(root, text="First Number:").grid(row=0, column=0)
tk.Label(root, text="Second Number:").grid(row=1, column=0)

# Dropdown for operation selection
operation_var = tk.StringVar(root)
operation_var.set("+")  # Default operation

operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=2, column=1, padx=10, pady=10)

# Button to calculate the result
calculate_button = tk.Button(root, text="Calculate", command=evaluate_expression)
calculate_button.grid(row=3, column=1, padx=10, pady=10)

# Result display
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.grid(row=4, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
