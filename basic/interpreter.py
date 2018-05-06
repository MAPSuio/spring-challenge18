import sys, re

var_values = {}
program = [line.rstrip() for line in sys.stdin]

# exp is list of tokens
def basic_eval(exp):
    return eval("".join([str(var_values[t]) if t in var_values else t for t in exp]))

lineno = 1
while True:
    line = program[lineno - 1]
    tokens = re.findall(r"[\w]+|[^\s\w]", line)
    keyword = tokens[0]

    if keyword == "LET":
        var_name = tokens[1]
        exp = tokens[3:]
        var_values[var_name] = basic_eval(exp)

    elif keyword == "JUMP":
        lineno = int(tokens[1])
        continue

    elif keyword == "CONDJUMP":
        exp = tokens[2:]
        if basic_eval(exp):
            lineno = int(tokens[1])
            continue

    elif keyword == "PRINT":
        var_name = tokens[1]
        print(var_values[var_name])

    elif keyword == "END":
        break

    lineno += 1
