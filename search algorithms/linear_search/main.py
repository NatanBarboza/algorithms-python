from linear_search import linear_search
from random import randrange

array = []

while(True):
    if(len(array) == 10):
        break

    array.append(randrange(0, 100))

print(array)
result = linear_search()

if(result is not False):
    print("The target is on array.")
else:
    print("The target isn't on array.")