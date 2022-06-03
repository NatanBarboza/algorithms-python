class Heap:
    def __init__(self, array:list):
        self.array = array

    def smaller_element(self):
        return self.array[1]

    def left_son(self, index:int):
        return self.array[2 * index]
    
    def right_son(self, index:int):
        return self.array[(2 * index) + 1]
    
    def parent(self, index:int):
        return self.array[index // 2]

    def verify_heap(self):
        for i in range(2, len(self.array)):
            if(self.array[i] > self.array[i // 2]):
                return False
            return True

    def promote(self, n:int):
        index = n

        while(True):
            if(index == 1):
                break

            p = index // 2
            
            if(self.array[p] >= self.array[index]):
                break

            self.array[p], self.array[index] = self.array[index], self.array[p]
            index = p

    def demote(self, n:int):
        index = n

        while(True):
            c = 2 * index

            if(c > n):
                break

            if(c + 1 <= n):
                if(self.array[c + 1] > self.array[c]):
                    c += 1

            if(self.array[index] <= self.array[c]):
                break

            self.array[c], self.array[index] = self.array[index], self.array[c]
            index = c

    def heapsort(self, n:int):
        for i in range(2, n):
            self.promote(i)

        for i in range(n, 1, -1):
            self.array[1], self.array[i] = self.array[i], self.array[1]
            self.demote(i - 1)