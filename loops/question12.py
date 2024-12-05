print("Prime numbers between 1 and 50 are:")

# 1 is not a prime number.

for num in range(2, 51):
    is_prime = True 
    for i in range(2, int(num ** 0.5) + 1): 
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
          print(num, end=" ")
