def sort_list(l1=[]):
    for i in range(len(l1)):
        for j in range(i, len(l1)):
            if(l1[i] > l1[j]):
                temp = l1[j]
                l1[j] = l1[i]
                l1[i] = temp
                # l1[j], l1[i] = l1[i], l1[j]
    return l1


l1 = [2, 4, 4, 1, 6, 2]
print(sort_list(l1))
