from priority_queue import PriorityQueue
from heap_priority_queue import HeapPriorityQueue
from stos import Stos


class GraphAdjacencyDict:
    def __init__(self, number_of_vertices: int, is_directed: bool = False):
        self._is_directed: bool = is_directed
        self._number_of_vertices: int = number_of_vertices
        self._adj_dict: dict[dict] = {}

    def add_edge(self, source_vertex: int, destination_vertex: int, weight=1) -> None:

        if source_vertex not in self._adj_dict:
            self._number_of_vertices += 1
            self._adj_dict[source_vertex] = {}
        if destination_vertex in self._adj_dict[source_vertex]:
            return None
        self._adj_dict[source_vertex][destination_vertex] = weight

        if not self._is_directed:
            if destination_vertex not in self._adj_dict:
                self._adj_dict[destination_vertex] = {}
            self._adj_dict[destination_vertex][source_vertex] = weight

    def is_edge(self, source_vertex: int, destination_vertex: int) -> bool:
        if source_vertex in self._adj_dict:
            if destination_vertex in self._adj_dict[source_vertex]:
                return True
        return False

    def remove_edge(self, source_vertex: int, destination_vertex: int) -> None:
        if not self.is_edge(source_vertex, destination_vertex):
            print(f"There is no edge to remove between {source_vertex} and {destination_vertex}")
            return None
        del self._adj_dict[source_vertex]

        if not self._is_directed:
            del self._adj_dict[destination_vertex]

    def print_adj_dict(self) -> None:

        for source_vertex in self._adj_dict:
            print(f"Neighbours of vertex {source_vertex}", end=": ")
            for destination_vertex in self._adj_dict[source_vertex]:
                print(f"({destination_vertex}, weight:{self._adj_dict[source_vertex][destination_vertex]})", end="")
                print(" -> ", end="")
            print("")

    def prim_mst_dict(self, start_vertex: int = 0, print_mst: bool = False) -> dict[dict]:

        priority_queue = HeapPriorityQueue()
        vertices_in_MST = Stos()
        mst_result: dict[dict] = {}

        vertices_in_MST.push(start_vertex)

        for destination_vertex in self._adj_dict[start_vertex]:
            priority_queue.push((start_vertex, destination_vertex), self._adj_dict[start_vertex][destination_vertex])

        while priority_queue.peek() is not None:
            edge, weight = priority_queue.pop()
            source_vertex, destination_vertex = edge[0], edge[1]

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

            # Adding edge to mst_result
            if source_vertex not in mst_result:
                mst_result[source_vertex] = {}
            mst_result[source_vertex][destination_vertex] = weight
            if not self._is_directed:
                if destination_vertex not in mst_result:
                    mst_result[destination_vertex] = {}
                mst_result[destination_vertex][source_vertex] = weight

            for search_destination_vertex in self._adj_dict[destination_vertex]:

                search_vertex_in_MST: Element = vertices_in_MST.pierwszy_element
                already_exists = False
                while search_vertex_in_MST is not None:
                    if search_vertex_in_MST is not None:
                        if search_destination_vertex == search_vertex_in_MST.dane:
                            already_exists = True
                            break
                        search_vertex_in_MST = search_vertex_in_MST.nastepny

                if already_exists:
                    continue

                priority_queue.push((destination_vertex, search_destination_vertex),
                                    self._adj_dict[destination_vertex][search_destination_vertex])

        if print_mst:
            print(f"Mst with Dictionaries")
            for source_vertex in mst_result:
                print(f"Neighbours of vertex {source_vertex}", end=": ")
                for destination_vertex in mst_result[source_vertex]:
                    print(f"({destination_vertex}, weight:{mst_result[source_vertex][destination_vertex]})", end="")
                    print(" -> ", end="")
                print("")

        return mst_result

