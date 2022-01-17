import math
import time
print("Select an operation to perform")
time.sleep(1)
print("1. ADD")
print("2. SUB")
print("3. MUL")
print("4. DIV")
print("5. SQUARE ROOT")
print("6. RAISE TO POWER")


operation = input()
time.sleep(1)


if operation == "1":
    num1 = float(input("Enter First no: "))
    num2 = float(input("Enter Second no: "))
    time.sleep(1)
    print("The sum is " + str(num1+num2))
elif operation == "2":
    num1 = input("Enter First no: ")
    num2 = input("Enter Second no: ")
    time.sleep(1)
    print("The sub is " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = int(input("Enter First no: "))
    num2 = int(input("Enter Second no: "))
    
    num3 = num1*num2
    time.sleep(1)
    print("The mul is: " ,num3)
elif operation == "4":
    num1 = input("Enter First no: ")
    num2 = input("Enter Second no: ")
    time.sleep(1)
    print("The div is " + str(int(num1) / int(num2)))
elif operation == "5":
    num = int(input("Enter no: "))
    sqrt = math.sqrt(num)
    time.sleep(1)
    print("The square root " ,num,"is",sqrt )
    
elif operation == "6":
    num = int(input("Enter  no: "))
    pow = math.pow(num,2)
    time.sleep(1)
    print("square of ",num,"is",pow)
    
else: 
    print("entered invalid number ")

    