num1 = float(input("Enter 1st Number : "))
num2 = float(input("Enter 2nd Number : "))
operator = input("Enter the operator (+,-,/,*) : ")

if operator == "+":
    print(f"The result is: {num1 + num2}")
elif operator == "-":
      print(f"The result is: {num1 - num2}")
elif operator == "*":
     print(f"The result is: {num1 * num2}")
elif operator == "/":
     if num2 != 0:
        print(f"The result is: {num1 / num2}")
     else:
          print("Error : Division by zero")
else:
     print = ("Error, Enter the correct operator ")

