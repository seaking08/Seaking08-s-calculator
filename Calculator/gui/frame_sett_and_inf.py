import tkinter as tk
from tkinter import ttk
import gui.notebook_main as notebook
from tab import settings as sett

def create_setting_frame_widgets():
    global style
    sett.create_var()
    set_label1 = ttk.Label(notebook.setting_frame,text="Calculator",font=("Arial",10,"bold")).place(x=0,y=0)
    set_label2 = ttk.Label(notebook.setting_frame,text="Table",font=("Arial",10,"bold")).place(x=0,y=70)
    set_label3 = ttk.Label(notebook.setting_frame,text="Equation",font=("Arial",10,"bold")).place(x=0,y=120)
    set_label4 = ttk.Label(notebook.setting_frame,text="System",font=("Arial",10,"bold")).place(x=0,y=170)

    checkbutton_bold = ttk.Checkbutton(notebook.setting_frame, text="bold calc text", variable=sett.bold_text_var, command=lambda:sett.save_settings("bold_text")).place(x=0,y=20)

    degree_unit_button = ttk.Menubutton(notebook.setting_frame, textvariable=sett.degree_unit_var)
    degree_unit_button.place(x=0, y=40)
    degree_units = tk.Menu(degree_unit_button, tearoff=0)
    degree_units.add_command(label="degrees", command=lambda: sett.set_degree_unit_var("Degree unit: degrees"))
    degree_units.add_command(label="radians", command=lambda: sett.set_degree_unit_var("Degree unit: radians"))
    degree_unit_button["menu"] = degree_units

    checkbutton_bold_equal = ttk.Checkbutton(notebook.setting_frame, text="bold equal text", variable=sett.bold_text_equal_var, command=lambda:sett.save_settings("bold_text")).place(x=0,y=90)
    checkbutton_bold_table = ttk.Checkbutton(notebook.setting_frame, text="bold table text", variable=sett.bold_text_table_var, command=lambda:sett.save_settings("bold_text")).place(x=0,y=140)

    style_button = ttk.Menubutton(notebook.setting_frame,textvariable=sett.style_var)
    style_button.place(x=0,y=195)
    styles = tk.Menu(style_button,tearoff=1)
    forbidden_styles = ["ubuntu", "radiance", "adapta"]

    for i in sett.style.get_themes():
        if not i in forbidden_styles:   styles.add_command(label=i, command=lambda theme=i: sett.set_style(theme))
    style_button["menu"] = styles

    max_number_button = ttk.Menubutton(notebook.setting_frame,textvariable=sett.max_var)
    max_number_button.place(x=0,y=220)
    values = tk.Menu(max_number_button,tearoff=0)

    for i in [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,1000000,10000000]:
        values.add_command(label=str(i),command=lambda val=i: sett.set_max_number_length(val))
    max_number_button["menu"] = values

def create_info_frame_widget():
    info_label = ttk.Label(notebook.info_frame,text="This is calculator version 2.1.0 .\nMade by Seaking08 "
                                           "\n\nNew features in 1.1: info, trigonometric calc, pi\nNew features in 1.2: settings, themes\n"
                                           "New features in 1.2.1: Bug fixed \n(MAX/MIN/STEPS not numbers), added new Pythonfiles [BG]\n"
                                           "New features in 1.3: Solving two functions\n\nNew features in 2.0: New calculation reader [BG],\n"
                                            "better trigonometric (asin, acos, atan; two degree units; \nusable in calc/table)"
                                            "added const e, reworked gui in calc\nNew features in 2.1.0: Added trigonometrical support\n"
                                            "in the solver,pi and e are now 'pi' and 'e' in calc, pi and e \nsupport in table and solver,"
                                            "sqrt surpport in table").place(x=0,y=0)