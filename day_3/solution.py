def found_in_both(line):
  0,1,2,3, 4,5,6,7
  half = len(line)//2
  set1 = set()
  """
  print(len(line))
  print(line[:half+1])
  print(line[half+1:])
  print(len(line[:half+1]))
  print(len(line[half+1:]))
  """
  for i in range(half):
    set1.add(line[i])
  set2 = set()
  for i in range(half,len(line)):
    set2.add(line[i])
  intersect = set1.intersection(set2)
  for x in intersect:
    return x

def common_for_three(a,b,c):
  set1 = set()
  set2 = set()
  set3 = set()
  for i in range(len(a)):
    set1.add(a[i])
  for i in range(len(b)):
    set2.add(b[i])
  for i in range(len(c)):
    set3.add(c[i])
  first = set1.intersection(set2)
  second = first.intersection(set3)
  for x in second:
    return x
  

def return_value(char):
  if char >= 'a' and char <= 'z':
    return ord(char) - 96
  elif char >= 'A' and char <= 'Z':
    return ord(char) - 38


sum = 0
f = open("input_1.txt","r")
for line in f:
  line_new = line.rstrip("\n")
  char = found_in_both(line)
  sum += return_value(char)
print(sum)
f.close()

g = open("input_1.txt", "r")
second_sum = 0
counter = 0
one = ''
two = ''
three = ''
for line in g:
  line_new = line.rstrip("\n")
  if counter % 3 == 0:
    one = line_new
    counter += 1
  elif counter % 3 == 1:
    two = line_new
    counter += 1
  else:
    three = line_new
    char = common_for_three(one, two, three)
    second_sum += return_value(char)
    one = ""
    two = ""
    three = ""
    counter += 1

print(second_sum)