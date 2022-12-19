def get_values(line):
  ranges = line.split(',')
  full_matrix = []
  for range in ranges:
    row = range.split("-")
    row[0] = int(row[0])
    row[1] = int(row[1])
    full_matrix.append(row)
  return full_matrix

def has_overlap(s1, e1, s2, e2):
  if s1 >= s2 and s1<=e2:
    return True
  elif e1 >= s2 and e1<=e2:
    return True
  elif s2 >= s1 and s2<=e1:
    return True
  elif e2 >= s1 and e2<=e1:
    return True
  else:
    return False

def part_one():
  counter = 0
  f = open("input.txt", "r")
  for line in f:
    fine_line = line.rstrip('\n')
    curr_line = get_values(fine_line)
    if curr_line[0][0] >= curr_line[1][0] and curr_line[0][1] <= curr_line[1][1]:
      counter += 1
    elif curr_line[1][0] >= curr_line[0][0] and curr_line[1][1] <= curr_line[0][1]:
      counter += 1
  f.close()
  return counter

def part_two():
  counter = 0
  f = open("input.txt", "r")
  for line in f:
    fine_line = line.rstrip('\n')
    curr_line = get_values(fine_line)
    if has_overlap(curr_line[0][0],curr_line[0][1],curr_line[1][0],curr_line[1][1]):
      counter += 1
  f.close()
  return counter


print(part_one())
print(part_two())
