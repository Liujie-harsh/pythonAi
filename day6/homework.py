# 作者:python11-刘杰
# 2025年06月02日17时44分19秒
# xxx@qq.com
# def func(*args):
#     return sum(args)
#
#
# a= func(1, 2, 3, 4)
# print(a)

def func1(*args, **kwargs):
    print(args)
    print(kwargs)
    return '成功'


# a= func1(1, 2, 3, 4,name='xiaoming',age=19)
# print(a)
numbers = (2, 3, 4)
info = {'name': 'xiaowang', 'age': 17}
func1(*numbers)
func1(**info)


class MusicPlayer:
    instance = None  # 类属性存储唯一实例

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)  # 首次创建实例
        return cls.instance  # 始终返回同一实例

    def __init__(self):
        print('音乐播放器初始化')


print(MusicPlayer.instance)
player = MusicPlayer()
print(MusicPlayer.instance)


class Animal(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"我叫{self.name}, 我的颜色是{self.color}"

    def bark(self):
        return "汪汪！"

    def shark(self):
        return "摇尾巴！"


dog = Animal('小黄', '黄色')
print(dog)
print(dog.shark())
print(dog.bark())


class Elephant(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"我叫{self.name}"

    def run(self):
        self.weight -= 0.5
        return f"我喜欢跑步，马上去跑步咯"

    def eat(self):
        self.weight += 1
        return f"我要开始吃饭咯"


elephant = Elephant('小飞象', 70)
print(elephant)
print(elephant.weight)
print(elephant.eat())
print(elephant.weight)
print(elephant.run())
print(elephant.weight)


class Person(object):
    def __init__(self, name):
        self.name = name
        self.age = 18

    def __Age(self):
        return 18
    # def __scart(self):
    #     return self.__Age()


xiaowang = Person('xiaowang')
print(xiaowang.name)
print(xiaowang.age)


class Animal(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def __str__(self):
        return f"我叫{self.name},我的颜色{self.color}"

class Dog(Animal):
    def bark(self):
        return f"汪汪！"

class Cat(Animal):
    def bark(self):
        return f"喵喵！"
xiaohuang=Dog('小黄','黄色')
print(xiaohuang.bark(),xiaohuang.__str__())
doudou=Cat('豆豆','黑色')
print(doudou.bark(),doudou.__str__())

class Singleton:
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
print(Singleton.instance)
s1=Singleton()
print(s1.instance)
s2=Singleton()
print(s2.instance)
print(s1 is s2)