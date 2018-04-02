'''
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.

'''
# To implement: Make current node a copy of next node and skip over next node.

def deleteNode(node):
    # Copy value of next node to this node
    node.value = node.next.value
    # Point this node to the node after next node
    node.next = node.next.next