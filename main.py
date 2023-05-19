from graph_adjacency_matrix import Graph
from graph_adjacency_list import GraphAdjacencyList
from graph_with_dictionaries import GraphAdjacencyDict
from random import randint
from random import random
from time import time

if __name__ == '__main__':

    GRAPH_VERTICES: int = 5

    graph_dict: GraphAdjacencyDict = GraphAdjacencyDict(GRAPH_VERTICES)
    graph_list: GraphAdjacencyList = GraphAdjacencyList(GRAPH_VERTICES)

    for i in range(GRAPH_VERTICES):
        for j in range(GRAPH_VERTICES):
            if random() <= 1:
                x: int = randint(1, 200)
                graph_dict.add_edge(i, j, x)
                graph_list.add_edge(i, j, x)

    graph_matrix: Graph = Graph(GRAPH_VERTICES)

    for j in range(graph_matrix.number_of_vertices()):
        i = j
        while i < graph_matrix.number_of_vertices():
            if random() < 1:
                if i == j:
                    graph_matrix.add_edge(j, i, 0)
                    i += 1
                    continue
                graph_matrix.add_edge(j, i, randint(1, 200))
            i += 1

    # print("-------------------- List --------------------")
    # graph_list.print_adj_list()
    # print("-------------------- Matrix --------------------")
    graph_matrix.print_graph()
    print("-------------------- MST START --------------------")
    time1 = time()
    graph_matrix.prims_mst_priority_queue(print_mst=True)
    time2 = time()
    #
    time3 = time()
    graph_matrix.prims_mst_table(print_mst=True)
    time4 = time()
    #
    time5 = time()
    graph_list.prim_mst(print_mst=True)
    time6 = time()
    #
    time7 = time()
    graph_list.prims_mst_with_list(print_mst=True)
    time8 = time()
    #
    time9 = time()
    graph_dict.prim_mst_dict(print_mst=False)
    time10 = time()
    print("----- MST Matrix + PRIORITY QUEUE -----")
    print(time2 - time1)
    print("----- MST Matrix + ITERACJA -----")
    print(time4 - time3)
    print("----- MST LISTA + STOS + PQ -----")
    print(time6 - time5)
    print("----- MST LISTA + LISTA + PQ -----")
    print(time8 - time7)
    print("----- MST DICT + STOS + PQ -----")
    print(time10 - time9)
