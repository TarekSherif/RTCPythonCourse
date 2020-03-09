def get_sum(l1):
    sum = 0
    for i in l1:
        sum += i
    return sum


def get_count(l1):
    count = 0
    for i in l1:
        count += 1
    return count


def get_avg(l1):
    return get_sum(l1)/get_count(l1)


print(get_avg([11, 44, 33]))
