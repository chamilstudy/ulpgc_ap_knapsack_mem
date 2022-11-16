from collections import namedtuple
from solve       import *

def test():
    Item = namedtuple("Item", ['index', 'value', 'weight'])

    first_line = input().split() 	# N, Capacity
    N          = int(first_line[0])
    capacity   = int(first_line[1])

    items = []
    for i in range(1, N+1):
        parts = input().split()
        items.append(Item(i, int(parts[0]), int(parts[1])))
    
    value = solve_memoization(items, capacity)
    print(value)

def test2():
    Item = namedtuple("Item", ['index', 'value', 'weight'])

    capacity   = 10

    items = []
    items.append(Item(0, 45, 5))
    items.append(Item(0, 48, 8))
    items.append(Item(0, 35, 3))
    
    value = solve_memoization(items, capacity)
    print(value)

test2()