class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        self.head = Node(item, self.head)

    def pop(self, i=0):
        h = self.head
        while i:
            try:
                h = h.next
            except AttributeError:
                raise IndexError("Or empty stack, or too high index")
            i -= 1
        try:
            res = self.head.val
            self.head = self.head.next
        except AttributeError:
            raise TypeError("Empty stack!")

        return res

    def peek(self):
        try:
            return self.head.val
        except AttributeError:
            raise TypeError("Empty stack!")

    def is_empty(self):
        return self.head is None


class MyQueue(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.push(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack1.is_empty() and self.stack2.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())
print(q.pop())
print(MyQueue().empty())
