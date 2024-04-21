my_list = []

my_list = [10,20,30,40]

my_list.insert(3, 15)

my_other_list = [50,60,70]

my_list.extend(my_other_list)

del my_list[7]

my_list.sort()

for item in range(len(my_list)):
    # if my_list[item] == 30:
    #     print(my_list[item])
    if my_list[item] == 30:
        index = item
        print(index)
