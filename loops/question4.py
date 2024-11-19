num = int(input("Enter a number : "))
print(f"Multiplication Table of {num}:")
for number in range(1, 11):
    print(f"{num} x {number} = {num * number}")
