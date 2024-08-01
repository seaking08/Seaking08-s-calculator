import math
from tkinter import ttk
from tab.calculation.calc import *

def calc_sqrt():
    global entry_rad, entry_ex, entry_nth, calc_sqrt_app, is_window
    try:
        if calc_sqrt_app.winfo_exists():
            is_window = True
        else:
            is_window = False
    except Exception:
        is_window = False
    if not is_window:
        calc_sqrt_app = tk.Tk()
        calc_sqrt_app.title("Square")
        calc_sqrt_app.geometry("230x120")
        calc_sqrt_app.resizable(False, False)
        lable_sqrt_nth = tk.Label(calc_sqrt_app, text="nth root:").grid(column=1,row=1)
        entry_nth = ttk.Entry(calc_sqrt_app)
        entry_nth.grid(column=2,row=1)
        lable_sqrt_rad = tk.Label(calc_sqrt_app, text="radical:").grid(column=1, row=2)
        entry_rad = ttk.Entry(calc_sqrt_app)
        entry_rad.grid(column=2, row=2)
        lable_sqrt_ex = tk.Label(calc_sqrt_app, text="exponent:").grid(column=1, row=3)
        entry_ex = ttk.Entry(calc_sqrt_app)
        entry_ex.grid(column=2, row=3)
        button_sqrt = tk.Button(calc_sqrt_app, text="calculate sqrt and add to main", command=add_sqrt).grid(column=1, row=4, columnspan=2)
        calc_sqrt_app.mainloop()

def add_sqrt():
    global is_window
    try:
        float(entry_rad.get()), float(entry_ex.get()), float(entry_nth.get())
        add(entry_rad.get() + "**(" + entry_ex.get() + "/" + entry_nth.get() + ")", entry_rad.get() + "**(" + entry_ex.get() + "/" + entry_nth.get() + ")")
        is_window = False
        calc_sqrt_app.destroy()
    except ValueError:
        message_lable = tk.Label(calc_sqrt_app,text="Error! Wrong input!", fg="White", bg="red").grid(column=1, row=5, columnspan=2)