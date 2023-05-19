from priority_queue import PriorityQueue
from heap_priority_queue import HeapPriorityQueue


class VertexElement:
    def __init__(self, weight: float = 1, *data):
        self.data = data
        self.weight: int = weight

    def __str__(self):
        return f'{self.weight}'


class Graph:
    def __init__(self, number_of_vertices: int, is_directed: bool = False):
        self._is_directed: bool = is_directed
        self._num_vertices: int = number_of_vertices
        self._adj_matrix: [[VertexElement]] = [[VertexElement(0)] * number_of_vertices for _ in
                                               range(number_of_vertices)]

    def add_vertex(self) -> None:
        self._adj_matrix.append([VertexElement(0)] * self._num_vertices)
        self._num_vertices += 1
        for i in range(self._num_vertices):
            self._adj_matrix[i].append(0)

    def add_edge(self, u: int, v: int, weight: float = 1.0) -> None:
        new_edge = VertexElement(weight)
        self._adj_matrix[u][v] = new_edge

        if not self._is_directed:
            self._adj_matrix[v][u] = VertexElement(weight)

    def remove_edge(self, u, v) -> None:
        self._adj_matrix[u][v] = VertexElement(0)
        if not self._is_directed:
            self._adj_matrix[v][u] = VertexElement(0)

    def print_graph(self):
        # row: [VertexElement]
        # for row in self._adj_matrix:
        #    for element in row:
        #       print(element.weight)
        for row in self._adj_matrix:
            print("[", end="")
            for element in row:
                print(element.weight, end=", ")
            print("]")

    def search_edge(self, u: int, v: int) -> int:
        if self._adj_matrix[u][v].weight == 0:
            return "There is no such edge"
        else:
            return self._adj_matrix[u][v].weight

    def number_of_vertices(self) -> int:
        return self._num_vertices

    def prims_mst_table(self, start: int = 0, print_mst: bool = False) -> list[[VertexElement]]:
        _infinity = float('inf')
        vertices_in_MST: list[bool] = [False for _ in range(self._num_vertices)]  # v
        result_matrix: [[VertexElement]] = [[VertexElement(0)] * self._num_vertices for _ in range(self.number_of_vertices())]  # v^2

        # self.print_graph()

        while (False in vertices_in_MST):

            minimum = VertexElement(_infinity, start, start)
            destination_vertex: int = start
            for i in range(self._num_vertices):  # v
                if vertices_in_MST[i]:
                    for j in range(self._num_vertices):  # v
                        if not vertices_in_MST[j] and self._adj_matrix[i][j].weight > 0:
                            if self._adj_matrix[i][j].weight < minimum.weight:
                                minimum = self._adj_matrix[i][j]
                                start, destination_vertex = i, j

            vertices_in_MST[destination_vertex] = True  # index [dest] is now True - won't go there again
            result_matrix[start][destination_vertex] = minimum
            if minimum.weight == _infinity:
                result_matrix[start][destination_vertex] = VertexElement(0)
            result_matrix[destination_vertex][start] = result_matrix[start][destination_vertex]

            # print(f"{start} -> {end} : {result_matrix[start][end]}")
        if print_mst:

            print("MST adjacency Matrix - table:")
            for row in result_matrix:
                print("[", end="")
                for element in row:
                    print(element.weight, end=", ")
                print("]")

        return result_matrix

    def prims_mst_priority_queue(self, starting_vertex: int = 0, print_mst: bool = False) -> list[[VertexElement]]:

        vertices_in_MST: list[bool] = [False for _ in range(self._num_vertices)]

        result_matrix = [[VertexElement(0)] * self._num_vertices for _ in range(self.number_of_vertices())]  # v^2

        start_vertex = VertexElement(0, starting_vertex, starting_vertex)

        # priority_queue = PriorityQueue()
        priority_queue = HeapPriorityQueue()
        priority_queue.push(start_vertex.data, start_vertex.weight)  # v max

        while False in vertices_in_MST:  # v

            edge, minimum_weight = priority_queue.pop()
            starting_vertex, destination_vertex = edge[0], edge[1]

            if vertices_in_MST[destination_vertex]:  # not needed
                continue

            vertices_in_MST[destination_vertex] = True
            result_matrix[starting_vertex][destination_vertex] = VertexElement(minimum_weight, starting_vertex,
                                                                               destination_vertex)
            result_matrix[destination_vertex][starting_vertex] = VertexElement(minimum_weight, starting_vertex,
                                                                               destination_vertex)
            # print(f"{starting_vertex} -> {destination_vertex} : {result_matrix[starting_vertex][destination_vertex]}")

            for i in range(len(result_matrix)):  # v
                if self._adj_matrix[destination_vertex][i].weight > 0 and destination_vertex != i:
                    if not vertices_in_MST[i]:
                        edge_element = VertexElement(self._adj_matrix[destination_vertex][i].weight, destination_vertex, i)
                        priority_queue.push(edge_element.data, edge_element.weight)
        if print_mst:
            print("MST adjacency Matrix - queue:")
            for row in result_matrix:
                print("[", end="")
                for element in row:
                    print(element.weight, end=", ")
                print("]")

        return result_matrix
