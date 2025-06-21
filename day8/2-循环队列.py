# 作者:python11-刘杰
# 2025年06月04日15时26分50秒
# xxx@qq.com
class CircleQueue:
    def __init__(self, maxsize):
        self.queue = [0] * maxsize
        self.maxsize = maxsize
        self.front = self.rear = 0

    def enqueue(self, element):
        if (self.rear + 1) % self.maxsize == 0:
            print("队满了")
            return False
        else:
            self.queue[self.rear] = element
            self.rear = (self.rear + 1) % self.maxsize
            return True

    def dequeue(self):
        if self.front == self.rear:
            print("队空")
            return False
        else:
            element = self.queue[self.front]
            self.front = (self.front + 1) % self.maxsize
            return element

    def print_queue(self):
        if self.front == self.rear:
            print("队空")
            return False
        print("当前队列中的元素:", end=" ")
        i = self.front
        while i != self.rear:
            print(self.queue[i], end=" ")
            i = (i + 1) % self.maxsize
        print()


if __name__ == '__main__':
    queue = CircleQueue(5)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue.dequeue())
    print(queue.dequeue())
    queue.print_queue()
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    queue.enqueue(9)
    queue.print_queue()
