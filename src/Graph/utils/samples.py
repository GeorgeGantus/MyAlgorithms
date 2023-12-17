from utils.edge import Edge

#undirected as directed sample
sample_graph = {
    0: [Edge(1,9),Edge(3,5),Edge(5,7),Edge(2,0)],
    1: [Edge(0,9),Edge(3,-2),Edge(6,4),Edge(4,3)],
    2: [Edge(0,0),Edge(5,6)],
    3: [Edge(0,5),Edge(5,2),Edge(6,3),Edge(1,-2)],
    4: [Edge(1,3), Edge(6,6)],
    5: [Edge(2,6), Edge(0,7), Edge(3,2), Edge(6,1)],
    6: [Edge(5,1), Edge(3,3), Edge(1,4), Edge(4,6)],
}


unconnected_graph = {
    0: [Edge(1,1)],
    1: [Edge(6,1)],
    2: [Edge(3,1)],
    3: [Edge(5,1)],
    4: [],
    5: [Edge(4,1)],
    6: [],
}