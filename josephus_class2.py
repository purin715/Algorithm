# 7 3
# <3, 6, 2, 7, 5, 1, 4>

n, k = map(int, input().split())

# 1. array
# n_list = list(range(1, n+1)) # [i for i in range(1, n+1)]

# i = k-1

# print("<", end="")

# while len(n_list) > 1:
#     print(n_list.pop(i), end=", ")
#     i = (i + k-1) % len(n_list)

# print(f"{n_list[0]}>")

# 2. deque
# from collections import deque
# n_list = deque(range(1, n+1))

# result_str = "<"

# while len(n_list) > 0:
#     n_list.rotate(-(k-1))
#     result_str += f"{n_list.popleft()}, "

# print(result_str.rstrip(", ") + ">")

# 3. linked_list

class LinkedList:
    class Node:
        def __init__(self, value, ref=None):
            self.value = value
            self.next_node = ref

    def __init__(self):
        self.size = 0
        self.start_node = None
        self.end_node = None

    def empty(self):
        return self.size == 0

    def append(self, value):
        new_node = self.Node(value)

        if self.empty():
            self.start_node = new_node
            new_node.next_node = new_node 
        else:
            new_node.next_node = self.end_node.next_node
            self.end_node.next_node = new_node
    
        self.end_node = new_node
        self.size += 1

    def pop(self, before_target_node):
        if not self.empty():
            target_node = before_target_node.next_node
            before_target_node.next_node = target_node.next_node

            if target_node == self.start_node:
                self.start_node = target_node.next_node
            if target_node == self.end_node:
                self.end_node = before_target_node
            
            self.size -= 1

            if self.empty():
                self.start_node = None
                self.end_node = None

            return target_node.value

l_list = LinkedList()
for i in range(1, n+1):
    l_list.append(i)

# TODO