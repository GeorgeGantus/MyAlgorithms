from heapq import heappop,heappush, heapify

#(target, weight)
#this sample graph is a undirected graph writen as a directed graph
sample_graph = {
    0: [(1,9),(3,5),(5,7),(2,0)],
    1: [(0,9),(3,-2),(6,4),(4,3)],
    2: [(0,0),(5,6)],
    3: [(0,5),(5,2),(6,3),(1,-2)],
    4: [(1,3), (6,6)],
    5: [(2,6), (0,7), (3,2), (6,1)],
    6: [(5,1), (3,3), (1,4), (4,6)],
}