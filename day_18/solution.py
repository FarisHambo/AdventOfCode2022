lines = open('/Users/farishambo/Desktop/advent_git/AdventOfCode2022/day_18/test.txt').readlines()
lines = [line.strip('\n') for line in lines]

filled_pockets = set()
for line in lines:
    x, y, z = [int(x) for x in line.split(',')]
    filled_pockets.add((x,y,z))

deltas = [
    (1,0,0),
    (-1,0,0),
    (0,1,0),
    (0,-1,0),
    (0,0,1),
    (0,0,-1),
]
count_1 = 0
for line in lines:
    x, y, z = [int(x) for x in line.split(',')]
    for dx, dy, dz in deltas:
        if (x+dx, y+dy, z+dz) not in filled_pockets:
            count_1 += 1
print("part 1", count_1)

def is_pocket_bfs(start, known_lava, known_outside, maxdepth = 10):
    visited = set()
    queue = [(0,start)]
    while queue:
        cur_depth, square = queue.pop(0)
        if square in visited: 
            continue
        if square in known_lava:
            continue
        if cur_depth > maxdepth or (square in known_outside):
            while queue:
                _, pos = queue.pop()
                visited.add(pos)
            return False, visited
        visited.add(square)
        for dx, dy, dz in deltas:
            new_curr = (cube[0]+dx, cube[1]+dy, cube[2]+dz)
            queue.append((cur_depth + 1, new_curr))
    return True, visited

known_outside = set()
for line in lines:
    x, y, z =  [int(x) for x in line.split(',')]
    for dx, dy, dz in deltas:
        newplace = (x+dx, y+dy, z+dz)
        if newplace not in filled_pockets and (newplace not in known_outside):
             if newplace in filled_pockets == False:
                is_pocket, visited =  is_pocket_bfs(newplace, filled_pockets, known_outside)                    
                if is_pocket:
                    filled_pockets.update(visited)
                else:
                    known_outside.update(visited)

count_2 = 0
for line in lines:
    x, y, z = [int(x) for x in line.split(',')]
    for dx, dy, dz in deltas:
        if (x+dx, y+dy, z+dz) not in filled_pockets:
            count_2 += 1
print("part_2", count_2)