num = int(input("Enter the number : "))
if num < 0:
    print("Error : The number cannot be negative.")
else:
    factorial = 1
    a = 1
    while a <= num:
        factorial *= a
        a += 1
    print(f"The factorial of {num} is: {factorial}")
