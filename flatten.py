myArray = [[1, 'a', {"name"}, ['cat'], 2], [[3], (3, 5), ['dog']], 4, 5]
result = []


def flattenArray(myArray):
    for arr in myArray:
        if(type(arr) != list and type(arr) != tuple and type(arr) != set):
            result.append(arr)
        else:
            flattenArray(arr)


flattenArray(myArray)
print(result)
