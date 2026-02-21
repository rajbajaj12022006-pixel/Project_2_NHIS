import tkinter as tk
from tkinter import messagebox


def add_to_screen(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear_screen():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    new_text = current[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

def calculate():
    try:
        problem = entry.get()
        if "%" in problem:
            problem = problem.replace("%", "/100")
            
        result = eval(problem)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        messagebox.showerror("Error", "Invalid Expression")

window = tk.Tk()
window.title("Python Calculator")

entry = tk.Entry(window, width=20, font=("Arial", 20), borderwidth=5, justify='right',bg="lightblue")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


tk.Button(window, text="(", width=5, height=2, command=lambda: add_to_screen("(")).grid(row=1, column=0)
tk.Button(window, text=")", width=5, height=2, command=lambda: add_to_screen(")")).grid(row=1, column=1)
tk.Button(window, text="%", width=5, height=2, command=lambda: add_to_screen("%")).grid(row=1, column=2)
tk.Button(window, text="C", width=5, height=2, command=clear_screen, fg="red").grid(row=1, column=3)

tk.Button(window, text="7", width=5, height=2, command=lambda: add_to_screen("7")).grid(row=2, column=0)
tk.Button(window, text="8", width=5, height=2, command=lambda: add_to_screen("8")).grid(row=2, column=1)
tk.Button(window, text="9", width=5, height=2, command=lambda: add_to_screen("9")).grid(row=2, column=2)
tk.Button(window, text="/", width=5, height=2, command=lambda: add_to_screen("/")).grid(row=2, column=3)

tk.Button(window, text="4", width=5, height=2, command=lambda: add_to_screen("4")).grid(row=3, column=0)
tk.Button(window, text="5", width=5, height=2, command=lambda: add_to_screen("5")).grid(row=3, column=1)
tk.Button(window, text="6", width=5, height=2, command=lambda: add_to_screen("6")).grid(row=3, column=2)
tk.Button(window, text="*", width=5, height=2, command=lambda: add_to_screen("*")).grid(row=3, column=3)

tk.Button(window, text="1", width=5, height=2, command=lambda: add_to_screen("1")).grid(row=4, column=0)
tk.Button(window, text="2", width=5, height=2, command=lambda: add_to_screen("2")).grid(row=4, column=1)
tk.Button(window, text="3", width=5, height=2, command=lambda: add_to_screen("3")).grid(row=4, column=2)
tk.Button(window, text="-", width=5, height=2, command=lambda: add_to_screen("-")).grid(row=4, column=3)

tk.Button(window, text="0", width=5, height=2, command=lambda: add_to_screen("0")).grid(row=5, column=0)
tk.Button(window, text=".", width=5, height=2, command=lambda: add_to_screen(".")).grid(row=5, column=1)
tk.Button(window, text="=", width=5, height=2, command=calculate, bg="lightgreen").grid(row=5, column=2)
tk.Button(window, text="+", width=5, height=2, command=lambda: add_to_screen("+")).grid(row=5, column=3)

tk.Button(window, text="← Backspace", width=30, height=2, command=backspace).grid(row=6, column=0, columnspan=4)

window.mainloop()