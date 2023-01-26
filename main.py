from functools import reduce
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

newlist = list(map(lambda x: x*x*x, my_list))
print("Map: ", newlist)

filtered_list = list(filter(lambda x: x > 2, my_list))
print("Filterd List: ", filtered_list)


print("Reduce: ", reduce(lambda x, y: x+y, my_list))
