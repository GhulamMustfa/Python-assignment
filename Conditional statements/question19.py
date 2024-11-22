string = input("Enter a string : ")
if string.isupper():
    print(f"{string} is in uppercase")
elif string.islower():
    print(f"{string} is in lowercase")
else:
    print(f"{string} is a mix")
