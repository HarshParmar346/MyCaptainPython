s = input("Enter A file name with extension\n")
s2 = ""
flag = 0
k = 0
for i in s:
    if i == '.':
        flag = 1
    if flag == 1:
        s2 += i
if s2 == ".py":
    print("Python")
if s2 == ".java":
    print("JAVA")
if s2 == ".txt":
    print("TEXT")
if s2 == ".c":
    print("C File")
if s2 == ".cpp":
    print("C++ File")
else :
    print("Could not find file type")