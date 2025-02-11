class MinHeap:
    def __init__(self):
        self.heap = []  # 使用列表存儲堆積

    def push(self, priority, task):
        """插入任務到堆積"""
        self.heap.append((priority, task))  # 先加入最後
        self._heapify_up(len(self.heap) - 1)  # 向上調整

    def pop(self):
        """取出優先級最高（最小）任務"""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]  # 取出根節點（最小值）
        self.heap[0] = self.heap.pop()  # 用最後一個節點替換根節點
        self._heapify_down(0)  # 向下調整
        return root

    def _heapify_up(self, index):
        """向上調整確保堆積性質"""
        parent = (index - 1) // 2 # 0
        while index > 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2


                  1
                 / \
                3   5
               / \   \
               7   9   6


    def _heapify_down(self, index):
        """向下調整確保堆積性質"""
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left
            if right < size and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def peek(self):
        """查看目前優先級最高的任務（不移除）"""
        return self.heap[0] if self.heap else None

    def is_empty(self):
        """檢查堆積是否為空"""
        return len(self.heap) == 0
