def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

num1 = int(input("Please enter number:"))
print("The fibbonaci number is", fibonacci(num1))