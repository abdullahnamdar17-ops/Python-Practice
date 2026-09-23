list1 = ['a','b','c']

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print ("Palindrome")
else:
    print("NOT Palindrome")

list1.append("f")
list1.append("f")
print(list1)
print (list1.count('f'))