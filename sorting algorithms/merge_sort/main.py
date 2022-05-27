from merge_sort import merge_sort
import random


array = random.sample(range(0, 100), 10)
print(f"Arranjo não ordenado: {array}")

aux = [0] * len(array)
merge_sort(array, aux, 0, len(array) - 1)
print(f"Array ordenado: {array}")