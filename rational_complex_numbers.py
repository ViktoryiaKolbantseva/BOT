# Блок для расчетов операций с комплексными числами


def Calc_block(left_value, oper, right_value):
    if oper == '+':
        res = sum(left_value, right_value)
    elif oper == '-':
        res = sub(left_value, right_value)
    elif oper == '*':
        res = mult(left_value, right_value)
    else:
        try:
            res = div(left_value, right_value)
        except ZeroDivisionError:
            res = "Ошибка деления на 0!"

    return res


def sum(left_value: complex, right_value: complex):
    return left_value + right_value


def sub(left_value: complex, right_value: complex):
    return left_value - right_value


def mult(left_value: complex, right_value: complex):
    return left_value * right_value


def div(left_value: complex, right_value: complex):
    return left_value / right_value
    
    
    
    

def my_eval(expresion):
    actions = {
        "^": lambda x, y: str(float(x) ** float(y)),
        "*": lambda x, y: str(float(x) * float(y)),
        "/": lambda x, y: str(float(x) / float(y)),
        "+": lambda x, y: str(float(x) + float(y)),
        "-": lambda x, y: str(float(x) - float(y))
    }

    priority_reg_exp = r"\((.+?)\)"
    action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"

    while (match := re.search(priority_reg_exp, expresion)):
        expresion: str = expresion.replace(match.group(0), my_eval(match.group(1)))  # рекурсия

    for symbol, action in actions.items():
        while (match := re.search(action_reg_exp.format(symbol), expresion)):
            if symbol == "+":
                expresion: str = expresion.replace(match.group(0), symbol + action(*match.groups()))
                if expresion.find(symbol) == 0:
                    expresion: str = expresion[1:]
                else:
                    pass
            else:
                expresion: str = expresion.replace(match.group(0), action(*match.groups()))

    return expresion
