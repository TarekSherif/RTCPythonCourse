def get_count(l1):
    count = 0

    if (type(l1) != type(1) and type(l1) != type(1.0)):
        for i in l1:
            count = count+1
    return count


print(get_count("65675.0"))
# print(len(65675))
