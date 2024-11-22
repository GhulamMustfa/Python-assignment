num = int(input("Enter the numbers : "))
reversed_num = int(str(abs(num))[::-1])
if num < 0 :
    reversed_num = -reversed_num
print(reversed_num)
