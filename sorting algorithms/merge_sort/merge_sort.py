def merge(array, aux, left, mid, right):
    for i in range(left, right + 1):
        aux[i] = array[i]
    j = left
    k = mid + 1

    for i in range(left, right + 1):
        if(j > mid):
            array[i] = aux[k]
            k += 1
        elif(j > right):
            array[i] = aux[i]
            j += 1
        elif(aux[k] < aux[j]):
            array[i] = aux[k]
            k += 1
        else:
            array[i] = aux[j]
            j += 1

def merge_sort(array, aux, left, right):
    if right <= left:
        return
    
    mid = (left + right) // 2

    merge_sort(array, aux, left, mid)

    merge_sort(array, aux, mid + 1, right)

    merge(array, aux, left, mid, right)