# # name = "abdullah"
# #       # 01234567
# #       # 87654321 (-ve value)

# # index = name.find("h") #returns the index of the alphabet
# # print(name[0:5])
# # shortname = name[0:3]
# # print(shortname)
 
# # print(name[-3:-1])
# # print(index)
# # rep = "shabs loves nasreen"
# # replace = rep.replace("shabs, nasreen")
# # print(replace) 

# # print

# n = input("Enter your name: ")
# print(f"Good Morning, {n}")

letter = '''
        Dear <|NAME|>, 
        You are selected!
        <|DATE|> '''

print(letter.replace("<|NAME|>", "Abdullah").replace("<|DATE|>", "20/06/2024"))

naam = "abdullah   is a good boi"

print(naam.find("    ")) # returns the index of the first occurrence of "a"

naam1 = "abdullah   is a good boi"
print(naam1.replace("   ", " ")) # returns the index of the first occurrence of "a"