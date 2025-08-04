def sub_test_1():
    n = int(input("Type the number of rows you want:"))
    for i in range(n):
        for j in range(i+1):
            print( "*", end = "")
        print()
def sub_test_2():
    n = int(input("How many rows do you want:")) 
    for i in range(n):
        spaces = n - i - 1 
        star = i + 1
        for j in range(i + 1):
           print( "*", end = " ")
        print(star)       
    

if __name__ == "__main__":
    sub_test_2()
#  * 
#  * *
#  * * * 

# expected ending for the project

#      *
#    * *
#  * * *

