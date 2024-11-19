num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter Third Number : "))

if num1 > num2 and num1 > num3:
    print("The largest number is first number.")
elif num2 > num1 and num2 > num3:
    print("The largest number is second number.")
elif num3 > num1 and num3 > num2:
    print("The largest number is third number.")
else:
    print("all are equal")
    