# 作者:python11-刘杰
# 2025年05月30日19时44分00秒
# xxx@qq.com
# 截取2~5位置的字符串
import copy

num_str = "0123456789"
print(num_str[2:6])
# 截取从 2 ~ 末尾的字符串
print(num_str[2:])
# 截取从 开始~ 5 位置 的字符串
print(num_str[:6])
# 截取完整的字符串
print(num_str)
# 从开始位置，每隔一个字符截取字符串
print(num_str[::2])
# 从索引 1 开始，每隔一个取一个
print(num_str[1::2])
# 截取从 2 ~ 末尾 - 1的字符串
print(num_str[2:-1])
# 截取字符串末尾两个字符
print(num_str[-2:])
# 字符串的逆序（面试题）
print(num_str[::-1])
# 使用zip组合下面两个元组，变为列表嵌套元组格式，与上课输出效果一致
a = (1, 2, 3)
b = ('a', 'b', 'c')
ziped = zip(a, b)
print(list(ziped))
# 使用enumerate把
# seasons = ['Spring', 'Summer', 'Fall', 'Winter'] 变为一个字典，效果和上课一致
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list1 = list(enumerate(seasons))
dict1 = {}
for i in list1:
    dict1[i[1]] = i[0]
print(dict1)
for i, season in enumerate(seasons, start=1):
    print(f"{i}:{season}")
print('-' * 100)
a = [1, 2, 3, 2, 4, 4]
b = [2, 3, 4]
print(list(set(a) & set(b)))
a.sort()
candidate = a[len(a) // 2]
if a.count(candidate) > len(a) // 2:
    print(candidate)
else:
    print(f"没有超过n/2的数")
print('-' * 100)
a = (1, 2, 3)
b = [2, 3, 4]
print(list(a) + list(b))
b.append(5)
b.insert(0, 1)
print(b)
print('-' * 100)
b.reverse()
print(b)
print(b[::-1].index(5))#查找列表切片后，元素5第一次出现的索引
from collections import Counter

print(Counter[True, False, 1, 2, 3])
a = [2, 3, 1, 5, 4, 7, 6]
print(sorted(a, reverse=True))
a = [1 if x > 5 else 0 for x in a]
print(a)
print('-' * 50)
odd = [x for x in b if x % 2 != 0]
even = [x for x in b if x % 2 == 0]
print(odd, even)
c = sorted([[1, 3], [6, 2], [3, 1]], key=lambda x: (x[0], x[1]))
print(c)
b[3:3] = ['x', 'y', 'z']
print(b)


d = {'Alice':20, 'Beth':18, 'Cecil':21}
list(d.keys())      # 23
list(d.values())    # 24
list(d.items())     # 25
print(list(d.values()), list(d.items()), list(d.keys()))
d.update({'David':19, 'Cecil':17})
print(d)
a1='David' in d  # False
a2='Alice' in d  # True
print(a1,a2)
d = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
for key, value in d.items():
    print(f"姓名: {key}, 年龄: {value}")
keys = ['A','B','C','D','E','F','G','H']
d1 = dict.fromkeys(keys, )
print(d1)
x, y, z = (1,2,3)
print(x,end='\n')
print(y,end='\n')
print(z,end='\n')
t = (2,5,3,7)
t=t[:2] + (9,) + t[2:]  # 输出：(2, 5, 9, 3, 7)
print(t)
s = 'blog.csdn.net/xufive/article/details/102946961'
print(s.split('/'))
s1 = "hello world"
print(s1.title())  # "Hello World"
s2 = "it's a book"
print(s2.title())  # "It'S A Book"（撇号后字母也被大写）
s3=[float(x.strip()) if '.' in x else int(x.strip()) for x in '2.722,  51, 73, 3.142'.split(',')]
print(s3)
s = 'adS12K56'
print(s.isalnum(), s.isdigit(), s.isalpha())
s = '\t python \n'
print(s)
print(s.rstrip())
for word in ['ok','hello','thank you']:
    print(f"|{word:<20}|{word:>15}|{word:^30}|")  # 左/右/居中对齐
