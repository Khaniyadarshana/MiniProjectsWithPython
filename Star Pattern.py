print("Pattern Printing")
num = int(input("Enter the number of rows you want:\n"))
bool_val = input("Enter 1 or 0 and see the magic")
if bool_val=="1":
    for i in range(0,num+1):
        print("*"*i)


if bool_val=="0":
    for i in range(num,0,-1):
        print("*"*i)


