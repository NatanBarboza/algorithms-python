from random import randrange
from selection_sort import selection_sort
from bubble_sort import bubble_sort

array = []

while(True):
    if(len(array) == 10):
        break

    array.append(randrange(0, 100))

bubble_sort(array)
selection_sort(array)