import sys
from ttkthemes import ThemedStyle
import tkinter as tk

def create_var():
    global bold_text_var, bold_text_table_var, style,style_var, max_var, bold_text_equal_var, degree_unit_var
    sys.set_int_max_str_digits(10000)
    style = ThemedStyle()
    style.set_theme("vista")
    bold_text_var = tk.BooleanVar()
    bold_text_var.set(True)
    bold_text_table_var = tk.BooleanVar()
    bold_text_table_var.set(True)
    bold_text_equal_var = tk.BooleanVar()
    bold_text_equal_var.set(True)
    style_var = tk.StringVar()
    style_var.set("Layout: " + style.theme_use())
    max_var = tk.StringVar()
    max_var.set("Length max number: 10000")
    degree_unit_var = tk.StringVar()
    degree_unit_var.set("Degree unit: degrees")
def save_settings(setting):
    global display
    if setting == "bold_text": bold_text_setting()

def bold_text_setting():
    import gui.frame_calculator as frame_calc
    import gui.frame_table as frame_table
    import gui.frame_solve_func as frame_solve
    if bold_text_var.get():
        frame_calc.display.config(font=("Arial",20,"bold"))
    else:
        frame_calc.display.config(font=("Arial",20,"normal"))
    if bold_text_table_var.get():
        frame_table.display_list.config(font=("Arial",8,"bold"))
    else:
        frame_table.display_list.config(font=("Arial",8,"normal"))
    if bold_text_equal_var.get():
        frame_solve .output_listbox.config(font=("Arial", 8, "bold"))
    else:
        frame_solve .output_listbox.config(font=("Arial", 8, "normal"))
    frame_calc.display.update()
    frame_table.display_list.update()
    frame_solve .output_listbox.update()

def set_style(type):
    style.set_theme(type)
    style_var.set("Layout: " + style.theme_use())

def set_max_number_length(val):
    sys.set_int_max_str_digits(val)
    max_var.set("Length max number: " + str(val))

def set_degree_unit_var(val):
    degree_unit_var.set(val)