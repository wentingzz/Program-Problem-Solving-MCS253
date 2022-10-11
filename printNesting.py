import sys


def printLevel(lvl):
    for k in lvl.keys():
        if lvl[k] != "":
            print("|" + " " * 2 * k + lvl[k])


def printNesting(s):
    lookup = {"{": "}", "(": ")", "[": "]"}
    stack, level, word = [], {0: ""}, False

    def updateLevel(char):
        if word:
            char = " " + char
        if len(stack) in level:
            level[len(stack)] += char
        else:
            level[len(stack)] = char

    for c in s:
        if c in lookup:
            stack.append(lookup[c])
            word = True
        elif c in [")", "}", "]"]:
            if stack and stack[-1] == c:
                word = True
                stack.pop()
            else:
                print("|mismatched groups!")
                return
        else:
            updateLevel(c)
            word = False
    printLevel(level)


if len(sys.argv) > 1:
    printNesting(sys.argv[1])