#exception handling

try:
    print(x)
except NameError:
    print("Variable x is not defined")
    
try:
    print(y)
except:
    print("An exceprion has occured")
    
try:
    print(a)
except:
    print("Something went wrong")
finally:
    print("finally always runs whether there was an exception or not")
    
try:
    print(b)
except NameError:
    print("Variable b is not defined")
else:
    print("Something else went wrong")