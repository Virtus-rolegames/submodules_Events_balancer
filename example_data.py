import random
from typing import List


class Event:

    def __init__(self, id: int, eco: int = 0, soc: int = 0, arm: int = 0, rel: int = 0):
        self.id = id
        self.eco = eco
        self.soc = soc
        self.arm = arm
        self.rel = rel
        self.bal = [eco, soc, arm, rel]

    @staticmethod
    def gen_possible():
        possible_events = []
        n = 0
        for i in range(-4, 5):
            for j in range(-4, 5):
                buf = [0, 0, i, j]
                a = random.choice(buf)
                buf.remove(a)
                b = random.choice(buf)
                buf.remove(b)
                c = random.choice(buf)
                buf.remove(c)
                d = random.choice(buf)
                buf.remove(d)
                possible_events.append(Event(eco=a, soc=b, arm=b, rel=d, id=n))
                n += 1
        print("gen success")
        for i in possible_events: print(f"{i.id} | {i.bal}")
        return possible_events


def gen_use_some(possible: List[Event], current_round: int):
    used: List[Event] = []
    print(possible)
    for i in range(current_round):
        buf = random.choice(possible)
        possible.remove(buf)
        used.append(buf)
    print(f"use gen success\n{used}")
    return [possible, used]
