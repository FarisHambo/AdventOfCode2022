
def second_value(value):
  if value == 'X':
    return 1
  elif value == 'Y':
    return 2
  else:
    return 3

def outcome(value_1, value_2):
  if (value_1 == 'A' and value_2 == 'X') or(value_1 == 'B' and value_2 == 'Y') or(value_1 == 'C' and value_2 == 'Z'):
    return 3
  elif (value_1 == 'A' and value_2 == "Y") or  (value_1 == 'B' and value_2 == "Z") or (value_1 == 'C' and value_2 == 'X'):
    return 6
  else:
    return 0
"""
A for Rock, B for Paper, and C for Scissors
X for Rock, Y for Paper, and Z for Scissors
X means you lose, Y means you draw, and Z means you win.
"""
def what_needs_to_be_played(value_1, value_2):
  if value_1 == "A" and value_2 == "X":
    return "Z"
  elif value_1 == "A" and value_2 == "Y":
    return "X"
  elif value_1 == "A" and value_2 == "Z":
    return "Y"
  if value_1 == "B" and value_2 == "X":
    return "X"
  elif value_1 == "B" and value_2 == "Y":
    return "Y"
  elif value_1 == "B" and value_2 == "Z":
    return "Z"
  if value_1 == "C" and value_2 == "X":
    return "Y"
  elif value_1 == "C" and value_2 == "Y":
    return "Z"
  elif value_1 == "C" and value_2 == "Z":
    return "X"
  
    
f = open("input_2.txt", "r")
sum = 0

matrix_of_results = []

for line in f:
  line = line.rstrip("\n")
  items = line.split()
  items[1] = what_needs_to_be_played(items[0], items[1])
  matrix_of_results.append(items)

print(matrix_of_results)

for line in matrix_of_results:
  sum += second_value(line[1]) + outcome(line[0],line[1])
print(sum)