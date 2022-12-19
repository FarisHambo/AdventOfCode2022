def place_1(line):
  for i in range(len(line)-3):
    temp_set = set()
    for j in range(i,i+4):
      temp_set.add(line[j])
    if len(temp_set) == 4:
      return i+4

def place_2(line):
  for i in range(len(line)-14):
    temp_set = set()
    for j in range(i,i+14):
      temp_set.add(line[j])
    if len(temp_set) == 14:
      return i+14

f = open("input.txt", "r")
line = f.read()
line = line.rstrip("\n")
print(place_2(line))