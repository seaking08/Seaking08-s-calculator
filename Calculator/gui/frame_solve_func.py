import tkinter as tk
from tkinter import ttk
import gui.notebook_main as notebook
from tab.solve_func import get_parameters, delete_output

def create_frame3_widgets():
    global entry_var_symbol,entry_func1,entry_func2,output_listbox
    scroll_listbox_x = ttk.Scrollbar(notebook.frame3, orient="horizontal")
    scroll_listbox_x.place(x=0,y=480,width=320)
    scroll_listbox_y = ttk.Scrollbar(notebook.frame3, orient="vertical")
    scroll_listbox_y.place(x=320, y=90, height=400)

    label_title = ttk.Label(notebook.frame3,text="Solve every kind of function",font=("Arial",10,"bold")).place(x=0,y=0)
    label_var_symbol = ttk.Label(notebook.frame3,text="Variable:").place(x=0,y=20)
    entry_var_symbol = ttk.Entry(notebook.frame3)
    entry_var_symbol.place(x=65,y=20)
    label_func1 = ttk.Label(notebook.frame3, text="Function 1:").place(x=0, y=40)
    entry_func1 = ttk.Entry(notebook.frame3)
    entry_func1.place(x=65, y=40)
    label_func2 = ttk.Label(notebook.frame3, text="Function 2:").place(x=0, y=60)
    entry_func2 = ttk.Entry(notebook.frame3)
    entry_func2.place(x=65, y=60)

    solve_button = tk.Button(notebook.frame3, text="solve",bg="green",fg="white",command= lambda: get_parameters(entry_func1.get(),entry_func2.get(),entry_var_symbol.get())).place(x=250,y=30)
    delete_button = tk.Button(notebook.frame3, text="delete",bg="red",fg="white",command= delete_output).place(x=250,y=60)

    output_listbox = tk.Listbox(notebook.frame3,height=24,width=53,xscrollcommand=scroll_listbox_x.set,yscrollcommand=scroll_listbox_y.set)
    output_listbox.place(x=0,y=90)

    scroll_listbox_x.config(command=output_listbox.xview)
    scroll_listbox_y.config(command=output_listbox.yview)