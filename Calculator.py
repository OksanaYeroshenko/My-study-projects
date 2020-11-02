"""
HW2
Calculator
"""
import tkinter as tk


def validate_input():
    """
    Tries to compile entered expression, checks for unallowed names.
    :return: compiled code or None
    """
    expr = ent_expr.get()
    try:
        code = compile(expr, "<string>", "eval")
    except SyntaxError:
        lbl_display_result["text"] = f"Invalid syntax"
        return None
    for name in code.co_names:
        if name not in allowed_names:
            lbl_display_result["text"] = f"Use any names isn`t allowed"
            return None
    return code


def eval_expression():
    """
    Evaluates validated code
    """
    code = validate_input()
    if code is not None:
        try:
            result = eval(code, {"__builtins__": {}}, allowed_names)
            lbl_display_result["text"] = f"{result}"
        except ZeroDivisionError:
            lbl_display_result["text"] = "Cannot be divided by zero"
        except Exception:
            lbl_display_result["text"] = "Unknown error during calculation"


allowed_names = {'pi': 3.14, 'e': 2.71}

window = tk.Tk()
window.title("Calculator")

lbl_entry_window = tk.Label(master=window, text="Enter an expression to calculate:", font=('Ubuntu', 20))
lbl_entry_window.grid(row=2, column=0, pady=10)

ent_expr = tk.Entry(master=window, width=30, font=('Ubuntu', 20))
ent_expr.grid(row=4, column=0, pady=10)

btn_get_res = tk.Button(master=window, text="Get result", command=eval_expression, font=('Ubuntu', 20))
btn_get_res.grid(row=6, column=0, pady=10)

lbl_result = tk.Label(master=window, text="Calculation result:", font=('Ubuntu', 20))
lbl_result.grid(row=8, column=0, pady=10)

lbl_display_result = tk.Label(master=window, font=('Ubuntu', 20))
lbl_display_result.grid(row=10, column=0)

window.mainloop()
