n = int(input("Enter number of numbers\n"))
a = []
i = 0
while i < n:
    a.append(int(input("")))
    i = i + 1
i = 0
while i < n:
    if a[i] > 0:
        print(a[i], end=" ")
    i = i + 1
