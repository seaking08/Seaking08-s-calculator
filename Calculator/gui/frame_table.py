import tkinter as tk
from tkinter import ttk
import gui.notebook_main as notebook
from tab.table import *

def create_frame2_widgets():
    global progress, display_list
    scroll_y_display_list = ttk.Scrollbar(notebook.frame2, orient="vertical")
    scroll_y_display_list.place(x=320, y=0, height=390)
    scroll_x_display_list = ttk.Scrollbar(notebook.frame2, orient="horizontal")
    scroll_x_display_list.place(x=0, y=390, width=330)

    display_list = tk.Listbox(notebook.frame2, width=53, height=26, yscrollcommand=scroll_y_display_list.set, xscrollcommand=scroll_x_display_list.set,font=("Arial",8,"bold"))
    display_list.place(x=0, y=0)

    scroll_y_display_list.config(command=display_list.yview)
    scroll_x_display_list.config(command=display_list.xview)

    lable1 = ttk.Label(notebook.frame2,text="function with var x:").place(x=0,y=405)
    lable2 = ttk.Label(notebook.frame2,text="Min value of x:").place(x=0,y=425)
    lable3 = ttk.Label(notebook.frame2,text="Max value of x:").place(x=0,y=445)
    lable4 = ttk.Label(notebook.frame2,text="Steps:").place(x=0,y=465)

    entry1 = ttk.Entry(notebook.frame2)
    entry1.place(x=150,y=405)
    entry2 = ttk.Entry(notebook.frame2)
    entry2.place(x=150,y=425)
    entry3 = ttk.Entry(notebook.frame2)
    entry3.place(x=150,y=445)
    entry4 = ttk.Entry(notebook.frame2)
    entry4.place(x=150,y=465)

    button_start = tk.Button(notebook.frame2,text="Start",bg="green",fg="white",command=lambda: table_setup(entry1.get(),entry2.get(),entry3.get(),entry4.get())).place(x=5,y=490)
    button_stop = tk.Button(notebook.frame2, text="Stop",bg="orange",fg="white",command=stop_table).place(x=50,y=490)
    button_delete = tk.Button(notebook.frame2,text="Delete",bg="red",fg="white", command=lambda: display_list.delete(0,tk.END)).place(x=95,y=490)

    progress = ttk.Progressbar(notebook.frame2,length=180, mode="determinate")
    progress.place(x=150,y=492)
    progress["maximum"] = 100