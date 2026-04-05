class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.items = None

    def push(self, item):
        self.items = Node(item, self.items)

    def pop(self):
        if self.items is None:
            raise IndexError("pop from empty queue")

        node = self.items
        if node.next is None:
            self.items = None
            return node.data
        if node.next.next is None:
            res = node.next.data
            self.items.next = None
            return res

        while node.next.next is not None:
            node = node.next
        res = node.next.data
        node.next = None
        return res

    def size(self):
        k = 0
        node = self.items
        while node is not None:
            node = node.next
            k += 1
        return k

    def is_empty(self):
        return self.size() == 0


# def test_queue():
#     q = Queue()
#     q.push(1)
#     q.push(2)
#     q.push(3)
#     assert q.pop() == 1
#     assert q.pop() == 2
#     assert q.pop() == 3
#     try:
#         q.pop()
#     except IndexError:
#         pass
#     else:
#         assert False, "Expected IndexError"

#     assert q.size() == 0
#     assert q.is_empty()
#     q.push(4)
#     assert q.size() == 1
#     assert not q.is_empty()


# test_queue()


class MyStack(object):
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.push(x)

    def pop(self):
        """
        :rtype: int
        """
        for _ in range(self.q1.size() - 1):
            self.q2.push(self.q1.pop())
        res = self.q1.pop()
        for _ in range(self.q2.size()):
            self.q1.push(self.q2.pop())
        return res

    def top(self):
        """
        :rtype: int
        """
        for _ in range(self.q1.size() - 1):
            self.q2.push(self.q1.pop())
        res = self.q1.pop()
        for _ in range(self.q2.size()):
            self.q1.push(self.q2.pop())
        self.q1.push(res)
        return res

    def empty(self):
        """
        :rtype: bool
        """
        return self.q1.is_empty() and self.q2.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
