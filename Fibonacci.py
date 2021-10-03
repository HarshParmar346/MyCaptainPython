n = int(input("Enter value of n\n"))
f = 0
s = 1
s2 = 0
for i in range(n):
    print(f, end=" ")
    s2 = f + s
    f = s
    s = s2
