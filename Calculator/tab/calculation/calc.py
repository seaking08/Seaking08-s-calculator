import gui.frame_calculator as frame_calc
import tkinter as tk
from tab.calculation.calc_reader import read_calculation, set_to_calculate

def calc_setup():
    global calc, ans
    calc = ""
    ans = 0.0

def add(n, to_back) -> None:
    global calc, ans
    try:
        if str(n) == "none" or str(n) == "c":
            calc=""
            set_to_calculate("none")
        elif str(n) == "ans":
            calc = calc + str(ans)
            set_to_calculate(str(ans))
        else:
            calc = calc + str(n)
            set_to_calculate(str(to_back))

        if not n == "c":
            add_to_display(calc)
    except ValueError:
        add_to_display("ValueError! To large Number for ANS!")

def add_to_display(text):
    try:
        frame_calc.display.config(state="normal")
        if "Error" in str(text):
            frame_calc.display.config(fg="red")
        else:
            frame_calc.display.config(fg="black")
        frame_calc.display.delete(1.0,tk.END)
        frame_calc.display.insert(1.0, text)
        frame_calc.display.config(state="disabled")
    except ValueError:
        add_to_display("ValueError! To large Number!")
    finally:
        frame_calc.display.config(state="disabled")

def calculate():
    global calc, ans
    try:
        ans = read_calculation(calc)
        if ans == "SyntaxError": raise SyntaxError
        elif ans == "NameError": raise NameError
        elif ans == "ValueError": raise ValueError
        else:
            add_to_display(ans)
            add("c", "c")
    except ZeroDivisionError:
        add_to_display("DivZeroError! Division by 0 are not allowed!")
        add("c", "c")
    except ValueError:
        add_to_display("ValueError! To large Number or wrong input!")
        add("c", "c")
    except SyntaxError:
        add_to_display("SyntaxError!")
        add("c", "c")
    except NameError:
        add_to_display("NameError! Not known keyword!")
        add("c", "c")
