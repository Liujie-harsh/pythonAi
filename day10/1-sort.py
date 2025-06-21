# 作者:python11-刘杰
# 2025年06月06日19时29分08秒
# xxx@qq.com

"""
这个程序演示了Python中不同的排序方法：
1. 使用sorted()函数对基本列表进行排序
2. 使用key参数对复杂数据结构（元组列表）进行排序
3. 使用key参数对自定义对象列表进行排序
"""

import random

# 生成包含10个1-99之间随机整数的列表
a = [random.randint(1, 99) for i in range(10)]
print("原始随机数列表:", a)

# 对列表进行降序排序（reverse=True表示降序）
b = sorted(a, reverse=True)
print("降序排序后的列表:", b)

# 创建一个包含学生信息的元组列表：(姓名, 年级, 年龄)
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
# 使用lambda函数按年龄(第3个元素，索引为2)对元组进行排序
print("按年龄排序的学生元组:", sorted(student_tuples, key=lambda x: x[2]))


class Student:
    """学生类，包含姓名、年级和年龄信息"""
    def __init__(self, name, grade, age):
        """初始化学生对象"""
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        """定义对象的字符串表示方式"""
        return repr((self.name, self.grade, self.age))


if __name__ == '__main__':
    # 创建Student对象列表
    student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
    ]
    # 使用lambda函数按姓名对学生对象进行排序
    c = sorted(student_objects, key=lambda student: student.name)
    print("按姓名排序的学生对象:", c)
