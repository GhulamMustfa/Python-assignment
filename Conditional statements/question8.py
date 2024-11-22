string = input("Enter a string : ")

lowercase_string = string.replace(" ", "").lower()

if lowercase_string == lowercase_string[::-1]:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
