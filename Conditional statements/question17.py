num = int(input("Enter the number : "))

if num % 2 == 0 and num % 3 == 0 :
    print("Its a divisible of 2 and 3")
elif num % 2 == 0:
    print("it is divisible by 2")
elif num % 3 == 0:
    print("it is divisible by 3")
else:
    print("Its not a divisible of 2 and 3")
