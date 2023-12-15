from utils.samples import sample_graph
from utils.helpers import adj_list_to_edge_list
from union_find import union, find

edges = adj_list_to_edge_list(sample_graph)

edges.sort()