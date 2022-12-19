def are_adjecent(Hi, Hj, Ti, Tj):
  if abs(Hi-Ti) <=1 and abs(Hj-Tj) <= 1:
    return True
  return False

def where_to_move(Hi, Hj, Ti, Tj):
  
  if Hi == Ti and Hj > Tj:
    return (Ti, Tj+1)
  if Hi == Ti and Hj < Tj:
    return (Ti, Tj-1)

  if Hj == Tj and Hi > Ti:
    return (Ti+1, Tj)
  if Hj == Tj and Hi < Ti:
    return (Ti-1, Tj)

  #up_right
  if Ti > Hi and Hj > Tj:
    return (Ti-1, Tj+1)
  #down_right
  if Ti < Hi and Hj > Tj:
    return (Ti+1, Tj+1)
  #up_left
  if Ti > Hi and Hj < Tj:
    return (Ti-1, Tj-1)
  #down_left
  if Ti < Hi and Hj < Tj:
    return (Ti+1, Tj-1)
    
rows = 10000
cols = 10000

visited_by_tail = set()

head_i = rows - 1
head_j = 0

tail_i = rows - 1
tail_j = 0

for i in range(rows):
  for j in range(cols):
    if i == head_i and j == head_j:
      print("H", end= " ")
    elif i == tail_i and j == tail_j:
      print("T", end= " ")
    elif i == tail_i and j == tail_j:
      print("-", end= " ")
    

visited_by_tail.add((tail_i, tail_j))

commands = []

f = open("input.txt", "r")
for line in f:
  new_line = line.rstrip("\n")
  command = new_line.split()
  command[1] = int(command[1])
  commands.append(command)

print(commands)
for command in commands:
  for _ in range(command[1]):
    if command[0] == "R":
      head_j += 1
    elif command[0] == "L":
      head_j -= 1
    elif command[0] == "U":
      head_i -= 1
    elif command[0] == "D":
      head_i += 1
      
    if are_adjecent(head_i, head_j, tail_i, tail_j) == False:
      res = where_to_move(head_i, head_j, tail_i, tail_j)
      tail_i = res[0]
      tail_j = res[1]
      visited_by_tail.add((tail_i, tail_j))

print(len(visited_by_tail))
        