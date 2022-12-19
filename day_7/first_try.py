import sys
sys.setrecursionlimit(3500)
curenntly_visited = []

sum_hash_map = {}

f = open("input_real_1.txt", "r")

#saving values on each level
while True:
  a = ''
  a = f.readline()
  a.rstrip("\n")
  if a == "":
    break
  line = a.split()
  if line[0] == "$" and line[1] == "cd" and line[2] != "..":
    curenntly_visited.append(line[2])
  elif line[0] == "$" and line[1] == "cd" and line[2] == "..":
    curenntly_visited.pop()
      
  elif line[0] == "$" and line[1] == "ls":
    while True:
        newline = ''
        newline = f.readline()
        newline.rstrip("\n")
        lines_within = newline.split()
        if newline == "":
            break
        elif lines_within[0][0] >= "0" and lines_within[0][0] <= "9":
          if curenntly_visited[-1] not in sum_hash_map:
            sum_hash_map[curenntly_visited[-1]] = int(lines_within[0])
          else:
            sum_hash_map[curenntly_visited[-1]] += int(lines_within[0])
        elif lines_within[0] == "$" and lines_within[1] == "cd" and lines_within[2] != "..":
          curenntly_visited.append(lines_within[2])
          break
        elif lines_within[0] == "$" and lines_within[1] == "cd" and lines_within[2] == "..":
          curenntly_visited.pop()
f.close()


f = open("input_real_1.txt", "r")
children = dict()
visited = []
#saving values on each level
while True:
  a = ''
  a = f.readline()
  a.rstrip("\n")
  if a == "":
    break
  line = a.split()
  if line[0] == "$" and line[1] == "cd" and line[2] != "..":
    visited.append(line[2])
    if line[2] not in children:
      children[line[2]] = []
  elif line[0] == "$" and line[1] == "cd" and line[2] == "..":
    visited.pop()
      
  elif line[0] == "$" and line[1] == "ls":
    while True:
      newline = ''
      newline = f.readline()
      newline.rstrip("\n")
      lines_within = newline.split()
      if newline == "":
          break
      elif lines_within[0][0] >= "0" and lines_within[0][0] <= "9":
        pass
      elif lines_within[0] == "$" and lines_within[1] == "cd" and lines_within[2] != "..":
        visited.append(lines_within[2])
        if lines_within[2] not in children:
          children[lines_within[2]] = []  
        break
      elif lines_within[0] == "$" and lines_within[1] == "cd" and lines_within[2] == "..":
        visited.pop()
        break
      elif lines_within[0] == "dir":
        children[visited[-1]].append(lines_within[1])

print(children)
f.close()

def sum_one(key, map_to_iterate, value_map):
  key_children = map_to_iterate[key]
  if len(key_children) == 0:
    return 0
  else:
    sum = 0
    for i in range(len(key_children)):
      sum += sum_one(key_children[i], map_to_iterate, value_map) + value_map[key_children[i]]
    return sum

new_hash_map = dict()

for key in sum_hash_map:
  new_hash_map[key] = sum_hash_map[key] + sum_one(key, children, sum_hash_map)

print(new_hash_map)



sum_total = 0
for key in new_hash_map:
  if new_hash_map[key] < 100000:
    sum_total += new_hash_map[key]
print(sum_total)