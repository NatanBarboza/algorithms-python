def binary_search(array:list, target:int):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == target:
            return mid
        elif(array[mid] < target):
            low = mid + 1
        elif(array[mid] > target):
            high = mid - 1
        else:
            print("The target isn't on array.")
    
    return -1