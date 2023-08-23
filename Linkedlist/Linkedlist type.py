# '''
# Delete : Deletes an element using the given key.
# '''

# class LinkedList:

#     class Node:
#         def __init__(self,data):
#             self.data = data
#             self.next = None

#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         newNode = self.Node(data)
#         if self.head is None:
#             self.head = newNode
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = newNode

#     def insertionAtBegining(self,data):
#         newNode = self.Node(data)
#         newNode.next = self.head
#         self.head = newNode

#     def dAB(self): # deletion at begining
#         if self.head:
#             self.head = self.head.next
#         else:
#             return("linked list is empty")

#     def displayLL(self):
#         current = self.head
#         while current:
#             print(current.data, end = "-->")
#             current = current.next
#         print("None")

#     def searching(self, key):
#         index = 0
#         temp = self.head
#         while temp:
#             if temp.data ==key:
#                 return index
#             temp = temp.next
#             index = index+1
#         return("ke not found")
    
#     def deletingByKey(self,key):
#         current = self.head

#         if current and current.data ==key:
#             self.head = current.next
#             current = None
#             return
        
#         previous = None
#         while current and current.data !=key:
#             previous = current
#             current = current.next

#         if current is None:
#             return
        
#         previous.next = current.next
#         current = None



# l = LinkedList()
# l.append("USA")
# l.append("India")
# l.append("Nepal")
# l.append("UK")
# l.insertionAtBegining("Kothaguda")
# # print(l.dAB())

# print(l.searching("Nepal"))
# # l.displayLL()


# l.displayLL()
#---------------------------------------------------------
#difference between array an linked array

# Using arrays
# my_array = [10, 20, 30, 40, 50]

# # Accessing elements
# print(my_array[2])  # Output: 30

# # Inserting elements
# my_array.insert(2, 25)  # Inserts 25 at index 2
# print(my_array)

# # Deleting elements
# my_array.pop(3)  # Removes element at index 3
# print(my_array)
#------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Using linked lists
my_linked_list = LinkedList()
my_linked_list.insert(50)
my_linked_list.insert(30)
my_linked_list.insert(10)
my_linked_list.display()  # Output: 10 -> 30 -> 50 -> None
