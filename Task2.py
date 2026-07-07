import tkinter as tk
from tkinter import messagebox

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate expression
def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""
        equation.set("")

# Function to clear the display
def clear():
    global expression
    expression = ""
    equation.set("")

# Function to delete last character
def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

# Keyboard input support
def key_press(event):
    key = event.char

    if key in "0123456789+-*/().":
        press(key)
    elif event.keysym == "Return":
        equalpress()
    elif event.keysym == "BackSpace":
        backspace()
    elif event.keysym == "Escape":
        clear()

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="#2C3E50")

expression = ""
equation = tk.StringVar()

# Display
entry = tk.Entry(root, textvariable=equation, font=("Arial", 24),
                 justify="right", bd=10, relief="sunken")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=10)

# Button layout
buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial",18),
                        bg="#27AE60", fg="white",
                        command=equalpress)
    else:
        btn = tk.Button(root, text=text, font=("Arial",18),
                        command=lambda t=text: press(t))
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text="C", font=("Arial",18),
                      bg="red", fg="white", command=clear)
clear_btn.grid(row=5, column=0, columnspan=2,
               sticky="nsew", padx=5, pady=5)

# Backspace button
back_btn = tk.Button(root, text="⌫", font=("Arial",18),
                     bg="orange", command=backspace)
back_btn.grid(row=5, column=2, columnspan=2,
              sticky="nsew", padx=5, pady=5)

# Configure grid
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Enable keyboard support
root.bind("<Key>", key_press)

root.mainloop()