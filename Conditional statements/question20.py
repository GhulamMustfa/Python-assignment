num = int(input("Enter a number : "))
if num > 1:
    for prime in range(2,num):
          if num % prime == 0:
            print("Its not a prime number")
            break
    else:
        print("Its a prime number.")
else:
    print("its not a prime number")
