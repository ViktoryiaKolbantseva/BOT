import logger_calc
import rational_calc
import rational_num
import controls
import calc_complex_numbers

print("Давайте посчитаем!")
calc_type = controls.start_calc()
if calc_type == 1:
    expression = controls.input_rational()
    if len(expression) == 1:
        evaluate = rational_calc.my_eval(expression[0])
    else:
        evaluate = rational_num.calculator_block(*expression)
else:
    expression = controls.input_complex()
    evaluate = calc_complex_numbers.Calc_block(*expression)
try:
    if len(expression) > 1:
        result = f"{str(expression[0]+expression[1]+expression[2])} = {evaluate}"
    else:
        result = f"{str(expression[0])} = {evaluate}"
except TypeError:
    result = f"{expression[0]}{str(expression[1])}{expression[2]} = {evaluate}"
print(result)
logger_calc.result_logger(result=result)

def view_data(data, title):
    print(f'{title} = {data}')


def get_value():
    return input()


def input_data():
    print(f'Choose:\n1 - for working with complex numbers (a + bi)\n2 - for working with rational numbers')
    data_type = get_value()
    if data_type == '1':
        print('Enter first number: ')
        first_value = get_value()
        print('Enter second number: ')
        second_value = get_value()
        print('Select an action (+, -, /, *):')
        action = get_value()
    elif data_type == '2':
        print('Enter first number: ')
        first_value = get_value()
        print('Enter second number: ')
        second_value = get_value()
        print('Select an action (+, -, /, *):')
        action = get_value()
    return (data_type, first_value, action, second_value)
