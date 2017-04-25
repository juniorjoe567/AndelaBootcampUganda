def find_max_min(input_value):
    min_value = min(input_value)
    max_value = max(input_value)

    if min_value == max_value:
        return [len(input_value)]
    return [min_value, max_value]


print (find_max_min([1, 2, 3, 4]))