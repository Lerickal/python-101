#strings
#variable names are always lower case ekko_x_diana

message = 'Hello World' #simpleString
message2 = "Teemo's world" #apostrophy
message3 = """Qiyana's kingdom 
rocks, breezes and hydrates""" #multiLine
message4 = "Ekko X Jinx"
message5 = " Diana X Leona "
message6 = "csv, ahh, file, do, this"

print(message)
print(message2)
print(message3)
print(message4[0])
print(message4[1])
print(message4[2])
print(message4[3])
print(message4[-4])
print(message4[-3])
print(message4[-2])
print(message4[-1])
print(len(message4))
print(len(message3))
print(len(message2))
print(message5.strip())
print(message5.lower())
print(message4.upper())
print(message6.split(','))