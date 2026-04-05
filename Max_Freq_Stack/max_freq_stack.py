class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class FreqStack(object):
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.maxfreq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freq[val] = self.freq.get(val, 0) + 1
        if self.freq[val] > self.maxfreq:
            self.maxfreq = self.freq[val]

        head = self.group.get(self.freq[val], None)
        self.group[self.freq[val]] = Node(val, head)

    def pop(self):
        """
        :rtype: int
        """
        if self.maxfreq == 0:
            raise IndexError("pop from empty stack")

        head = self.group[self.maxfreq]
        val = head.val
        self.group[self.maxfreq] = head.next

        new_freq = self.freq[val] - 1
        if new_freq == 0:
            del self.freq[val]
        else:
            self.freq[val] = new_freq

        if self.group[self.maxfreq] is None:
            del self.group[self.maxfreq]
            self.maxfreq -= 1
        return val


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
#     assert s.pop() == 2  # 3 -> 9 -> 0 -> 4 -> None
#     assert s.pop() == 3  # 9 -> 0 -> 4 -> None
#     assert s.pop() == 9 # 0 -> 4 -> None
#     assert s.pop() == 0 # 4 -> None
#     assert s.pop() == 4 # None


# test()
