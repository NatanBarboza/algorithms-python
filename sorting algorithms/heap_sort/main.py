from heaps import Heap

if(__name__ == "__main__"):
    array = ['', 34, 13, 21, 2, 3, 5, 8, 0, 1, 1]
    heap = Heap(array)

    print(heap.array)

    heap.heapsort(10)
    print(array)