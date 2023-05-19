class Node:
    def __init__(self, value, priority: int):
        self.value = value
        self.priority: int = priority
        self.prev: Node = None
        self.next: Node = None


class PriorityQueue:
    def __init__(self):
        self.head: Node = None

    def is_empty(self) -> bool:
        return self.head is None

    def push(self, value, priority) -> None:
        new_node = Node(value, priority)

        if self.is_empty():
            self.head = new_node
        else:
            current_node: Node = self.head
            while current_node is not None and current_node.priority < new_node.priority:
                current_node = current_node.next

            if current_node is None:
                last_node = self.head
                while last_node.next is not None:
                    last_node = last_node.next
                last_node.next = new_node
                new_node.prev = last_node
            else:
                new_node.prev = current_node.prev
                new_node.next = current_node
                if current_node.prev is not None:
                    current_node.prev.next = new_node
                else:
                    self.head = new_node
                current_node.prev = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Priority queue is empty")

        value = self.head.value
        priority = self.head.priority
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

        return value, priority

    def peek(self):
        if self.is_empty():
            return None
            raise Exception("Priority queue is empty")

        return self.head.value
