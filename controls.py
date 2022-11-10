import logger_calc
import fractions


def start_calc(calc_type=None):
    print("Какой калькулятор вам нужен?")
    while calc_type not in [1, 2]:
        try:
            calc_type = int(input("1 - для рациональных чисел, 2 - для комплексных чисел: "))
        except ValueError:
            print("Повторите ввод типа калькулятора")
            logger_calc.result_logger(result="Некорректный ввод вида калькулятора")
            continue

    return calc_type


def input_rational():
    nums_to_work = []
    when_to_stop = False
    for elem in range(1, 4):
        if elem == 3:
            operation = input("Какую операцию производим? Доступны: + - * / ")
            while operation not in ["+", "-", "*", "/"]:
                message = "Введен неподдерживаемый знак операции"
                print(message)
                logger_calc.result_logger(message)
                operation = input("Повторите ввод знака? Доступны: + - * / ")
            nums_to_work.insert(1, operation)
            continue
        else:
            while True:
                a = input(f"Введите {elem} числo ")
                if expr_check(a):
                    nums_to_work.append(a)
                    when_to_stop = True
                    break
                elif len(a.split("/")) == 2:
                    try:
                        a = fractions.Fraction(*(int(i) for i in a.split("/")))
                        nums_to_work.append(a)
                    except (ValueError, ZeroDivisionError):
                        message = "Числитель/знаменатель дроби - не число"
                        print(message)
                        logger_calc.result_logger(message)
                    break
                else:
                    nums_to_work.append(int(a))
                    break
        if when_to_stop:
            break

    return nums_to_work


def expr_check(string):
    """проверяем не ввел ли пользователь стразу строку"""
    num_operations = []
    for i in ["+", "-", "**", "/", "^", "*"]:
        if i in string:
            num_operations.append(string.find(i))
        else:
            pass
    if len(set(num_operations)) >= 2:
        return True
    else:
        return False


def input_complex():
    nums_to_work = []
    for i in range(1, 4):
        while len(nums_to_work) < 3:
            if i == 3:
                operation = input("Какую операцию производим? Доступны: + - * / ")
                while operation not in ["+", "-", "*", "/"]:
                    message = "Введен неподдерживаемый знак операции"
                    print(message)
                    logger_calc.result_logger(message)
                    operation = input("Повторите ввод знака? Доступны: + - * / ")
                nums_to_work.insert(1, operation)
                continue
            else:
                try:
                    a, b = map(float,
                               input(f"Введите через пробел действительную и мнимую части {i} числа ").split(" "))
                    nums_to_work.append(complex(a, b))
                    break
                except ValueError:
                    message = "Некорректный ввод части числа"
                    print(message)
                    logger_calc.result_logger(result=message)
                    continue
                except UnboundLocalError:
                    message = "Отсутствует одна из частей комплексного числа"
                    print(message)
                    logger_calc.result_logger(result=message)
                    continue
                except KeyboardInterrupt:
                    message = "Работа прервана пользователем"
                    print(message)
                    logger_calc.result_logger(result=message)
                    break
    return nums_to_work



from datetime import datetime


def result_logger(result):
    current_date = datetime.now()
    current_date_string = current_date.strftime(' %m/%d/%y %H:%M')
    with open('log.csv', 'a', encoding='cp1251') as file:
        file.write(f'{current_date_string}  результат: {result}\n')
