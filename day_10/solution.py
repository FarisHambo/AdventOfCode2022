def prob_1():
  commands = []
  f = open("input.txt", "r")
  for line in f:
    new_line = line.rstrip("\n")
    row = new_line.split()
    commands.append(row)
  f.close()

  X = 1
  counter = 0
  sum = 0
  for command in commands:
    if command[0] == "noop":
      counter += 1
      if counter == 20 or counter == 60 or counter == 100 or counter == 140 or counter == 180 or counter == 220:
        print (X)
        sum += X*counter
    else:
      counter += 1
      if counter == 20 or counter == 60 or counter == 100 or counter == 140 or counter == 180 or counter == 220:
        print (X)
        sum += X*counter
      counter += 1
      if counter == 20 or counter == 60 or counter == 100 or counter == 140 or counter == 180 or counter == 220:
        print (X)
        sum += X*counter
      X += int(command[1])
  return sum

def prob_2():
  matrix = [["?" for _ in range(40)] for _ in range(6)]
  commands = []
  f = open("input.txt", "r")
  for line in f:
    new_line = line.rstrip("\n")
    row = new_line.split()
    commands.append(row)
  f.close()

  X = 1
  counter = -1
  for command in commands:
    if command[0] == "noop":
      counter += 1
      print(counter//40, counter%40)
      matrix[counter//40][counter%40] = ("#" if abs(X-(counter%40))<= 1 else ".")
    else: 
      counter += 1
      print(counter//40, counter%40)
      matrix[counter//40][counter%40] = ("#" if abs(X-(counter%40))<= 1 else ".")
      
      counter += 1
      print(counter//40, counter%40)
      matrix[counter//40][counter%40] = ("#" if abs(X-(counter%40))<= 1 else ".")
      X += int(command[1])
  return matrix

print(prob_1())
matrix = prob_2()
for line in matrix:
  for char in line:
    print(char,end=" ")
  print()
print()