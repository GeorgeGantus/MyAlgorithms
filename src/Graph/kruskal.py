from utils.samples import sample_graph
from utils.helpers import adj_list_to_edge_list
from union_find import UnionFind




def kruskal(adj_list):
    edges = adj_list_to_edge_list(sample_graph)
    edges.sort()

    union_find = UnionFind(adj_list.keys())
    output = []
    outputSize = 0
    for weigth, origin, target  in edges:

        if not union_find.is_connected(origin, target):
            union_find.union(origin, target)
            output.append((weigth, origin, target))
            outputSize += weigth

        if union_find.num_of_components == 1:
             return outputSize, output
    return outputSize, output

print(kruskal(sample_graph))