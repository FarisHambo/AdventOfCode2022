def get_crates(input):
  lines = input.split("\n")
  full_matrix = []
  total_num_of_chars = (len(lines[0])//4) + 1
  for i in range(total_num_of_chars):
    full_matrix.append([])

  for j in range(len(lines[0])):
    for i in range(len(lines)-1,-1,-1):
      if lines[i][j] != " " and j%4==1:
        full_matrix[int(j//4)].append(lines[i][j])
  return full_matrix

def read_command_1(command, matrix):
  #move 2 from 4 to 2
  commands = command.split(" ")
  
  how_many = int(commands[1])
  from_where = int(commands[3])-1
  to_where = int(commands[5])-1
  
  what_to_move = matrix[from_where][-how_many:]
  what_to_move.reverse()
  
  for _ in range(how_many):
    matrix[from_where].pop()
    
  for i in range(len(what_to_move)):
    matrix[to_where].append(what_to_move[i])
    
  return matrix

def read_command_2(command, matrix):
  #move 2 from 4 to 2
  commands = command.split(" ")
  
  how_many = int(commands[1])
  from_where = int(commands[3])-1
  to_where = int(commands[5])-1
  
  what_to_move = matrix[from_where][-how_many:]
  
  for _ in range(how_many):
    matrix[from_where].pop()
    
  for i in range(len(what_to_move)):
    matrix[to_where].append(what_to_move[i])
    
  return matrix

f = open("crates.txt","r")
a = f.read()
matrix = get_crates(a)
f.close()

for row in matrix:
  print(row)
print()
print()
g = open("commands.txt","r")
for line in g:
  filtered_line = line.rstrip("\n")
  matrix = read_command_2(filtered_line, matrix)
  for row in matrix:
    print(row)
  print()
  print()

for i in range(len(matrix)):
  print(matrix[i][-1],end="")