total_Rows = int(input("Type the # of rows for your diamond:"))
if total_Rows%2 == 0:
    half_Rows = int(total_Rows/2)
else:
    half_Rows = int(total_Rows/2) + 1
space = int(half_Rows) - 1

for i in range(1 , half_Rows):
    for j in range(1, space + 1):
        print(end = " ")
    space = space - 1
    num = 1
    for j in range(2 * i - 1):
        print(end = str(num))
        num += 1
    print()
space = 1
for i in range(1 , half_Rows):
    for j in range(1, space + 1):
        print(end = " ")
    space = space + 1
    num = 1
    for j in range(1, 2 * (half_Rows - i)):
        print(end = str(num))
        num += 1
    print()
