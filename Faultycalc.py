print("Operations are: 1. Addition 2. Subtraction. 3. Multiplication 4. Division")
opt = int(input("Select an operation"))
val1 = input(print("Please enter first number:" ))
val1 = float(val1)
val2 = input(print("Please enter second number:" ))
val2 = float(val2)


if opt > 4 or opt < 1:
    print("Choose valid operator")
elif val1==45 and val2==3 and opt==3:
    print("555")
elif val1==56 and val2==9 and opt==1:
    print("77")
elif val1==56 and val2==6 and opt==4:
    print("4")
else:
    if(opt == 1):
        print(val1+val2)
    elif(opt == 2):
        print(val1 - val2)
    elif (opt == 3):
        print(val1 * val2)
    elif (opt == 4):
        print(val1 / val2)

