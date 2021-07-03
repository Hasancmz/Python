myArray = [[[1, 2], 3], [4, 5], [6, 7, 8], [9, 10, [11, 12]]]


def reverseArray(myArray):
    myArray.reverse()
    for arr in myArray:
        if(type(arr) == list):
            reverseArray(arr)


reverseArray(myArray)
print(myArray)
