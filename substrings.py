import sys
def buildDictionary(strings):
    dic = {}
    for s in strings:
        if len(s) not in dic:
            dic[len(s)] = [s]
        else:
            dic[len(s)].append(s)
    return dic
def searchParentString(values, subString):
    res, seenSelf = [], False
    for v in values:
        if v == subString:
            if seenSelf:
                res.append(v)
            else:
                seenSelf = True
        elif v.find(subString) > -1:
            res.append(v)
    return res

def printAllParentStrings(strings):
    dic = buildDictionary(strings)
    for s in strings:
        res  = []
        for l,values in dic.items():
            if l >= len(s):
                res += searchParentString(values, s)
        print( s, ":" , res)


with open(sys.argv[1], "r") as file:
    line = file.readline()
    printAllParentStrings(line.split(","))