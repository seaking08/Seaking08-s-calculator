import gui.notebook_main as gui_main
from gui.frame_calculator import create_frame1_widgets
from gui.frame_table import create_frame2_widgets
from gui.frame_solve_func import create_frame3_widgets
from gui.frame_sett_and_inf import create_setting_frame_widgets, create_info_frame_widget
from tab.calculation.calc import calc_setup

if __name__ == "__main__":
    calc_setup()
    gui_main.create_app()
    gui_main.create_notebook()
    create_frame1_widgets()
    create_frame2_widgets()
    create_frame3_widgets()
    create_setting_frame_widgets()
    create_info_frame_widget()
    gui_main.run_app()