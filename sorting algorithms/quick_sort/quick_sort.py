# def partition(array, left, right):
#     pointer = array[left]

#     i = left
#     j = right

#     while(i <= j):
#         while(array[i] <= pointer):
#             i += 1

#             if(i == right):
#                 break

#         while(pointer <= array[j]):
#             j -= 1
            
#             if(j == left):
#                 break

#         if(i >= j):
#             break

#         array[i], array[j] = array[j], array[i]

#     pointer, array[j] = array[j], pointer

#     return j

# def quick_sort(array, left, right):
#     if(left >= right):
#         return

#     index_pointer = partition(array, left, right)
#     quick_sort(array, left, index_pointer - 1)
#     quick_sort(array, index_pointer + 1, right)


def partition(array, start, end):
    pivot = array[end]
    bottom = start - 1
    top = end

    done = 0

    while(not done):
        while(not done):
            bottom += 1

            if(bottom == top):
                done = 1
                break

            if(array[top] > pivot):
                array[top] = array[bottom]
                break

        while(not done):
            top -= 1

            if(top == bottom):
                done = 1
                break

            if(array[top] < pivot):
                array[bottom] = array[top]
                break

        array[top] = pivot
        return top

def quick_sort(array, start, end):
    if(start < end):
        split = partition(array, start, end)
        quick_sort(array, start, split - 1)
        quick_sort(array, split + 1, end)
    else:
        return