list1 = list(x for x in range(5))
print(list1)

list1.append(8)
print(list1)
list1[len(list1):]=[90]
print(list1)


list1.extend([43,62,25,382])
print(list1)