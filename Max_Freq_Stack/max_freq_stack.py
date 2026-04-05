class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class FreqStack(object):
    def __init__(self):
        self.items = None
        self.freq = {}

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.items = Node(val, self.items)
        self.freq[val] = self.freq.get(val, 0) + 1

    def pop(self):
        """
        :rtype: int
        """
        try:
            if self.items.next is None:
                res = self.items.val
                self.items = None
                self.freq[res] = self.freq.get(res, 0) - 1
                return res
        except AttributeError:
            raise IndexError("pop from empty stack")
        node = self.items
        max_freq = max(self.freq.values())
        maxes = [k for k, v in self.freq.items() if v == max_freq]
        if node.val not in maxes:
            while node.next.val not in maxes:
                node = node.next
            res = node.next.val
            node.next = node.next.next
        else:
            res = node.val
            self.items = node.next
        self.freq[res] -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()


# def test():
#     # ["FreqStack","push","push","push","push","push","push","pop","push","pop","push","pop","push","pop","push","pop","pop","pop","pop","pop","pop"]
#     # [[],[4],[0],[9],[3],[4],[2],[],[6],[],[1],[],[1],[],[4],[],[],[],[],[],[]]
#     # Output
#     # [null,null,null,null,null,null,null,4,null,2,null,6,null,1,null,4,1,3,9,0,4]
#     s = FreqStack()
#     s.push(4)  # 4 -> None
#     s.push(0)  # 0 -> 4 -> None
#     s.push(9)  # 9 -> 0 -> 4 -> None
#     s.push(3)  # 3 -> 9 -> 0 -> 4 -> None
#     s.push(4)  # 4 -> 3 -> 9 -> 0 -> 4 -> None
#     s.push(2)  # 2 -> 4 -> 3 -> 9 -> 0 -> 4 -> None
#     assert s.pop() == 4  # 2 -> 3 -> 9 -> 0 -> 4 -> None
#     s.push(6)  # 6 -> 2 -> 3 -> 9 -> 0 -> 4 -> None
#     assert s.pop() == 6  # 2 -> 3 -> 9 -> 0 -> 4 -> None
#     s.push(1)  # 1 -> 2 -> 3 -> 9 -> 0 -> 4 -> None
#     assert s.pop() == 1  # 2 -> 3 -> 9 -> 0 -> 4 -> None
#     s.push(1)  # 1 -> 2 -> 3 -> 9 -> 0 -> 4 -> None
#     assert s.pop() == 1  # 2 -> 3 -> 9 -> 0 -> 4 -> None
#     s.push(4)  # 4 -> 2 -> 3 -> 9 -> 0 -> 4 -> None
#     assert s.pop() == 4  # 2 -> 3 -> 9 -> 0 -> 4 -> None
#     assert s.pop() == 3  # 2 -> 9 -> 0 -> 4 -> None
#     assert s.pop() == 9
#     assert s.pop() == 0
#     assert s.pop() == 4


# test()
