def max(list):
    max=list[0]
    for a in list:
        if a>max:
            max=a
    return max
print(max([1,9,3,4,5]))