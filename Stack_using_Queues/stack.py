class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0


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
