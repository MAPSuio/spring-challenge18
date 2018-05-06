# Converts a Basic BASIC program to a BASIC program which can be ran
# at www.quitebasic.com. The only things that need to be changed are
# the JUMP and CONDJUMP statements.

from sys import stdin

lineno = 1
for line in map(lambda l: l.rstrip(), stdin):
    tokens = line.split()
    keyword = tokens[0]
    
    if keyword == "JUMP":
        goto_lineno = tokens[1]
        out_line = "GOTO " + goto_lineno
    elif keyword == "CONDJUMP":
        goto_lineno = tokens[1]
        cond = " ".join(tokens[2:])
        out_line = "IF " + cond + " THEN GOTO " + goto_lineno
    else:
        out_line = line # no change

    # A line number needs to be included in a BASIC statement
    print(lineno, out_line)
    lineno += 1
