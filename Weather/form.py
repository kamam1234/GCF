my_list = [1,2,34,5,6,7,89,90,10,27,23,4,53,2,4,4,5,2454,3]
my_list[:] =[x for x in my_list if x%2 !=0]
print(my_list)


