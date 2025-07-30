#control statements

num = 2
num1 = -3

num2 = int(input("Enter your first number: "))
num3 = int(input("Enter your second number: "))

if num2 > num3:
    print(num2, "is greater than" , num3)
elif num3 > num2:
    print(num2, "is less than" , num3)
else:
    print(num2, "is the equavalent of" ,num3)

if num > 0:
    print("This number is a positive")
elif num < 0:
    print("This number is a negative")
else:
    print("This number is either zero or negative")
    
if num1 > 0:
    print("This number is a positive")
elif num1 < 0:
    print("This number is a negative")
else:
    print("This number is either zero or negative")