def get_min(l1: list):
    if(len(l1) > 0):
        min = l1[0]
    else:
        min = "Can not get min to empaty list"
    for i in l1:
        if(min > i):
            min = i
    return min


print(get_min([2, 4, 4, 1, 6, 2]))
# print(get_min(["tarek1", "Ahmed", "ahmed"]))
# print(ord("A"))
# print(ord("a"))
