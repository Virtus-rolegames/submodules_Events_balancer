import math
from typing import List, Dict

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
    for i in range(4):
        sum += curr_bal[i]
        if result:
            if curr_bal[i] > result[1]:
                result = [i, curr_bal[i]]
        elif curr_bal[i] > 2:
            result = [i, curr_bal[i]]
    return result


def finder(param: int, value: int, possibles: List[Event]):
    variants: Dict = {"Value": possibles[0].bal[param], "IDs": [possibles[0].id]}
    delta = variants["Value"] + value
    for possible in possibles:
        if abs(possible.bal[param]+value) == abs(delta):
            variants["IDs"].append(possible.id)
        elif abs(possible.bal[param]+value) < abs(delta):
            variants["Value"] = possible.bal[param]
            variants["IDs"].clear()
            variants["IDs"].append(possible.id)
            delta = variants["Value"] + value
    result = variants["IDs"]
    return result


def balancer(current: int, max: int, possible: List[Event], used: List[Event]):
    result = "error or smth"
    if current >= math.ceil(max/2):
        analyzed = analyzer(calc_curr_bal(used))
        if analyzed:
            variants: List[int] = []
            result = finder(param=analyzed[0], value=analyzed[1], possibles=possible)
        else:
            result = "it's ok already"
    else:
        result = "it's not the time"
    return result


print(balancer(current_round, max_round, events[0], events[1]))
