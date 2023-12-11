from utils.samples import unconnected_graph

def union_find(adj_list):
    #Assume that each node is mapped to a integer, if its not your case create a map first

    num_of_components = len(adj_list.keys())
    parents = [i for i in range(num_of_components)]
    size = [1 for _ in range(num_of_components)]

    for source, edges in adj_list.items():
        for edge in edges:
            num_of_components = union(source, edge.target, size, parents, num_of_components)
    
    return num_of_components, size


def union(node_a, node_b, size, parents, num_of_components):

    root_a, root_b = find(node_a, parents), find(node_b, parents)

    if root_a == root_b:
        return num_of_components

    if size[root_a] >= size[root_b]:
        size[root_a] += size[root_b]
        size[root_b] = 0
        parents[root_b] = root_a
    else:
        size[root_b] += size[root_a]
        size[root_a] = 0
        parents[root_a] = root_b


    return num_of_components - 1


def find(target, parents):
    root = target
    while parents[root] != root:
        root = parents[root]
    
    #path compression
    while target != root:
        nxt = parents[target]
        parents[target] = root
        target = nxt

    return target

def main():
    print(union_find(unconnected_graph))

if __name__ == '__main__':
    main()
