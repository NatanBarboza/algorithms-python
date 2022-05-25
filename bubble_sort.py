def bubble_sort(array):
    l = len(array)
    for i in range(l - 1, 0, -1):
        for j in range(i):
            if(array[j] > array[j + 1]):
                temp = array[j]
                array[j], array[j + 1] = array[j + 1], temp
    
    return print(array)