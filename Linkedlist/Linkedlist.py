# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         newNode = Node(data)
#         if self.head is None:
#             self.head = newNode
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = newNode

#     def displayLL(self):
#         current = self.head
#         while current:
#             print(current.data, end = ", ")
#             current = current.next
#         print("None")


# l = LinkedList()
# l.append("USA")
# l.append("India")
# l.append("Nepal")
# l.append("UK")


# l.displayLL()
#---------------------------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Creating a linked list and appending elements
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# Displaying the linked list
linked_list.display()
  