def convert_string_to_number(s):
    decimal = 0
    for i in range(len(s)-1,-1,-1):
        curr_pow = len(s) - 1 - i
        if s[i] == "=":
            decimal = decimal -(2*(5**curr_pow))
        elif s[i] == "-":
            decimal = decimal -(5**curr_pow)
        else:
            decimal = decimal + int(s[i])*(5**curr_pow)
    return decimal

def snafu(dec):
    out = []
    while dec:
        dec, rem = divmod(dec,5)
        if rem in (0,1,2):
            out.append(str(rem))
        if rem == 3:
            out.append("=")
            dec += 1
        if rem == 4:
            out.append('-')
            dec += 1
    out.reverse()
    output = "".join(out)
    return output

f = open("day_25/input.txt", "r")
sum = 0
for line in f:
    new_line = line.rstrip("\n")
    sum += convert_string_to_number(new_line)
print(snafu(sum))
