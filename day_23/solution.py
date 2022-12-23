import itertools

with open("day_23/input.txt", 'r') as input_file:
    input = input_file.read()


def prob_1():
    places_to_move = [
        ((-1, 0), (-1, 1), (-1, -1), (-1, 0)),
        ((1, 0), (1, 1), (1, -1), (1, 0)),
        ((0, -1), (-1, -1), (1, -1), (0, -1)),
        ((0, 1), (-1, 1), (1, 1), (0, 1))
    ]

    grid = dict()
    initial = input.splitlines()
    sy, sx = len(initial), len(initial[0])
    elves = set()
    elf = 1
    for y in range(0, sy):
        for x in range(0, sx):
            if initial[y][x] == '#':
                grid[(y, x)] = 1
                elves.add((y, x))
                elf += 1
            else:
                grid[(y, x)] = 0

    for _ in range(10):
        propositions = dict()
        ps = dict()
        for (y, x) in elves:
            if {(y + a, x + b) for (a, b) in set(itertools.product([-1, 0, 1], [-1, 0, 1])) if
                (y + a, x + b) in elves} == {(y, x)}:
                continue
            for (p1, p2, p3, t) in places_to_move:
                if not any([(y + p[0], x + p[1]) in elves for p in [p1, p2, p3]]):
                    target_position = (y + t[0], x + t[1])
                    propositions[(y, x)] = target_position
                    ps[target_position] = 1 + ps.get(target_position, 0)
                    break

        places_to_move = places_to_move[1:] + [places_to_move[0]]
        for ((y, x), target_position) in propositions.items():
            if ps.get(target_position, 0) == 1:
                grid[y, x] = 0
                elves.discard((y, x))

        for (_, target_position) in propositions.items():
            if ps.get(target_position, 0) == 1:
                grid[target_position] = 1
                elves.add(target_position)

    min_x, max_x = min(x for (y, x) in elves), max(x for (y, x) in elves)
    min_y, max_y = min(y for (y, x) in elves), max(y for (y, x) in elves)
    area = (max_x - min_x + 1) * (max_y - min_y + 1)
    return area - len(elves)


def prob_2():
    places_to_move = [
        ((-1, 0), (-1, 1), (-1, -1), (-1, 0)),
        ((1, 0), (1, 1), (1, -1), (1, 0)),
        ((0, -1), (-1, -1), (1, -1), (0, -1)),
        ((0, 1), (-1, 1), (1, 1), (0, 1))
    ]

    initial = input.splitlines()
    sy, sx = len(initial), len(initial[0])
    elves = set()
    for y in range(0, sy):
        for x in range(0, sx):
            if initial[y][x] == '#':
                elves.add((y, x))

    i = 1
    while True:
        propositions = dict()
        ps = dict()
        elves_prev = elves.copy()
        for (y, x) in elves:
            if {(y + a, x + b) for (a, b) in set(itertools.product([-1, 0, 1], [-1, 0, 1])) if
                (y + a, x + b) in elves} == {(y, x)}:
                continue
            for (p1, p2, p3, t) in places_to_move:
                if not any([(y + p[0], x + p[1]) in elves for p in [p1, p2, p3]]):
                    target_position = (y + t[0], x + t[1])
                    propositions[(y, x)] = target_position
                    ps[target_position] = 1 + ps.get(target_position, 0)
                    break

        places_to_move = places_to_move[1:] + [places_to_move[0]]
        for ((y, x), target_position) in propositions.items():
            if ps.get(target_position, 0) == 1:
                elves.discard((y, x))

        for (_, target_position) in propositions.items():
            if ps.get(target_position, 0) == 1:
                elves.add(target_position)

        if elves == elves_prev:
            return i
        i += 1


print(prob_1())
print(prob_2())