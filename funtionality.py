#functions

def greetings(name):
    print(f"Hi {name}")
    
greetings("Alice")

def add(a,b):
    return a + b

print(add(5,3))

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
def minus(a,b):
    return a-b 

def divide(a,b):
    return a/b 

def multiply(a,b):
    return a*b 