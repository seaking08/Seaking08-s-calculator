import sympy as sp
import gui.frame_solve_func as frame_solve

def get_parameters(func1,func2,var_sign):
    try:
        check = check_function_sign(func1,var_sign)
        if check == "Error":
            error_message(func1, func2, 0, "Error! Wrong function.", "Functions are only allowed to contain numbers,points and variables.")
            return
        check = check_function_sign(func2, var_sign)
        if check == "Error":
            error_message(func1, func2, 0, "Error! Wrong function.", "Functions are only allowed to contain numbers,points and variables.")
            return
        if func1 == "" or func2 == "" or var_sign == "":
            error_message(func1,func2,0, "Error! Not all parameters are given.", "All parameters must be given.")
            return
        if var_sign in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] or len(var_sign) > 1:
            error_message(func1,func2,0, "Error! Variable must be one letter!", f"'{var_sign}' is not a letter.")
            return
        solution = solve_equation(func1 + "-(" + func2 + ")",var_sign)
        if solution == "ValueError":
            raise ValueError
        frame_solve.output_listbox.insert(0, f"solution {solution} from equation {func1} = {func2}")
    except Exception as e:
        error_message(func1,func2,0,"Error! Can't solve equation.","Maybe you forgot a the arithmetic symbol?","Maybe you used a wrong variable?")

def check_function_sign(func,var_sign):
    from tab.calculation.calc_reader import keyword_tuple
    m_keyword = ""
    counter = 0
    while counter > len(func):
        if not func[counter] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","*","/","+","-",".","(",")",var_sign]:
            for x in range(3):
                m_keyword += func[counter]
                counter += 1
            if not m_keyword in keyword_tuple:
                return "Error"
        counter += 1
    return "Okay"

def error_message(func1,func2,position,text,tip,tip2=""):
    frame_solve.output_listbox.insert(position, text + " Equation: " + func1 + " = " + func2)
    frame_solve.output_listbox.itemconfig(position, {"fg": "red"})
    frame_solve.output_listbox.insert(position + 1,tip)
    frame_solve.output_listbox.itemconfig(position + 1, {"fg": "green"})
    frame_solve.output_listbox.insert(position + 2, tip2)
    frame_solve.output_listbox.itemconfig(position + 2, {"fg": "green"})

def solve_equation(equation_str, variable_str):
    variable = sp.symbols(variable_str)
    equation = sp.sympify(equation_str)

    solution = sp.solve(equation, variable)
    solution_check = check_solution(solution)
    if solution_check == "ValueError":
        return "ValueError"
    elif solution_check == "Complex":
        return str(solution) + " [COMPLEX]"
    else:
        return solution


def check_solution(solution):
    from tab.calculation.calc_reader import read_calculation, set_to_calculate
    for i in range(len(solution)):
        if "I" in str(solution[i]):
            return "Complex"
        set_to_calculate("none")
        set_to_calculate(solution[i])
        if read_calculation(str(solution[i])) == "ValueError":
            return "ValueError"

def delete_output():
    frame_solve.output_listbox.delete(0,frame_solve.tk.END)