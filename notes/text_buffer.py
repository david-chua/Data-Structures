from doubly_linked_list import DoublyLinkedList

class TextBuffer:
    def __init__(self):
        self.contents = DoublyLinkedList()

    def append(self, char):
        self.contents.add_to_tail(char)

    def prepend(self, char):
        self.contents.add_to_head(char)

    def remove_from_end(self):
        self.contents.remove_from_tail()

    def remove_from_front(self):
        self.contents.remove_from_head()

    # check that this is an identical text buffer
    #join text buffer to end
    def join_text_buffers_to_end(self, other_buffer):
        self.contents.tail.next = other_buffer.contents.head
        other_buffer.contents.head.prev = self.contents.tail
        self.tail = other_buffer.contents.tail
        other_buffer.contents.head = self.contents.head

    # join text buffer to front
    def join_text_buffer_to_front(self, other_buffer):
        

    # put text buffer in the middle:
