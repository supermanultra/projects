def multiply(number, multiply):
    print(number * multiply)
def add(number, addition):
    print(number + addition)
def subtract(number, subtracted):
    print(number - subtracted)
def anything(number, operator, number_two):
    multipliers = ['x', '*', 'multiply', 'times']
    additors = ['+', 'plus', 'add']
    subtractors = ['-', 'minus', 'subtract']
    if operator in additors:
        add(number,number_two)
    if operator in multipliers:
        multiply(number, number_two)
    if operator in subtractors:
        subtract(number, number_two)
        
