#kahn algorith for topological sort and checking cycles
from collections import defaultdict, deque
class Khan:
    def __init__(self, num_of_vertices):
        self.adj_list = defaultdict(list)
        self.num_of_vertices = num_of_vertices
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
    
    def topological_sort(self):
        
        #computar e armezar os indregrees de cada nó
        in_degree = [0] * self.num_of_vertices

        for i in self.adj_list:
            for j in self.adj_list[i]:
                in_degree[j] += 1

        #get the start nodes with indegree of 0, meaning they depends of no one
        queue = deque()
        for index, degree in in_degree:
            if degree == 0:
                queue.append(index)

        count = 0

        top_sort = []

        while queue:
            
            pos = queue.popleft()
            top_sort.append(pos)
            count += 1
            for v in self.adj_list[pos]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        if count != len(self.adj_list):
            return None
    
        return top_sort
        






    
