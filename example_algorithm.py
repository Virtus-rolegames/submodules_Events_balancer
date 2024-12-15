import math
from typing import List

from example_data import Event, gen_use_some

current_round = 4
max_round = 7


possibles = Event.gen_possible()
events = gen_use_some(possibles, current_round)


def calc_curr_bal(used: List[Event]):
    bal = [0, 0, 0, 0]
    for event in used:
        bal[0] += event.bal[0]
        bal[1] += event.bal[1]
        bal[2] += event.bal[2]
        bal[3] += event.bal[3]
    return bal


def analyzer(curr_bal: List[int]):
    result = False
    sum = 0
    for i in curr_bal:
        if i:
            ...
    return result


def balancer(current: int, max: int, possible: List[Event], used: List[Event]):

    result = "error or smth"
    if current >= math.ceil(max/2):
        if analyzer(calc_curr_bal(used)):
            variants: List[int] = []
            for event in possible:
                ...
        else:
            result = "it's ok already"
    else:
        result = "it's not the time"
    return result


print(balancer(current_round,max_round,events[0],events[1]))
