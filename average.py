import sys

with open(sys.argv[1], "r") as file:
    count, total = 0, 0

    def noOverflowOnAddition(n1, n2):
        if sys.float_info.max - n1 < n2:
            print("The input causes an overflow")
            return False
        else:
            return True

    def isValid(string):
        try:
            tmp = float(string)
        except:
            print("The input file contains non-numeric character")
            return False

        return noOverflowOnAddition(total, tmp)

    def addNumber(string):
        if isValid(string):
            global total, count
            total += float(string)
            count += 1
        else:
            exit(1)

    line = file.readline()
    while line:
        addNumber(line)
        line = file.readline()
    if count != 0:
        print(f"The average of the {count} numbers in file \"{sys.argv[1]}\" is {round(total / count, 1)}")
    else:
        print(f"The average of the 0 numbers in file \"{sys.argv[1]}\" is 0")
