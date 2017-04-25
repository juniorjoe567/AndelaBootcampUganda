def data_type(N):
    # my_argument for returning a legnth
    if type(N) == str:
        return len(N)
        # my_argument for returning NO VALUE

    elif type(N) == type(None):
        return 'no value'

    # my_argument for returning BOOLEAN
    elif type(N) == bool:
        return N

    # my_argument for returning INTERGERS
    elif type(N) == int:
        if N < 100:
            return "less than 100"
        elif N > 100:
            return "more than 100"
        else:
            return 'equal to 100'

    # my_argument for returning lists
    elif type(N) == list:
        return N[2]
    else:
        return None
data_type(True)
