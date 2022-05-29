from tracemalloc import start
from quick_sort import quick_sort
import random


array = random.sample(range(0, 100), 10)
print(f"Arranjo não ordenado: {array}")

start = 0
end = len(array) - 1

quick_sort(array, start, end)
print(f"Array ordenado: {array}")