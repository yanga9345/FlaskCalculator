def safe_eval(expr_str):
    return eval(expr_str, {"__builtins__": None}, None)