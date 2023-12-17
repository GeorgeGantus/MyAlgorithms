
def adj_list_to_edge_list(adj_list):
    out = []
    for key in adj_list.keys():
        for edge in adj_list[key]:
            out.append((edge.weight, key, edge.target))
    return out