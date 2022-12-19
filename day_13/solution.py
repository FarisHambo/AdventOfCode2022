import ast


def areInOrder(left, right):
  for i in range(max(len(left), len(right))):
    if i >= len(left):
      return True
    if i >= len(right):
      return False

    l = left[i]
    r = right[i]

    if type(l) == type(r) == int:
      if r == l:
        continue
      if r < l:
        return False
      if l < r:
        return True

    if type(l) == type(r) == list:
      inOrder = areInOrder(l, r)
      if inOrder is not None:
        return inOrder

    if type(l) != type(r):
      if type(r) == int:
        r = [r]
      if type(l) == int:
        l = [l]
      inOrder = areInOrder(l, r)
      if inOrder is not None:
        return inOrder

  return None


def compare(l, r):
  x = areInOrder(l, r)
  if x:
    return -1
  else:
    return 1


def prob_1(path):
  f = open(path, "r")
  counter = 0
  matrix = []
  for line in f:
    new_line = line.rstrip("\n")
    if new_line != "":
      new_line = ast.literal_eval(new_line)
      matrix.append(new_line)
  for i in range(0, len(matrix), 2):
    left = matrix[i]
    right = matrix[i + 1]
    if areInOrder(left, right):
      counter += i // 2 + 1

  return counter


def prob_2(path):
  f = open(path, "r")
  elems = []
  elems += [[[2]]]
  elems += [[[6]]]

  for line in f:
    new_line = line.rstrip("\n")
    if new_line != "":
      new_line = ast.literal_eval(new_line)
      elems += [new_line]

  from functools import cmp_to_key
  ordered = sorted(elems, key=cmp_to_key(compare))
  for line in ordered:
    print(line)
  return (ordered.index([[2]]) + 1) * (ordered.index([[6]]) + 1)


print(prob_1("input.txt"))
print(prob_2("input.txt"))
