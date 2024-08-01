import tkinter as tk
from tkinter import ttk
from tkinter import font
import gui.notebook_main as notebook
from tab.calculation.calc import add, calculate
from tab.calculation.trig_calc import calc_sqrt
from math import pi, e

def create_button(frame, name, text, to_display, to_back, x, y,):
    name = ttk.Button(frame, text=text, style="Custom.TButton", command=lambda: add(to_display, to_back))
    name.place(x=x, y=y, height=85, width=65)

def create_frame1_num_widgets():
    arial_font = font.Font(family="Arial", size=20)
    style = ttk.Style()
    style.configure("Custom.TButton", font=arial_font)
    create_button(notebook.frame1_num, "button1", 1, 1, 1, 0, 0)
    create_button(notebook.frame1_num, "button2", 2, 2, 2,68, 0)
    create_button(notebook.frame1_num, "button3", 3, 3, 3,136,0)
    create_button(notebook.frame1_num, "button4", 4, 4, 4,0, 90)
    create_button(notebook.frame1_num, "button5", 5, 5, 5,68, 90)
    create_button(notebook.frame1_num, "button6", 6, 6, 6,136, 90)
    create_button(notebook.frame1_num, "button7", 7, 7, 7,0, 180)
    create_button(notebook.frame1_num, "button8", 8, 8, 8,68, 180)
    create_button(notebook.frame1_num, "button9", 9, 9, 9, 136, 180)
    create_button(notebook.frame1_num, "button0", 0, 0, 0, 0, 270)

def create_frame1_trig_widgets():
    create_button(notebook.frame1_trig, "buttonSIN", "sin", "sin(", "_sin(", 0, 0)
    create_button(notebook.frame1_trig, "buttonCOS", "cos", "cos(", "_cos(", 67, 0)
    create_button(notebook.frame1_trig, "buttonTAN", "tan", "tan(", "_tan(", 134, 0)
    create_button(notebook.frame1_trig, "buttonASIN", "asin", "asin(", "_asin(", 0, 90)
    create_button(notebook.frame1_trig, "buttonACOS", "acos", "acos(", "_acos(", 67, 90)
    create_button(notebook.frame1_trig, "buttonATAN", "atan", "atan(", "_atan(", 134, 90)

def create_frame1_ex_widgets():
    create_button(notebook.frame1_ex, "buttonEX", "^x", "**", "**", 0, 0)
    buttonSQRT = ttk.Button(notebook.frame1_ex, text="sqrt", style="Custom.TButton", command=calc_sqrt).place(x=67, y=0, height=85, width=65)

def create_frame1_widgets():
    global display
    create_frame1_num_widgets()
    create_frame1_trig_widgets()
    create_frame1_ex_widgets()
    buttonE = tk.Button(notebook.frame1, text="=",height=5,width=8,command=lambda: calculate(), bg="light green").place(x=68,y=395)
    buttonC = tk.Button(notebook.frame1, text="C",height=5,width=8,command=lambda: add("none", "none"), bg="red").place(x=136,y=395)
    buttonM = tk.Button(notebook.frame1, text="-",height=5,width=8,command=lambda: add("-", "-"),bg="light blue").place(x=204,y=125)
    buttonP = tk.Button(notebook.frame1, text="+",height=5,width=8,command=lambda: add("+", "+"),bg="light blue").place(x=204,y=215)
    buttonMA = tk.Button(notebook.frame1, text="*",height=5,width=8,command=lambda: add("*", "*"),bg="light blue").place(x=272,y=125)
    buttonT = tk.Button(notebook.frame1, text="/",height=5,width=8,command=lambda: add("/", "/"),bg="light blue").place(x=272,y=215)
    buttonD = tk.Button(notebook.frame1, text=".",height=5,width=8,command=lambda: add(".", "."),bg="cyan").place(x=204,y=395)
    buttonKO = tk.Button(notebook.frame1, text="(",height=5,width=8,command=lambda: add("(", "("),bg="cyan").place(x=204,y=305)
    buttonKC = tk.Button(notebook.frame1, text=")",height=5,width=8,command=lambda: add(")", ")"),bg="cyan").place(x=272,y=305)
    buttonANS = tk.Button(notebook.frame1, text="ANS",height=5,width=8,command=lambda: add("ans", "ans"), bg="yellow").place(x=272,y=395)
    buttonPI = ttk.Button(notebook.frame1, text="π", command=lambda: add("pi", str(pi))).place(height=25, width=67, x=0, y=485)
    buttonEconst = ttk.Button(notebook.frame1, text="e", command= lambda: add("e", str(e))).place(height=25, width=67, x=68, y=485)

    scroll_display = ttk.Scrollbar(notebook.frame1,orient="vertical")
    scroll_display.place(x=320,y=0, height=100)

    display = tk.Text(notebook.frame1, height=3,width=21,font=("Arial",20,"bold"),state="disabled",yscrollcommand=scroll_display.set)
    display.place(x=0,y=0)
    scroll_display.config(command=display.yview)