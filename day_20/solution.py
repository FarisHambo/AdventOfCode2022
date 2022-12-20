import os
path = os.getcwd()
print(path)
def mixing(iters, multiplier):
    f = open("input.txt", "r")
    input = f.read().split("\n")
    input = [int(x) for x in input]
    input = [x*multiplier for x in input]
    list_of_index = list(range(len(input)))
    for i in range(iters):
        print(i)
        for ind in range(len(input)):
            index = list_of_index.index(ind)
            targeted_value = input.pop(index)
            next_ind = (index + targeted_value) % len(input)
            if targeted_value != 0 and next_ind == 0:
                next_ind = len(input)
            elif next_ind == len(input):
                next_ind = 0
            input.insert(next_ind, targeted_value)
            list_of_index.pop(index)
            list_of_index.insert(next_ind, ind)
    
    index_zero = input.index(0)
    return input[(index_zero + 1000) % len(input)] + input[(index_zero + 2000) % len(input)] + input[(index_zero + 3000) % len(input)]

print("part 1: ", mixing(1, 1))
print("part 2: ", mixing(10, 811589153))