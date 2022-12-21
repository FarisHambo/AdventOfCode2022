import sympy
solution_dict = {}

f = open("day_21/input.txt", "r")
for line in f:
    splitted_line = line.rstrip("\n").split(": ")
    if "0" <= splitted_line[1][0] and splitted_line[1][0] <= "9":
        solution_dict[splitted_line[0]] = int(splitted_line[1])
    else:
        solution_dict[splitted_line[0]] = splitted_line[1]
f.close()




f = open("day_21/input.txt", "r")
solution_dict_2 = {}
for line in f:
    splitted_line = line.rstrip("\n").split(": ")
    if "0" <= splitted_line[1][0] and splitted_line[1][0] <= "9":
        solution_dict_2[splitted_line[0]] = int(splitted_line[1])
    else:
        solution_dict_2[splitted_line[0]] = splitted_line[1].split()
f.close()


def prob_1(solution_dict, current_key):
    #print("working with: ", current_key)
    #a = input()
    if isinstance(solution_dict[current_key], int):
        return solution_dict[current_key]
    if "+" in solution_dict[current_key]:
        keys = solution_dict[current_key].split(" + ")
        return prob_1(solution_dict, keys[0]) + prob_1(solution_dict, keys[1])
    if "*" in solution_dict[current_key]:
        keys = solution_dict[current_key].split(" * ")
        return prob_1(solution_dict, keys[0]) * prob_1(solution_dict, keys[1])
    if "-" in solution_dict[current_key]:
        keys = solution_dict[current_key].split(" - ")
        return prob_1(solution_dict, keys[0]) - prob_1(solution_dict, keys[1])
    if "/" in solution_dict[current_key]:
        keys = solution_dict[current_key].split(" / ")
        return prob_1(solution_dict, keys[0]) / prob_1(solution_dict, keys[1])

def prob_2_part_1(solution_dict, current_key):
    """
    if current_key == "root":
        vals = solution_dict["root"].split()
        return sympy.solve(prob_2(solution_dict, vals[0])-prob_2(solution_dict, vals[1]))
    """
    if current_key == "humn":
        return sympy.symbols("x")
    if isinstance(solution_dict[current_key], int):
        return solution_dict[current_key]
    first = prob_2_part_1(solution_dict, solution_dict[current_key][0])
    second = prob_2_part_1(solution_dict, solution_dict[current_key][2])

    return sympy.parsing.sympy_parser.parse_expr(f"({first}){solution_dict[current_key][1]}({second})")


def prob_2_part_2(solution_dict):
    return sympy.solve_linear(prob_2_part_1(solution_dict, solution_dict["root"][0]),\
                              prob_2_part_1(solution_dict, solution_dict["root"][2])
        )[1]

print(prob_1(solution_dict,"root"))
print(prob_2_part_2(solution_dict_2))