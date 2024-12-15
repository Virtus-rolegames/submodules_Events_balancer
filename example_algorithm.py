import math
from example_data import Event, gen_use_some

current_round = 4
max_round = 7


possibles = Event.gen_possible()
events = gen_use_some(possibles, current_round)

def calc_bal(used):
    bal = [0,0,0,0]
    for event in used:
        bal[0] += event.eco
        bal[1] += event.arm
        bal[2] += event.eco
        bal[3] += event.eco


def balancer(current, max, possible, used):
    target_bal = [0,0,0,0]
    if current >= math.ceil(max/2):






print(balancer(current_round,max_round,events[0],events[1]))