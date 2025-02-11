#新增任務
#刪除任務
#ui設計
#查詢任務
#社群系統
#
#任務管理使用堆堆踐演算法
class TaskManager:
    def __init__(self):
        self.heap = []

    def taks_list(list):
        pass

    # append task
    def push_task(self, tasknum, task):
        self.heap.append((tasknum, task))
        self.task_up(len(self.heap) - 1)

    def pop_task(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop() # [0, 1] -> pop(1) 
        

        root = self.heap[0]# [0, 1] [0]
        self.heap[0] = self.heap.pop()# [0] = [1]
        self.task_down(0)
        return root#pop拿掉頭部會造成二元數不符合規範 必須向下整理

    def task_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def task_down(self, index):
        size = len(self.heap)
        while True:#確保二元數抱持左節點小於右節點
            left = 2 * index + 1 #二元樹
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


task_manager = TaskManager()

# 加入任務（數字越小，優先級越高）
task_manager.push_task(3, "寫作業")
task_manager.push_task(2, "買東西")
task_manager.push_task(1, "準備考試")
print(task_manager.heap)


# 取出優先級最高的任務
print(task_manager.pop_task())  # (1, "準備考試")
print(task_manager.pop_task())  # (2, "買東西")
print(task_manager.pop_task())  # (3, "寫作業")