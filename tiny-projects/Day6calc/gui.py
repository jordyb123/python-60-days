import tkinter as tk
from tkinter import ttk
from unittest import result
from calculator import *

root = tk.Tk()
root.title("Jordan's Calculator")
root.geometry("400x500")

input1 = tk.Entry(root, font=("Arial", 14))
input1.pack(pady=10)

input2 = tk.Entry(root, font=("Arial", 14))
input2.pack(pady=10)

result_label = tk.Label(root, text="Result: ", font=("Arial", 16))
result_label.pack(pady=20)

def show_result(value):
    result_label.config(text=f"Result: {value}")

def do_add():
    a = float(input1.get())
    b = float(input2.get())
    show_result(add(a, b))

def do_subtract():
    a = float(input1.get())
    b = float(input2.get())
    show_result(subtract(a, b))

def do_multiply():
    a = float(input1.get())
    b = float(input2.get())
    show_result(multiply(a, b))

def do_divide():
    a = float(input1.get())
    b = float(input2.get())
    result = divide(a, b)
    show_result("Error" if result is None else result)

ttk.Button(root, text="Add", command=do_add).pack(pady=5)
ttk.Button(root, text="Subtract", command=do_subtract).pack(pady=5)
ttk.Button(root, text="Multiply", command=do_multiply).pack(pady=5)
ttk.Button(root, text="Divide", command=do_divide).pack(pady=5)

root.mainloop()