s = str(input("Enter a String"))
a = []
ch = 'A'
i = 0
while i < 26:
    a.append(0)
    i = i + 1
i = 0
j = 0
while i < 26:
    while j < len(s):
        if (ch - s[j] == 0) or (ch - s[j] == -32):
            a[ch - 65] = a[ch - 65] + 1
        j = j + 1
    ch = ch + 1
    i = i + 1
count = 0
i = 0
while i < 26:
    if a[i] != 0:
        count = count + 1
    i = i + 1
char = []
num = []
i = 0
while i < 26:
    if a[i] != 0:
        char.append(char(i + 97))
        num.append(a[i])
    i = i + 1
temp = ''
temp2 = 0
i = 0
j = 0
while i < count - 1:
    while j < count - i - 1:
        if num[j + 1] > num[j]:
            temp2 = num[j + 1]
            num[j + 1] = num[j]
            num[j] = temp2
            temp = char[j + 1]
            char[j + 1] = char[j]
            char[j] = temp
        j = j + 1
    i = i + 1
i = 0
while i < count:
    print(str(char[i]) + " = " + str(num[i]))
