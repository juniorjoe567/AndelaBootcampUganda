
def find_missing(x, y):
    if not x and not y:
        return 0
    if not set(x) ^ set(y):
        return 0
    else:
        return list(set(x) ^ set(y))[0]


print (find_missing([0, 1, 2], [1, 2]))
print (find_missing([1, 2, 3], [1, 2, 3, 4]))
print (find_missing([4, 6, 8], [4, 6, 8, 10]))
print (find_missing([5, 4, 7, 77], [5, 4, 7]))