# 作者:python11-刘杰
# 2025年06月05日09时20分46秒
# xxx@qq.com
import random


class Sort:
    def __init__(self, arr_len):
        self.arr = []
        self.arr_len = arr_len
        self.arr_random()  # 初始化时生成随机数组

    def arr_random(self):
        # 生成指定长度的随机数组，元素范围为0~99
        self.arr = [random.randint(0, 99) for _ in range(self.arr_len)]

    def bubble(self):
        # 冒泡排序
        arr = self.arr
        for i in range(self.arr_len - 1, 0, -1):  # 从后往前遍历
            for j in range(i):  # 每次冒出一个最大值到未排序部分的末尾
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 交换相邻元素

    def selection(self):
        # 选择排序
        arr = self.arr
        for i in range(self.arr_len):
            min_index = i  # 假设当前位置是最小值
            for j in range(i + 1, self.arr_len):  # 在未排序区寻找更小的值
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]  # 将最小值放到已排序末尾

    def insertion(self):
        # 插入排序
        arr = self.arr
        for i in range(1, self.arr_len):
            key = arr[i]  # 当前要插入的元素
            j = i - 1
            while j >= 0 and arr[j] > key:  # 向左寻找合适位置
                arr[j + 1] = arr[j]  # 元素右移
                j -= 1
            arr[j + 1] = key  # 插入元素

    def shell(self):
        # 层次插入排序（Shell Sort）
        arr = self.arr
        n = self.arr_len
        gap = n // 2  # 初始gap为数组长度的一半

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]  # 间隔比较并移动
                    j -= gap
                arr[j] = temp  # 插入元素
            gap //= 2  # 缩小gap

    def quick_sort(self):
        # 快速排序
        def _quick_sort(arr, low, high):
            if low < high:
                pivot_index = partition(arr, low, high)  # 分区
                _quick_sort(arr, low, pivot_index - 1)  # 排序左区
                _quick_sort(arr, pivot_index + 1, high)  # 排序右区

        def partition(arr, low, high):
            pivot = arr[high]  # 选择初始进分置点
            i = low - 1

            for j in range(low, high):  # 将比较结果排序
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]  # 小于pivot的置于左侧
            arr[i + 1], arr[high] = arr[high], arr[i + 1]  # 把pivot移到分界点
            return i + 1

        _quick_sort(self.arr, 0, self.arr_len - 1)

    def heap_sort(self):
        # 堆排序
        arr = self.arr
        n = self.arr_len

        def heapify(n, i):
            largest = i  # 假设根节点最大
            left = 2 * i + 1  # 左子节点
            right = 2 * i + 2  # 右子节点

            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]  # 交换如果子节点更大
                heapify(n, largest)  # 继续调整子堆

        # 构造大顶堆
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        # 将堆顶元素放到末尾，重复调整
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]  # 交换堆顶到末尾
            heapify(i, 0)  # 重新调整前面的堆

if __name__ == '__main__':
    # 原始数组
    my_sort = Sort(10)
    print(my_sort.arr)

    # 冒泡排序
    # my_sort.bubble()
    # print("冒泡排序:", my_sort.arr)


    # 选择排序
    # my_sort.selection()
    # print("选择排序:", my_sort.arr)

    # 插入排序
    # my_sort.insertion()
    # print("插入排序:", my_sort.arr)

    # my_sort.shell()
    # print("希尔排序:", my_sort.arr)

    my_sort.heap_sort()
    print(my_sort.arr)

