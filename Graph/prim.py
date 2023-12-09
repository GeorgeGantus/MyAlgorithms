#Lazy Version O(Elog(E)) where E is the number of Edges
from heapq import heappop,heappush, heapify
from utils import samples
from utils.edge import Edge

graph = samples.sample_graph

#return the edges of the mst (Minimum spanning tree)
def prim(start_node, adj_list):
    #initialize data
    queue = []
    visited = set([start_node])
    #whe know that the mst will have num of vertex -1 edges
    target_size = len(adj_list.keys())-1
    output = []
    outputSize = 0

    #Initialize the queue with the edges of the start node    
    for edge in adj_list[start_node]:
        heappush(queue, (edge.weight, edge.target))
    

    while queue and len(output) != target_size:
        weigth, current = heappop(queue)
        if current in visited:
            continue
        output.append(Edge(current, weigth))
        outputSize += weigth
        visited.add(current)

        for edge in adj_list[current]:
            if (edge.target not in visited):
                heappush(queue, (edge.weight, edge.target))
    return outputSize, output

print(prim(0,graph))

