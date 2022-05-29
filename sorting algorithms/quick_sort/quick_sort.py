def partition(array, start, end):
    pivot = array[end]
    i = start
    
    for j in range(start, end):
        if(array[j] <= pivot):
            array[j], array[i] = array[i], array[j]
            i += 1
    array[i], array[end] = array[end], array[i]
    return i

def quick_sort(array, start=0, end=None):
    if(end is None):
        end = len(array) - 1
    if(start < end):
        p = partition(array, start, end)
        quick_sort(array, start, p - 1)
        quick_sort(array, p + 1, end)