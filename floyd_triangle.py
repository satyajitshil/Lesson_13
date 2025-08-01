
beg = 1
rows = int(input("Enter the number of rows: "))
for i in range(rows):
    i += 1
    for j in range(i):
        print(beg, end=" ")
        beg += 1
    print()

