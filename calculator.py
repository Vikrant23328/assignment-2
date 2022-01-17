import math
import time
print("Select an operation to perform")
time.sleep(2)
print("1. ADD")
print("2. SUB")
print("3. MUL")
print("4. DIV")
print("5. SQUARE ROOT")
print("6. RAISE TO POWER")


operation = input("Please enter choice (1/ 2/ 3/ 4/ 5/ 6/): ")
time.sleep(0.5)
# if operation == "1"or "2" or "3" or"4":
oplist = ["1","2","3","4"]
if (operation in oplist) :
 
   num1 = float(input("Enter First no: "))
   num2 = float(input("Enter Second no: "))
else :
   num = int(input("Enter no: "))

if operation == "1":
    time.sleep(1)
    print("The sum is " + str(num1+num2))

elif operation == "2":
    time.sleep(1)
    print("The sub is " + str(int(num1) - int(num2)))
   

elif operation == "3":
    num3 = num1*num2
    time.sleep(1)
    print("The mul is: " ,num3)
    
elif operation == "4":
    time.sleep(1)
    print("The div is " + str(int(num1) / int(num2)))
    
    
elif operation == "5":
    sqrt = math.sqrt(num)
    time.sleep(1)
    print("The square root " ,num,"is",sqrt )
    
    
elif operation == "6":
    time.sleep(1)
    
    print("The div is " + str(math.pow(num,2)))
else: 
    print("entered invalid number ")
