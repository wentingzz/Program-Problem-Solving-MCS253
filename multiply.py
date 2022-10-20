import sys
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def convertStringToLinkedList(s):
    res = None
    for c in s:
        res = Node(int(c), res)
    return res

def convertListToString(positive, l):
    tmp, res = l, ""
    while tmp:
        res = str(tmp.val) + res
        tmp = tmp.next
    if not positive:
        res = "-" + res
    return res
    
def multiplyLists(l1, l2):
    cur1, cur2, res = l1, l2, Node()
    cur = res
    
    def multiply(m, l):
        tmpL, carry, tmpR = l, 0, cur
        while tmpL:
             carry, tmpR.val = divmod(tmpL.val * m + carry + tmpR.val, 10)
             if not tmpR.next and (tmpL.next or carry > 0):
                 tmpR.next = Node()
             tmpL, tmpR = tmpL.next, tmpR.next
        if carry > 0:
            tmpR.val += carry

    while cur2:
        multiply(cur2.val, l1)
        cur2 = cur2.next
        cur = cur.next
    return res


def handleNegative(boolean, s):
    if s[0] == "-":
        return (not boolean, s[1:])
    return (boolean, s)
        
n1, n2 = sys.argv[1], sys.argv[2]
if "0" in [n1, n2]:
    print("0")
else:
    positive = True
    positive, n1 = handleNegative(positive, n1)
    positive, n2 = handleNegative(positive, n2)
    list1, list2 = convertStringToLinkedList(n1), convertStringToLinkedList(n2)
    print(convertListToString(positive, multiplyLists(list1, list2)))