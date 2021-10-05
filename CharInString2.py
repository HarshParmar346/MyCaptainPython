def charInString(s):
    Dict = {}
    i = 0
    ch = 'A'
    while i < 26:
        Dict[ch] = 0
        ch = chr(ord(ch) + 1)
        i = i + 1
    ch = 'A'
    i = 0
    while i < 26:
        j = 0
        while j < len(s):
            if ch == s[j].upper():
                Dict[ch] = Dict[ch] + 1
            j = j + 1
        i = i + 1
        ch = chr(ord(ch) + 1)
    ch = 'A'
    i = 0
    count = 0
    while i < 26:
        if Dict[ch] != 0:
            count = count + 1
        ch = chr(ord(ch) + 1)
        i = i + 1
    sortedDict = sorted(Dict.items(), key=lambda kv: kv[1], reverse=True)
    i = 0
    while i < count:
        print(sortedDict[i])
        i = i + 1


charInString(str(input("Enter a String\n")))
