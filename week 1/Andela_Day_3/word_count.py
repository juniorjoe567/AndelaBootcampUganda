def words(string):
    # my empty dictonary
    dict = {}
    # my list wsh is to be split
    list = string.split()
    # checking for a word in my list
    for word in list:

        if word.isdigit():
            word = int(word)

        if word in dict:
            # dict[word] += 1
            dict[word] = dict[word] + 1

        else:
            dict[word] = 1

    return dict
