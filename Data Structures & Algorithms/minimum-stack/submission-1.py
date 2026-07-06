class MinStack:

    def __init__(self):
        self.arr = []
        self.mini = float('inf')
        # self.topo = -float('inf')
    def push(self, val: int) -> None:
        self.arr.append(val)
        if val < self.mini: self.mini = val
        # if val > self.topo: self.topo = val
    def pop(self) -> None:
        temp = self.arr.pop()
        if temp == self.mini:
            self.mini = float('inf')
            for i in self.arr:
                if i < self.mini:
                    self.mini = i
        # if temp == self.topo:
        #     self.topo = -float('inf')
        #     for i in self.arr:
        #         if i > self.topo:
        #             self.topo = i
    def top(self) -> int:
        # return int(self.topo)
        return self.arr[-1]

    def getMin(self) -> int:
        return int(self.mini)
