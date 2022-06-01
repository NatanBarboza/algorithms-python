def linear_search(array:list, target:int):
    found = False
    position = 0

    while(position < len(array) and found == False):
        if(array[position] == target):
            found = True
        position += 1

    return found