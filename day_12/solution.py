
def possible_neighbours(matrix, curr_pos):
  i = curr_pos[0]
  j = curr_pos[1]
  if i == 0 and j == 0:
    list_to_return = []

    if matrix[0][1] - matrix[i][j] <= 1:
      list_to_return.append((0,1))

    if matrix[1][0] - matrix[i][j] <= 1:
      list_to_return.append((1,0))

    return list_to_return

  elif i == 0 and j == len(matrix[0])-1:

    list_to_return = []
    if matrix[0][len(matrix[0])-2] - matrix[i][j] <= 1:
      list_to_return.append((0,len(matrix[0])-2))

    if matrix[1][len(matrix[0])-1] - matrix[i][j] <= 1:
      list_to_return.append((1,len(matrix[0])-1))

    return list_to_return

  elif i == len(matrix) - 1 and j == 0:
    list_to_return = []

    if matrix[len(matrix) - 2][0] - matrix[i][j] <= 1:
      list_to_return.append((len(matrix) - 2,0))

    if matrix[len(matrix) - 1][1] - matrix[i][j] <= 1:
      list_to_return.append((len(matrix) - 1, 1))

    return list_to_return

  elif i == len(matrix) - 1 and j == len(matrix[0]) - 1:
    
    list_to_return = []
    
    if matrix[len(matrix) - 1][len(matrix[0]) - 2] - matrix[i][j] <= 1:
      list_to_return.append((len(matrix) - 1, len(matrix[0]) - 1))
    
    if matrix[len(matrix) - 2][len(matrix[0]) - 1] - matrix[i][j] <= 1:
      list_to_return.append((len(matrix) - 2, len(matrix[0]) - 1))
    
    return list_to_return
  
  elif i == 0:
    list_to_return = []
    
    if matrix[i][j-1] - matrix[i][j] <= 1:
      list_to_return.append((i,j-1))
    
    if matrix[i][j+1] - matrix[i][j] <= 1:
      list_to_return.append((i,j+1))
    
    if matrix[i+1][j] - matrix[i][j] <= 1:
      list_to_return.append((i+1,j))
    
    return list_to_return
  
  elif i == len(matrix)-1:
    list_to_return = []
    
    if matrix[i][j-1] - matrix[i][j] <= 1:
      list_to_return.append((i,j-1))
    
    if matrix[i][j+1] - matrix[i][j] <= 1:
      list_to_return.append((i,j+1))
    
    if matrix[i-1][j] - matrix[i][j] <= 1:
      list_to_return.append((i-1,j))
    
    return list_to_return
  
  elif j == 0:
    list_to_return = []
    
    if matrix[i+1][j] - matrix[i][j] <= 1:
      list_to_return.append((i+1,j))
    
    if matrix[i-1][j] - matrix[i][j] <= 1:
      list_to_return.append((i-1,j))
    
    if matrix[i][j+1] - matrix[i][j] <= 1:
      list_to_return.append((i,j+1))
    
    return list_to_return
  
  elif j == len(matrix[0])-1:
    list_to_return = []
    
    if matrix[i+1][j] - matrix[i][j] <= 1:
      list_to_return.append((i+1,j))
    
    if matrix[i-1][j] - matrix[i][j] <= 1:
      list_to_return.append((i-1,j))
    
    if matrix[i][j-1] - matrix[i][j] <= 1:
      list_to_return.append((i,j-1))
    
    return list_to_return
  
  else:
    
    list_to_return = []
   
    if matrix[i+1][j] - matrix[i][j] <= 1:
      list_to_return.append((i+1,j))
   
    if matrix[i-1][j] - matrix[i][j] <= 1:
      list_to_return.append((i-1,j))
   
    if matrix[i][j-1] - matrix[i][j] <= 1:
      list_to_return.append((i,j-1))
   
    if matrix[i][j+1] - matrix[i][j] <= 1:
      list_to_return.append((i,j+1))
   
    return list_to_return
  
      
def prob_1():  
  f = open("input.txt", "r")
  matrix = []
  for line in f:
    new_line = line.rstrip("\n")
    print(new_line)
    matrix.append(new_line)
  f.close()
  num_matrix = []
  for i in range(len(matrix)):
    curr_row = []
    
    for j in range(len(matrix[0])):
      
      if matrix[i][j] >= 'a' and matrix[i][j] <= 'z':
        curr_row.append(ord(matrix[i][j])-96)
      
      elif matrix[i][j] == "S":
        curr_row.append(0)
      
      else:
        curr_row.append(27)
    
    num_matrix.append(curr_row)
  matrix = num_matrix
  
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      
      if matrix[i][j] == 0:
        start = (i,j) 
      
      elif matrix[i][j] == 27:
        end = (i,j)
  queue = [(start, 0)]
  
  visited = set()

  while len(queue) != 0:
      curr_poss, num_of_stemps = queue.pop(0)
    
      if curr_poss in visited:
          continue
  
      visited.add(curr_poss)
  
      if curr_poss == end:
          return num_of_stemps
  
      neighbours = possible_neighbours(matrix, curr_poss)
      for neighbour in neighbours:
          queue.append((neighbour, num_of_stemps + 1))
  
  return -1


      
def prob_2():  
  f = open("input.txt", "r")
  matrix = []
  for line in f:
    new_line = line.rstrip("\n")
    print(new_line)
    matrix.append(new_line)
  f.close()
  num_matrix = []
  for i in range(len(matrix)):
    curr_row = []
    for j in range(len(matrix[0])):
      if matrix[i][j] >= 'a' and matrix[i][j] <= 'z':
        curr_row.append(ord(matrix[i][j])-96)
      elif matrix[i][j] == "S":
        curr_row.append(1)
      else:
        curr_row.append(27)
    num_matrix.append(curr_row)
  matrix = num_matrix
  print()

  list_of_starts = []
  min_length = len(matrix)*len(matrix[0])
  
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == 1:
        list_of_starts.append((i,j)) 
      elif matrix[i][j] == 27:
        end = (i,j)

  for start in list_of_starts:
    queue = [(start, 0)]
    
    visited = set()
  
    while len(queue) != 0:
        curr, num_of_stemps = queue.pop(0)
      
        if curr in visited:
            continue
    
        visited.add(curr)
    
        if curr == end:
            if num_of_stemps < min_length:
              min_length = num_of_stemps
              break
    
        neighbours = possible_neighbours(matrix, curr)
        for neighbour in neighbours:
            queue.append((neighbour, num_of_stemps + 1))
    
  return min_length


print(prob_2())