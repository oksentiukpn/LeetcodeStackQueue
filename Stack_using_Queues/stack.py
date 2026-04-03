from queue import Queue


class MyStack(object):
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.put(x)

    def pop(self):
        """
        :rtype: int
        """
        for i in range(self.q1.qsize() - 1):
            self.q2.put(self.q1.get())
        res = self.q1.get()
        for i in range(self.q2.qsize()):
            self.q1.put(self.q2.get())
        return res

    def top(self):
        """
        :rtype: int
        """
        for i in range(self.q1.qsize() - 1):
            self.q2.put(self.q1.get())
        res = self.q1.get()
        for i in range(self.q2.qsize()):
            self.q1.put(self.q2.get())
        self.q1.put(res)
        return res

    def empty(self):
        """
        :rtype: bool
        """
        return self.q1.empty() and self.q2.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
