import tkinter as tk
from tkinter import ttk

def create_app():
    global app
    app = tk.Tk()
    app.title("Calculator")
    app.geometry("338x540")
    app.resizable(False,False)

def run_app():
    app.mainloop()

def create_notebook():
    global tab, frame1, frame1_num, frame1_trig, frame1_ex, frame2, frame3, setting_frame, info_frame
    tab = ttk.Notebook(app)
    tab.place(x=0,y=0,width=338, height=540)

    frame1 = ttk.Frame(tab)

    test = ttk.Notebook(frame1)
    test.place(x=0, y=100, width=338, height=540)

    frame1_num = ttk.Frame(test)
    frame1_trig = ttk.Frame(test)
    frame1_ex = ttk.Frame(test)

    frame2 = ttk.Frame(tab)
    frame3 = ttk.Frame(tab)
    setting_frame = ttk.Frame(tab)
    info_frame = ttk.Frame(tab)

    tab.add(frame1, text='calc')
    tab.add(frame2, text='table')
    tab.add(frame3, text='equal')
    tab.add(setting_frame, text='sys')
    tab.add(info_frame, text='info')

    test.add(frame1_num, text="num")
    test.add(frame1_trig, text="trig")
    test.add(frame1_ex, text="ex")