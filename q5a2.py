a = int(input("length of side 1 : "))
b = int(input("length of side 2 : "))
c = int(input("length of side 3 : "))
while ((a+b)>c) and ((a+c)>b) and ((b+c)>a):
    print("Yes")
    break
while ((a+b)<c) or ((a+c)<b) or ((b+c)<a):
    print("No")
    break

