list = ["hi", 2, 3.5, 2]
print(list)

'''
item = 2
list.remove(item)
print(list)

list.reverse()
print(list)
'''

copy_of_list = []
print(copy_of_list)


copy_of_list.append(list)
print(copy_of_list)

for x in list:
   copy_of_list.append(x)

print(copy_of_list)
