side1 = float(input("Enter the length of the 1st side: "))
side2 = float(input("Enter the length of the 2nd side: "))
side3 = float(input("Enter the length of the 3rd side: "))

if side1 == side2 == side3 :
    print("Equilateral")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles")
else :
    print("Scalene")
