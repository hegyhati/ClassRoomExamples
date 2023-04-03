def increase(number, increase_by):
    return number + increase_by

def increase_by_one(number):
    return number + 1

def increase_specially_by_one(number):
    return increase(number, 1)


def double_elements(list):
    l = []
    for item in list:
        l.append(item*2)
    return l

def triple_elements(list):
    l = []
    for item in list:
        l.append(item*3)
    return l

def get_multiplied_elements(list, multiplier):
    l = []
    for item in list:
        l.append(item*multiplier)
    return l

def get_doubled_elements_2(list):
    return get_multiplied_elements(list, 2)

def get_tripled_elements_2(list):
    return get_multiplied_elements(list, 3)

def get_negated_elements_2(list):
    return get_multiplied_elements(list,-1)

from functools import partial

get_negated_elements_3 = partial(get_multiplied_elements, multiplier=-1)

def get_increased_by_one_elements(list):
    l = []
    for item in list:
        l.append(item+1)
    return l

def get_decreased_by_one_elements(list):
    l = []
    for item in list:
        l.append(item-1)
    return l

def get_elements_increased_by(list, value):
    l = []
    for item in list:
        l.append(item+value)
    return l

def get_increased_by_one_elements_2(list):
    return get_elements_increased_by(list, 1)

def get_decreased_by_one_elements_2(list):
    return get_elements_increased_by(list, -1)

get_increased_by_one_elements_3 = partial(get_elements_increased_by, value=1)
get_decreased_by_one_elements_3 = partial(get_elements_increased_by, value=-1)


def get_modified_list(list, modifier):
    l = []
    for item in list:
        l.append(modifier(item))
    return l

def get_increased_by_one_elements_4(list):
    return get_modified_list(list,increase_by_one)

get_increased_by_one_elements_5 = partial(get_modified_list, modifier=increase_by_one)


def increase_by_two(number):
    return number+2

get_increased_by_two_elements_5 = partial(
    get_modified_list, 
    modifier=increase_by_two
)

get_increased_by_three_elements_5 = partial(
    get_modified_list, 
    modifier=partial(increase,increase_by=3)
)

get_increased_by_three_elements_6 = partial(
    get_modified_list, 
    modifier = lambda x: x+3
)

get_squares_of_elements_6 = partial(
    get_modified_list, 
    modifier = lambda x: x**2
)

print(get_modified_list(
    range(1,11),
    lambda x: x**0.5
))





