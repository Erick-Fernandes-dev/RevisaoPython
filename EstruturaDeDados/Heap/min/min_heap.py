class MinHeap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def sift_up(self, i):

        stop = False

        while (i // 2 > 0) and stop == False:

            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            else:
                Stop = True
            i = i // 2
    
    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.sift_up(self.current_size)
    
    def sift_down(self, i):

        while (i * 2) <= self.current_size:
            
            mc = self.min_child(i)
            
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc
    
    def min_child(self, i):
        
        if (i * 2)+1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1
    
    def delete_min(self):
        if len(self.heap_list) == 1:
            return 'Empty heap'
 
        root = self.heap_list[1]
 
        
        self.heap_list[1] = self.heap_list[self.current_size]
 
        *self.heap_list, _ = self.heap_list
 
        self.current_size -= 1
 
        self.sift_down(1)
 
        return root
    

m = MinHeap()
m.insert(10)
m.insert(5)
m.insert(6)
m.insert(3)
m.insert(4)

print(m.heap_list)
print(m.delete_min())

print(m.heap_list)

print(m.delete_min())

print(m.heap_list)