import tab.settings as sett

to_calculate = ""
keyword_tuple = ("sin","cos","tan","asin","acos","atan", "pi","e" , "sqrt")
allowed_signs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "+", "/", "*", "(", ")","_"]

def generate_definitions():
    definition = ""
    if sett.degree_unit_var.get() == "Degree unit: radians":
        degree_unit_convert1 = "degrees"
        degree_unit_convert2 = "1*"
    else:
        degree_unit_convert1 = "radians"
        degree_unit_convert2 = "degrees"
    for i in keyword_tuple:
        if i[0] == "a":
            definition += f"def _{i}(n):\n   return {degree_unit_convert2}({i}(n));\n"
        else:
            definition += f"def _{i}(n):\n   return {i}({degree_unit_convert1}(n));\n"
    return definition

def read_calculation(calc):
    global counter, output
    counter = 0
    for i in calc:
        if counter > len(calc):
            break
        check_keyword_appearance_and_read(calc, i)
        counter += 1

    return calculate(to_calculate)

def calculate(expression):
    try:
        context = {}
        exec("from math import sin, asin, cos, acos, tan, atan, radians, degrees, pi, e, sqrt;\n" + generate_definitions() + "a=" + expression + ";", context)
        a = context["a"]
        return a
    except SyntaxError:
        return "SyntaxError"
    except SyntaxWarning:
        return "SyntaxError"
    except TypeError:
        return "Bad Syntax"
    except ValueError:
        return "ValueError"

def set_to_calculate(string):
    global to_calculate
    if string == "none":
        to_calculate = ""
    else:
        to_calculate += str(string)

def read_keyword(calc, position):
    try:
        m_keyword = ""
        len = 4
        if calc[position] == "p": len = 2
        elif calc[position] == "e":
            m_keyword = "e"
            return True
        for i in range(len):
            if calc[position + i] == "(":
                break
            m_keyword += calc[position + i]
        if m_keyword in keyword_tuple:
            return True
        else:
            return False
    except IndexError:
        return False

def read_keyword_input(calc): #need work
    global counter, to_calculate
    current_letter = ""
    out_sign = 1 #amount (
    in_sign = 0  #amount )
    while len(calc) > counter:
        current_letter = calc[counter]
        if current_letter == ")":
            in_sign += 1
        if current_letter == "(":
            out_sign += 1
        counter += 1

    if out_sign != in_sign:
        return "Missing bracket"
    else:
        return to_calculate

def check_keyword_appearance_and_read(calc, sign):
    global counter, to_calculate
    if sign not in allowed_signs:
        if not read_keyword(calc, counter):
            return "Not known keyword"
        counter += 4
        if read_keyword_input(calc) == to_calculate:
            return True
        else:
            return to_calculate
    else:
        return False