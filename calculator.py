import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "add":
            result = num1 + num2
        elif operation == "sub":
            result = num1 - num2
        elif operation == "mul":
            result = num1 * num2
        elif operation == "div":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2

        text_area.insert(tk.END, f"{num1} {operation} {num2} = {result}\n")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero!")

root = tk.Tk()
root.title("Basic Calculator (Buttons + Text Box + Text Area)")
root.geometry("400x350")

tk.Label(root, text="Enter Number 1:").pack()
entry1 = tk.Entry(root, width=30)
entry1.pack(pady=5)

tk.Label(root, text="Enter Number 2:").pack()
entry2 = tk.Entry(root, width=30)
entry2.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="+ Add", width=10, command=lambda: calculate("add")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="- Sub", width=10, command=lambda: calculate("sub")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="* Mul", width=10, command=lambda: calculate("mul")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="/ Div", width=10, command=lambda: calculate("div")).grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Results:").pack()
text_area = tk.Text(root, height=8, width=40)
text_area.pack(pady=5)

root.mainloop()
