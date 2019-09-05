SLL = LinkedList()

SLL.add_to_head(1)
SLL.add_to_tail(2)
SLL.add_to_tail(3)
SLL.insert_after_node(2, 2.5)
# only node that remembers node2 is node1
node2:{
    value: 2,
    next: node2.5 },
node2.5: {
    value: 2.5,
    next: node3

}
{
head: node1: {
    value: 1,
    next: node2 },
tail: node3: {
    value: 3,
    next: None },
}

class LinkedList:
    __init__(self):
        self.head = None
        self.tail = None
    add_to_head(self, value):
    add_to_tail(self, value):
    insert_after_node(self, target_value, new_value):
    remove_from_tail(self):
