class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        cur = self.head
        for i in range(index):
            if cur:
                cur = cur.next
            else: 
                return -1

        if cur:
            return cur.val
        else:
            return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node

    def remove(self, index: int) -> bool:
        cur = self.head
        if not cur:
            return False
        if index == 0:
            self.head = cur.next
            return True
        for i in range(index-1):
            cur = cur.next
        if not cur:
            return False
        if cur.next:
            cur.next = cur.next.next
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        values = []
        cur = self.head
        if cur:
            values.append(cur.val)
        else:
            return []
        while cur.next:
            cur = cur.next
            values.append(cur.val)
            
        
        return values
