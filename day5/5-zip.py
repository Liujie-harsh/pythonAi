# 作者:python11-刘杰
# 2025年05月30日19时36分59秒
# xxx@qq.com
names = ['小明', '小红', '小华']
scores = [95, 88, 92]
zipped = zip(names, scores)
print(list(zipped))
print('-' * 100)
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]
print(list(zip(list1, list2, list3)))
print('-' * 100)
keys = ['name', 'age']
values = ['Alice', 30]
dict_from_zip = dict(zip(keys, values))
print(dict_from_zip)
print('-' * 100)
for name, score in zip(names, scores):
    print(f"{name}: {score}")
print('-' * 100)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = list(zip(*matrix))
print(transposed)
print('-' * 50)
a = (1, 2, 3)
b = [2, 3, 4]
print(list(a) + list(b))
print(b[::-1].index(4))
c = sorted([[1, 3], [6, 2], [3, 1]], key=lambda x: (x[0], x[1]))
t = (2, 5, 3, 7)
t = t[:2] + (2, 1, 9) + t[2:]  # 输出：(2, 5, 9, 3, 7)
print(t)
print(max(t))
print(min(t))
str1 = 'hello world'
print(str1 * 4)
str1 = "hello python"
str2 = '我的外号是"大西瓜"'
print(str2)
print(str1[6])
for char in str2:
    print(char)
poem_str = "登鹳雀楼\t 王之涣 \t 白日依山尽 \t \n 黄河入海流 \t\t 欲穷千里目\t\t\n更上一层楼"
print(poem_str)
# 1. 拆分字符串
poem_list = poem_str.split()
print(poem_list)
# 2. 合并字符串
result = " ".join(poem_list)
print(result)
title, author = poem_list[0], poem_list[1]
lines = poem_list[2:]  # 诗句列表：['白日依山尽', '黄河入海流', '欲穷千里目', '更上一层楼']
centered_poem = "\n".join(line.center(20) for line in [title, author] + lines)
print(centered_poem)


def demo(num, num_list):
    print("函数内部")
    # 赋值语句
    num = 200
    num_list = [1, 2, 3]
    print(num)
    print(num_list)
    print("函数代码完成")


gl_num = 99
gl_list = [4, 5, 6]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
