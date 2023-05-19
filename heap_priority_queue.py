class HeapPriorityQueue:
    def __init__(self):
        self.heap = []
        self.size = 0

    def __is_empty(self) -> bool:
        return self.size == 0

    @staticmethod
    def __get_parent_index(index: int) -> int:
        return (index - 1) // 2

    @staticmethod
    def __get_left_child_index(index: int) -> int:
        return (2 * index) + 1

    @staticmethod
    def __get_right_child_index(index: int) -> int:
        return (2 * index) + 2

    def __has_parent(self, index: int) -> bool:
        return self.__get_parent_index(index) >= 0

    def __has_left_child(self, index: int) -> bool:
        return self.__get_left_child_index(index) < self.size

    def __has_right_child(self, index: int) -> bool:
        return self.__get_right_child_index(index) < self.size

    def __swap(self, index_1: int, index_2: int) -> None:
        self.heap[index_1], self.heap[index_2] = self.heap[index_2], self.heap[index_1]

    def heapify_up(self, index: int) -> None:
        while self.__has_parent(index) and self.heap[index][1] < self.heap[self.__get_parent_index(index)][1]:
            parent_index = self.__get_parent_index(index)
            self.__swap(index, parent_index)
            index = parent_index

    def heapify_down(self, index: int) -> None:
        while self.__has_left_child(index):
            smallest_child_index = self.__get_left_child_index(index)

            if self.__has_right_child(index) and self.heap[self.__get_right_child_index(index)][1] < self.heap[smallest_child_index][1]:
                smallest_child_index = self.__get_right_child_index(index)

            if self.heap[index][1] < self.heap[smallest_child_index][1]:
                break

            self.__swap(index, smallest_child_index)
            index = smallest_child_index

    def push(self, value: int, priority: int) -> None:
        element = (value, priority)
        self.heap.append(element)
        self.size += 1
        self.heapify_up(self.size - 1)

    def pop(self) -> tuple:
        if self.__is_empty():
            raise IndexError("Priority queue is empty")

        root = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heap.pop()  # return maybe (0) if needed
        self.heapify_down(0)

        return root

    def peek(self) -> tuple:
        if self.__is_empty():
            return None
            raise IndexError("Priority queue is empty")

        return self.heap[0]
