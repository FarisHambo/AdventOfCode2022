def right_distance (row, col, matrix):
  if col == len(matrix[0])-1:
    return 0
  num = matrix[row][col]
  counter = 0
  for j in range(col+1, len(matrix)):
    if matrix[row][j] < num:
      counter += 1
    else:
      counter += 1
      break
  return counter
  
def left_distance (row, col, matrix):
  if col == 0:
    return 0
  num = matrix[row][col]
  counter = 0
  for j in range(col-1, -1, -1):
    if matrix[row][j] < num:
      counter += 1
    else:
      counter += 1
      break
  return counter

def bottom_distance (row, col, matrix):
  if row == len(matrix)-1:
    return 0
  num = matrix[row][col]
  counter = 0
  for i in range(row+1, len(matrix)):
    if matrix[i][col] < num:
      counter += 1
    else:
      counter += 1
      break
  return counter


def top_distance (row, col, matrix):
  if row == 0:
    return 0
  num = matrix[row][col]
  counter = 0
  for i in range(row-1, -1, -1):
    if matrix[i][col] < num:
      counter += 1
    else:
      counter += 1
      break
  return counter
  

def is_visible_from_all_side(row, col, matrix):
  num = matrix[row][col]
  top_visible = True
  right_visible = True
  left_visible = True
  bottom_visible = True
  for j in range(col):
    if matrix[row][j] >= num:
      left_visible =  False
  for j in range(col+1,len(matrix[0])):
    if matrix[row][j] >= num:
      right_visible = False
  for i in range(row):
    if matrix[i][col] >= num:
      top_visible = False
  for i in range(row+1,len(matrix)):
    if matrix[i][col] >= num:
      bottom_visible = False
  return top_visible or right_visible or left_visible or bottom_visible

def is_visible(row, col, matrix):
  num = matrix[row][col]
  top_visible = True
  right_visible = True
  left_visible = True
  bottom_visible = True
  #top
  top_row = 1
  while True:
    if matrix[row - top_row][col] >= num:
      top_visible = False
      break
    else:
      top_row += 1
      if row - top_row < 0:
        break
  #bottom
  bottom_row = 1
  while True:
    if matrix[row + bottom_row][col] >= num:
      bottom_visible = False
      break
    else:
      bottom_row += 1
      if row + bottom_row == len(matrix):
        break
  #left
  left_col = 1
  while True:
    if matrix[row][col-left_col] >= num:
      left_visible = False
      break
    else:
      left_col += 1
      if col-left_col < 0:
        break
  #left
  right_col = 1
  while True:
    if matrix[row][col+right_col] >= num:
      right_visible = False
      break
    else:
      right_col += 1
      if col+right_col == len(matrix):
        break
  return top_visible or right_visible or left_visible or bottom_visible


def all_rows_same_length(matrix):
  first_row = len(matrix[0])
  for row in matrix:
    if len(row) != first_row:
      return False
  return True

matrix = []
f = open("input.txt", "r")

for line in f:
  stripped_line = line.rstrip("\n")
  matrix.append(stripped_line)

f.close()
for line in matrix:
  print(line)

print(top_distance(4,3, matrix))
print(left_distance(4,3, matrix))
print(right_distance(4,3, matrix))
print(bottom_distance(4,3, matrix))

max_product = -100000000
top_i = 0
top_j = 0
for i in range(len(matrix)):
  for j in range(len(matrix)):
    print(i,j)
    a = top_distance(i,j, matrix)
    b = left_distance(i, j, matrix)
    c = right_distance(i, j, matrix)
    d = bottom_distance(i, j, matrix)
    product = a*b*c*d
    if product >= max_product:
      max_product = product
      top_i = i
      top_j = j

print()
print(max_product)
print(top_i, top_j)
"""
counter = 0
for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    if (i != 0 and i != len(matrix)-1) and( j != 0 and j != len(matrix[0])-1):
      if is_visible_from_all_side(i, j, matrix):
        counter += 1
"""

