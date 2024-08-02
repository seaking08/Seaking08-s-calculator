import gui.frame_table as frame_table

table_run = True

def error_catching_display_list(f=0, min_val=0, max_val=0, step=0) -> bool:
    global error, error_counter
    error = False
    error_counter = 0
    try:
        if max_val == "" or min_val == "":
            error = error_display_list(error_counter, "NotGivenError! MAX and MIN must be given!")
            error_counter += 1
        elif int(max_val) <= int(min_val):
            error = error_display_list(error_counter,"ValueError! MAX <= MIN")
            error_counter += 1
        if step == "":
            error = error_display_list(error_counter, "NotGivenError! Step must be given!")
            error_counter += 1
        elif 1 > float(step):
            error = error_display_list(error_counter, "ValueError! Step must be taller or equal 1!")
            error_counter += 1
        if "x" not in f:
            error = error_display_list(error_counter, "NotGivenError! No x given!")
            error_counter += 1
    except ValueError:
        error = error_display_list(error_counter, "TypeError! Type of MAX,MIN and STEPS must be number!")
        error_counter += 1
    finally:
        return error

def error_display_list(ec,message):
    frame_table.display_list.insert(ec, message)
    frame_table.display_list.itemconfig(ec, {"fg": "red"})
    return True

def table_setup(f, min_val, max_val, step):
    from tab.calculation.calc_reader import read_calculation, set_to_calculate
    global end_function, table_run
    if error_catching_display_list(f, min_val, max_val, step): return 0
    max_val = int(max_val)
    min_val = int(min_val)
    step = int(step)

    for n in range(min_val, max_val + 1, step):
        if table_run == False: break
        frame_table.progress["value"] = (n/max_val) * 100
        end_function = ""
        for i in f:
            if str(i) == "x":
                end_function = end_function + str(n)
            else:
                end_function = end_function + str(i)
        try:
            set_to_calculate(str(end_function))
            result = str(read_calculation(end_function))
            frame_table.display_list.insert(0, str(end_function) + "=" + result + " with x = " + str(n))
            if "Error" in result:
                frame_table.display_list.itemconfig(0, {"fg": "orange"})
            else:
                frame_table.display_list.itemconfig(0, {"fg": "black"})
            set_to_calculate("none")
            frame_table.display_list.update()
        except SyntaxError:
            error_display_list(0,"SyntaxError! Function is invalid!")
            table_run = False
        except ValueError:
            error_display_list(0, "ValueError! To large Number!")
            table_run = False
    table_run = True

def stop_table():
    global table_run
    table_run = False
