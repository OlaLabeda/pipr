
def count_symbols(arr):
    dictionary = {}
    for i in arr:
        for j in i:
            if j not in dictionary.keys():
                dictionary[j] = 1
            else:
                dictionary[j] += 1
    return dictionary


arr = [['a', 'c', 'o'], ['a', 'a', 'c'], ['d', 'o', 'O'], ['c', 'b', 'a']]

print(count_symbols(arr))
