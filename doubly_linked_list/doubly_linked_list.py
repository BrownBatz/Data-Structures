"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        newNode = ListNode(value)

        if self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.length += 1
            return
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return
        else:
            newHead = self.head.next
            self.head = newHead
            newHead.prev = None
            self.length = self.length - 1
            return
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        newNode = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode
            self.length = self.length + 1
            return
        else:
            oldTail = self.tail
            oldTail.next = newNode
            self.tail = newNode
            self.length = self.length + 1
            return
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return
        elif self.length == 1:
            oldTail = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return oldTail.value
        else:
            oldTail = self.tail
            newTail = self.tail.prev
            newTail.next = None
            self.tail = newTail
            self.length -= 1
            return oldTail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head is None and self.tail is None:
            return
        
        rightRef = node.next
        leftRef = node.prev

        leftRef.next = rightRef
        righRef.prev = leftRef

        node.next = None
        node.prev = None

        oldHead = self.head
        oldHeadprev = node

        self.head = node
        self.head.next = oldHead
        return
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.head is None and self.tail is None:
            return
        
        rightRef = node.next
        leftRef = node.prev

        leftRef.next = rightRef
        rightRef.prev = leftRef

        node.next = None
        node.prev = None

        oldTail = self.tail
        oldTail.next = node

        self.tail = node
        self.tail.prev = oldTail
        return

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None and self.tail is None:
            return
        
        rightRef = node.next
        leftRef = node.prev
        
        leftRef.next = rightRef
        rightRef.prev = leftRef

        node.next = None
        node.prev = None

        node = None
        return

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current = self.head
        currentMax = current.value
        while(current.next is not None):
            nextNode = current.next
            if (nextNode.value > currentMax):
                currentMax = nextNode.value
                current = nextNode
                continue
            else:
                current = nextNode
                continue
        return currentMax