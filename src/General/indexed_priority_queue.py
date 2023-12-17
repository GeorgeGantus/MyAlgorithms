class IndexedPriorityQueue:
    def __init__(self):

        

        self.heap = []
        self.mapper = {}
        return
    
    def heapify_up(self, index):
        current_index = index
        parent_index = self.get_parent(index)
        while current_index != 0 and self.heap[parent_index] > self.heap[current_index]:
            self.swap(current_index, parent_index)
            current_index = parent_index
            parent_index = self.get_parent(current_index)

    def heapify_down(self, index):
        child_a, child_b = self.get_childs(index)
        current_index = index

        #TODO: check if indexes are in bound, this function and in get_childs
         
        while self.heap[current_index] > self.heap[child_a] or self.heap[current_index] > self.heap[child_b]:
            if self.heap[child_a] <= self.heap[child_b]:
                self.swap(child_a, current_index)
                current_index = child_a
            else:
                self.swap(child_b, current_index)
                current_index = child_b
            child_a, child_b = self.get_childs(current_index)

        

        return


    def swap(self,a,b):
        aux = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = aux

    
    def get_parent(index):
        if index == 0: return None

        if index % 2 == 2:
            return (index-2)/2
        
        return (index-1)/2
    
    def get_childs(index):
        return 2*index+1, 2*index + 2