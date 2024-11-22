a=0
b=1
c=0
print("The first 10 Fibonacci numbers are :")
print(a)
print(b)
for num in range(1,9):
    c=a+b
    a=b
    b=c
    print(c)
    