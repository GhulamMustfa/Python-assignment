side1 = int(input("Enter 1st Side : "))
side2 = int(input("Enter 2nd Side : "))
side3 = int(input("Enter 3rd Side : "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("It is a valid triangle")
else:
    print("its not a triangle")
