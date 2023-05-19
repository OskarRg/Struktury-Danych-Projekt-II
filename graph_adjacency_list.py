from priority_queue import PriorityQueue
from stos import Stos
from heap_priority_queue import HeapPriorityQueue


class VertexElement:
    def __init__(self, vertex, weight: float = 1):
        self.vertex: int = vertex
        self.weight: int = weight
        self.next: VertexElement = None
        self.prev: VertexElement = None


class GraphAdjacencyList:

    def __init__(self, number_of_vertices: int, is_directed: bool = False):
        self._is_directed: bool = is_directed
        self._number_of_vertices: int = number_of_vertices
        self._adj_list: [VertexElement] = [None] * number_of_vertices

    def add_vertex(self, vertex_index: int) -> None:
        while self._number_of_vertices <= vertex_index:
            self._adj_list.append(None)
            self._number_of_vertices += 1

    def add_edge(self, source_vertex: int, destination_vertex: int, weight: int = 1) -> None:

        if destination_vertex >= self._number_of_vertices:
            self.add_vertex(destination_vertex)

        if self.is_edge(source_vertex, destination_vertex):
            # print(f"There is an edge between {u_vertex} and {v_vertex} already.")
            return None

        new_vertex = VertexElement(destination_vertex, weight)
        new_vertex.next = self._adj_list[source_vertex]

        if self._adj_list[source_vertex] is not None:
            self._adj_list[source_vertex].prev = new_vertex
        self._adj_list[source_vertex] = new_vertex

        if not self._is_directed and source_vertex != destination_vertex:

            new_vertex = VertexElement(source_vertex, weight)
            new_vertex.next = self._adj_list[destination_vertex]
            if self._adj_list[destination_vertex] is not None:
                self._adj_list[destination_vertex].prev = new_vertex
            self._adj_list[destination_vertex] = new_vertex

    def is_edge(self, source_vertex: int, destination_vertex: int) -> bool:
        seek_vertex: VertexElement = self._adj_list[source_vertex]
        while seek_vertex:
            if seek_vertex.vertex == destination_vertex:
                return True
            seek_vertex = seek_vertex.next
        return False

    def remove_edge(self, source_vertex: int, destination_vertex: int) -> None:
        if not self.is_edge(source_vertex, destination_vertex):
            print(f"There is no edge to remove between {source_vertex} and {destination_vertex}")
            return None
        seek_vertex: VertexElement = self._adj_list[source_vertex]
        while seek_vertex:
            if seek_vertex.vertex == destination_vertex:
                if seek_vertex.prev:
                    seek_vertex.prev.next = seek_vertex.next
                else:
                    self._adj_list[source_vertex] = seek_vertex.next
                if seek_vertex.next:
                    seek_vertex.next.prev = seek_vertex.prev
                break
            seek_vertex = seek_vertex.next

        if not self._is_directed:
            seek_vertex: VertexElement = self._adj_list[destination_vertex]
            while seek_vertex:
                if seek_vertex.vertex == source_vertex:
                    if seek_vertex.prev:
                        seek_vertex.prev.next = seek_vertex.next
                    else:
                        self._adj_list[destination_vertex] = seek_vertex.next
                    if seek_vertex.next:
                        seek_vertex.next.prev = seek_vertex.prev
                    break
                seek_vertex = seek_vertex.next

    def print_adj_list(self) -> None:
        for i in range(self._number_of_vertices):
            print(f"Neighbours of vertex {i}", end=": ")
            vertex_to_print = self._adj_list[i]
            if vertex_to_print is None:
                print("None")
            else:
                while vertex_to_print:
                    print(f"({vertex_to_print.vertex}, weight:{vertex_to_print.weight})", end="")
                    if vertex_to_print.next:
                        print(" -> ", end="")
                    vertex_to_print = vertex_to_print.next
                print("")

    def prim_mst(self, start_vertex: int = 0, print_mst: bool = False) -> [VertexElement]:
        mst_result = [None] * self._number_of_vertices
        vertices_in_MST = Stos()
        # priority_queue = HeapPriorityQueue()
        priority_queue = HeapPriorityQueue()

        vertices_in_MST.push(start_vertex)  # starting vertex in stack

        search_first_vertex: VertexElement = self._adj_list[start_vertex]  # Adding neighbours to pq

        while search_first_vertex is not None:
            priority_queue.push((start_vertex, search_first_vertex.vertex), search_first_vertex.weight)
            search_first_vertex = search_first_vertex.next

        while priority_queue.peek() is not None:

            edge, weight = priority_queue.pop()
            source_vertex: int = edge[0]
            destination_vertex: int = edge[1]

            # Jeśli wierzchołek nie został jeszcze odwiedzony
            from element_plik import Element
            search_vertex_in_MST: Element = vertices_in_MST.pierwszy_element
            already_exists = False
            for i in range(self._number_of_vertices):
                if search_vertex_in_MST is not None:
                    if destination_vertex == search_vertex_in_MST.dane:
                        already_exists = True
                        break
                    search_vertex_in_MST = search_vertex_in_MST.nastepny

            if already_exists:
                continue

            vertices_in_MST.push(destination_vertex)
            vertex_to_add = VertexElement(destination_vertex, weight)
            # print(f"{source_vertex} -> {destination_vertex} : {weight}")

            search_place_for_vertex: VertexElement = mst_result[source_vertex]
            if search_place_for_vertex is not None:
                while search_place_for_vertex.next is not None:
                    search_place_for_vertex = search_place_for_vertex.next
                search_place_for_vertex.next = vertex_to_add
            else:
                # search_place_for_vertex.next = vertex_to_add
                mst_result[source_vertex] = vertex_to_add

            search_place_for_destination: VertexElement = mst_result[destination_vertex]
            if search_place_for_destination is not None:
                while search_place_for_destination.next is not None:
                    search_place_for_destination = search_place_for_destination.next
                search_place_for_destination.next = VertexElement(source_vertex, weight)
            else:
                # search_place_for_vertex.next = vertex_to_add
                mst_result[destination_vertex] = VertexElement(source_vertex, weight)

            # Dodajemy do listy priorytetowej sąsiadów z wagami krawędzi
            search_vertex_in_destination: VertexElement = self._adj_list[destination_vertex]
            while search_vertex_in_destination is not None:
                search_vertex_in_MST: Element = vertices_in_MST.pierwszy_element
                already_exists = False
                for i in range(self._number_of_vertices):
                    if search_vertex_in_MST is not None:
                        if search_vertex_in_destination.vertex == search_vertex_in_MST.dane:
                            already_exists = True
                            search_vertex_in_destination = search_vertex_in_destination.next
                            break
                        search_vertex_in_MST = search_vertex_in_MST.nastepny

                if already_exists:
                    continue

                priority_queue.push((destination_vertex, search_vertex_in_destination.vertex),
                                    search_vertex_in_destination.weight)
                search_vertex_in_destination = search_vertex_in_destination.next
        if print_mst:
            for i in range(self._number_of_vertices):
                print(f"Neighbours of vertex {i}", end=": ")
                vertex_to_print = mst_result[i]
                if vertex_to_print is None:
                    print("None")
                else:
                    while vertex_to_print:
                        print(f"({vertex_to_print.vertex}, weight:{vertex_to_print.weight})", end="")
                        if vertex_to_print.next:
                            print(" -> ", end="")
                        vertex_to_print = vertex_to_print.next
                    print("")

        return mst_result

    def prims_mst_with_list(self, start_vertex: int = 0, print_mst: bool = False) -> [VertexElement]:
        mst_result = [None] * self._number_of_vertices

        vertices_in_MST: list[int] = []  # v

        priority_queue = HeapPriorityQueue()

        vertices_in_MST.append(start_vertex)

        search_first_vertex: VertexElement = self._adj_list[start_vertex]
        # Adding neighbours to pq
        while search_first_vertex is not None:  # V
            if search_first_vertex.vertex in vertices_in_MST:
                search_first_vertex = search_first_vertex.next
                continue
            priority_queue.push((start_vertex, search_first_vertex.vertex), search_first_vertex.weight)
            search_first_vertex = search_first_vertex.next

        while priority_queue.peek() is not None:  # V
            edge, weight = priority_queue.pop()
            source_vertex: int = edge[0]
            destination_vertex: int = edge[1]

            if destination_vertex in vertices_in_MST:
                continue

            vertices_in_MST.append(destination_vertex)

            vertex_to_add = VertexElement(destination_vertex, weight)
            # print(f"{source_vertex} -> {destination_vertex} : {weight}")

            search_place_for_vertex: VertexElement = mst_result[source_vertex]
            if search_place_for_vertex is not None:
                while search_place_for_vertex.next is not None:
                    search_place_for_vertex = search_place_for_vertex.next
                search_place_for_vertex.next = vertex_to_add
            else:
                # search_place_for_vertex.next = vertex_to_add
                mst_result[source_vertex] = vertex_to_add

            search_place_for_destination: VertexElement = mst_result[destination_vertex]
            if search_place_for_destination is not None:
                while search_place_for_destination.next is not None:
                    search_place_for_destination = search_place_for_destination.next
                search_place_for_destination.next = VertexElement(source_vertex, weight)
            else:
                # search_place_for_vertex.next = vertex_to_add
                mst_result[destination_vertex] = VertexElement(source_vertex, weight)

            # Dodajemy do listy priorytetowej sąsiadów z wagami krawędzi
            search_vertex_in_destination: VertexElement = self._adj_list[destination_vertex]
            while search_vertex_in_destination is not None:
                if search_vertex_in_destination.vertex in vertices_in_MST:
                    search_vertex_in_destination = search_vertex_in_destination.next
                    continue
                priority_queue.push((destination_vertex, search_vertex_in_destination.vertex),
                                    search_vertex_in_destination.weight)
                search_vertex_in_destination = search_vertex_in_destination.next
        if print_mst:
            for i in range(self._number_of_vertices):
                print(f"Neighbours of vertex {i}", end=": ")
                vertex_to_print = mst_result[i]
                if vertex_to_print is None:
                    print("None")
                else:
                    while vertex_to_print:
                        print(f"({vertex_to_print.vertex}, weight:{vertex_to_print.weight})", end="")
                        if vertex_to_print.next:
                            print(" -> ", end="")
                        vertex_to_print = vertex_to_print.next
                    print("")

        return mst_result
