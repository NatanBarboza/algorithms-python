from binary_search import binary_search
from random import randrange

def selection_sort(array):
    l = len(array)
    for i in range(l - 1, 0, -1):
        for j in range(i):
            if(array[j] > array[j + 1]):
                temp = array[j]
                array[j], array[j + 1] = array[j + 1], temp
    
    return array

array = []

while(True):
    if(len(array) == 10):
        break

    array.append(randrange(0, 100))

print(array)
selection_sort(array)
print(array)
result = binary_search(array, 10)
print(result)