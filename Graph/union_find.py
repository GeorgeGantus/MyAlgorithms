from utils.samples import unconnected_graph

adj_list = unconnected_graph
#Assume that each node is mapped to a integer, if its not your case create a map first

num_of_components = len(adj_list.keys())
parents = [i for i in range(num_of_components)]
size = [1 for _ in range(num_of_components)]

def union_find(edge_list):

    for source, edges in edge_list.items():
        for edge in edges:
            union(source, edge.target)
    
    return num_of_components


def union(node_a, node_b):

    global num_of_components
    root_a, root_b = find(node_a), find(node_b)

    if root_a == root_b:
        return

    if size[root_a] >= size[root_b]:
        size[root_a] += size[root_b]
        size[root_b] = 0
        parents[root_b] = root_a
    else:
        size[root_b] += size[root_a]
        size[root_a] = 0
        parents[root_a] = root_b


    num_of_components -= 1


def find(target):
    root = target
    while parents[root] != root:
        root = parents[root]
    
    #path compression
    while target != root:
        nxt = parents[target]
        parents[target] = root
        target = nxt

    return target

print(union_find(unconnected_graph))
print(size)
