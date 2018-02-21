import re

def get_numbers(value, separator):
    value = list(map(int, str.split(sep=separator)))
    return sum(value)

def get_separator(inpt):
    return inpt[2:inpt.startswith(//)]

def add(value):
    if value == '':
        return "0"
    else:
        return str(sum(get_numbers(value)))

#num_input = [0]
#result = sum(map(int,num_input))