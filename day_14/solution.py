def generate_cave(path):
  cave = [["." for _ in range(1000)] for _ in range(1000)]
  f = open(path, "r")
  for line in f:
    new_line = line.rstrip("\n")
    new_line = new_line.replace(" ", "")
    partial_path = new_line.split("->")
    full_path = []
    for path in partial_path:
      new_path = path.split(",")
      full_path.append([int(new_path[1]), int(new_path[0])])
    for i in range(len(full_path) - 1):
      if full_path[i][0] == full_path[i + 1][0]:
        for ind in range(min(full_path[i][1], full_path[i + 1][1]),
                         max(full_path[i][1], full_path[i + 1][1]) + 1):
          cave[full_path[i][0]][ind] = "#"
      if full_path[i][1] == full_path[i + 1][1]:
        for ind in range(min(full_path[i][0], full_path[i + 1][0]),
                         max(full_path[i][0], full_path[i + 1][0]) + 1):
          cave[ind][full_path[i][1]] = "#"

  max_i = 0
  for i in range(len(cave)):
    if "#" in cave[i]:
      max_i = i
  print(max_i)

  for j in range(len(cave[max_i + 2])):
    cave[max_i + 2][j] = "#"

  return cave


matrix = generate_cave("test.txt")
for i in range(12):
  for j in range(491, 507):
    print(matrix[i][j], end=" ")
  print()


def simulate_sand_fall_1(path):
  cave = generate_cave(path)
  num_units_at_rest = 0

  while True:
    i = 0
    j = 500
    while True:
      if i == 999:
        break
      if cave[i + 1][j] == ".":
        i += 1
        if i == 999:
          break
      elif j > 0 and cave[i + 1][j - 1] == ".":
        i += 1
        j -= 1
        if i == 999:
          break
      elif j < 1000 and cave[i + 1][j + 1] == ".":
        i += 1
        j += 1
        if i == 999:
          break
      else:
        cave[i][j] = "O"
        num_units_at_rest += 1
        break
    if i == 999:
      return num_units_at_rest


def simulate_sand_fall_2(path):
  cave = generate_cave(path)
  num_units_at_rest = 0

  while True:
    i = 0
    j = 500
    is_source_blocked = False
    while True:

      if cave[i + 1][j] == ".":
        i += 1
      elif j > 0 and cave[i + 1][j - 1] == ".":
        i += 1
        j -= 1
      elif j < 1000 and cave[i + 1][j + 1] == ".":
        i += 1
        j += 1
      else:
        cave[i][j] = "O"
        num_units_at_rest += 1
        if i == 0 and j == 500:
          is_source_blocked = True
        break
    if is_source_blocked == True:
      for i in range(12):
        for j in range(480, 515):
          print(cave[i][j], end=" ")
        print()
      return num_units_at_rest


print(simulate_sand_fall_2("input.txt"))
