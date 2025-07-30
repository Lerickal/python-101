#loops

fruits = ["apple","banana","pear","orange","mango"]

for fruit in fruits:
    print(fruit)

print()
print(fruits)
print()

numbers = [0,1,2,3,4,5,6,7,8,9]

for number in numbers:
    print(number)

print()    
print(numbers)
print()

count = 1

while count <= 9:
    print(count, "rabbit")
    count += 1

print()  
#loop control statements

vegies = ["potatoe","cabbage","spinash","pumpkin","carrot","bean","kale","raddish","eggplant"]

for veg in vegies:
    if veg == "carrot":
        break #stops when finds carrot
    print(veg)
    
print()

for veg in vegies:
    if veg == "carrot":
        continue #skips carrot
    print(veg)