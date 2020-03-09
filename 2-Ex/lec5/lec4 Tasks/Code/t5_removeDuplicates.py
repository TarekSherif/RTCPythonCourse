def removeDuplicates(l1=[]):
    temp = []
    for i in l1:
        if(not(i in temp)):
            temp.append(i)
    return temp


l1 = [2, 4, 4, 1, 6, 2]
print(removeDuplicates(l1))
