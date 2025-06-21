# 作者:python11-刘杰
# 2025年06月02日16时27分41秒
# xxx@qq.com
class MyClassa:
    _instance_count = 0  # 类变量统计总实例数
    _instances = {}  # 类变量记录每个实例

    def __init__(self, name):
        self.name = name
        MyClassa._instance_count += 1
        MyClassa._instances[name] = MyClassa._instances.get(name, 0) + 1

    @classmethod
    def get_most_frequent(cls):
        return max(cls._instances.items(), key=lambda x: x[1])


# 测试
obj1 = MyClassa("A")
obj2 = MyClassa("B")
obj3 = MyClassa("A")
obj4 = MyClassa("C")
obj5 = MyClassa("A")

print(f"总实例数: {MyClassa._instance_count}")  # 输出: 5
print("出现最多的实例:", MyClassa.get_most_frequent())  # 输出: ('A', 3)

"""
class MyClass:
    class_var = "类变量"

    @classmethod
    def class_method(cls, arg1):
        print(f"访问类变量: {cls.class_var}")
        return cls(arg1)  # 可作为工厂方法创建实例


# 直接通过类调用
MyClass.class_method("参数")
"""


class Animal:
    @classmethod
    def class_create(cls):
        return (cls)


class Dog(Animal):
    pass
dog=Dog.class_create()
print(dog)

class Animal:
    instance=None
    def speak(self): pass
    @classmethod
    def class_create(cls):
        if cls.instance is None:
            cls.instance =cls.__new__(cls)
        return cls.instance
class Dog(Animal):
    def speak(self): return "汪汪！"

class Cat(Animal):
    def speak(self): return "喵喵！"

def animal_sound(animal: Animal):
    print(animal.speak())  # 统一调用接口

animal_sound(Dog())  # 输出: 汪汪！
animal_sound(Cat())  # 输出: 喵喵！

print('-'*50)
class Singleton:
    _instance = None  # 类变量存储唯一实例

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)  # 调用父类__new__
        return cls._instance

    @classmethod
    def class_create(cls):
        """替代构造方法的类方法"""
        if cls._instance is None:
            cls._instance = cls()  # 触发__new__和__init__
        return cls._instance

# 测试
s1 = Singleton.class_create()
s2 = Singleton.class_create()
print(s1 is s2)  # 输出: True (确认是同一实例)