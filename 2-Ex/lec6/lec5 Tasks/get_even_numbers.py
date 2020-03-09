def get_even_numbers(l1=[]):
    temp = []
    for x in l1:
        if x % 2 == 0:
            temp.append(x)
    return temp


L1 = get_even_numbers([2, 3, 4, 1, 6, 9])  # [2,4,6]
print(L1)
