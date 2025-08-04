
n = int(input("How many rows do you want:")) 
for i in range(n):
    spaces = n - i - 1 
    star = i + 1
    for x in range(spaces):
        print(" ", end = " ")
    for j in range(star):
        print( "*", end = " ")
    print() 