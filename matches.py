def getFrequencyList(w, s):
    frequencyW = [0] * 26
    frequencyS = [0] * 26

    for i in range(len(w)):
        frequencyW[ord(w[i].lower()) - ord('a')] += 1
        frequencyS[ord(s[i].lower()) - ord('a')] += 1
        return (frequencyW, frequencyS)


def getInitialMatches(f1, f2):
    matches = 0

    for i in range(26):
        if f1[i] == f2[i]:
            matches += 1
    return matches


def anagrams(w, s):
    frequencyW, frequencyS = getFrequencyList(w, s)
    matches = getInitialMatches(frequencyW, frequencyS)

    res = []
    start = 0
    for end in range(len(w), len(s)):
        if matches == 26:
            res.append(start)


        def moveRightAndUpdateFrequencyList():
            global start, matches
            frequencyS[start] -= 1
            frequencyS[end] += 1
            if frequencyW[start] + 1 == frequencyS[start]:
                matches -= 1
            if frequencyW[end] == frequencyS[end]:
                matches += 1
            start += 1
        moveRightAndUpdateFrequencyList()
    return res


def matches(needle, text):
    res = []
    if len(needle) > len(text):
        return res
    for i in range(len(text) - len(needle)):
        if text[i: i + len(needle)] == needle:
            res.append(i)
    return res
