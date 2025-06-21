# 作者:python11-刘杰
# 2025年06月04日16时17分08秒
# xxx@qq.com
import random


class Sort:
    def __init__(self, arr_len):
        self.arr = []
        self.arr_len = arr_len
        self.arr_random()

#生成 self.arr_len 个范围在 [0, 99] 的随机整数，存入 self.arr。
    def arr_random(self):
        for i in range(self.arr_len):
            self.arr.append(random.randint(0, 99))

    def bubble(self):
        arr = self.arr
        for i in range(self.arr_len - 1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    my_sort = Sort(10)
    print(my_sort.arr)
    my_sort.bubble()
    print(my_sort.arr)
