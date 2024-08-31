import tkinter as tk
from tkinter import messagebox

# Function to update the input field whenever a button is clicked
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
            messagebox.showerror("Error", "Invalid Input")
        screen.update()
    elif text == "C":
        screen_var.set("")
        screen.update()
    else:
        screen_var.set(screen_var.get() + text)
        screen.update()

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("400x400")

# StringVar to hold the value of the input field
screen_var = tk.StringVar()

# Entry widget to display the input
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold", bd=10, relief=tk.SUNKEN)
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack()

# List of button texts
buttons = [
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "C", "0", "=", "/"
]

# Adding buttons to the frame
row = 0
col = 0
for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font="lucida 15 bold", width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the main loop
root.mainloop()
