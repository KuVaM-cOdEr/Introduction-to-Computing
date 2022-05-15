def countthebits( n ):
    count = 0
    while n:
        count+=1
        n&=(n-1)
    return count
def flipthecount(a , b):
    return countthebits(a^b)
a = int(input("enter first number="))
b = int(input("enter seond number="))
print(flipthecount(a, b))


