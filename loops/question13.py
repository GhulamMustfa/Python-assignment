rows = 5
for a in range(1,rows + 1):
    for b in range(rows - a):
        print(" ", end="")
    for c in range(2 * a - 1):
        print("*", end="")
    print() 
