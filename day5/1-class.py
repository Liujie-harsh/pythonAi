# 作者:python11-刘杰
# 2025年06月01日17时11分10秒
# xxx@qq.com
class Elephant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f'大象的名字叫{self.name} ，今年{self.age}岁了，体重为 {self.height + 100}kg'


elephant = Elephant('Bob', 20, 100)
print(elephant.__str__())


class Tiger:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f'我叫{self.name},今年{self.age},体重{self.height + 100}kg'

    def __repr__(self):
        return f'我最喜欢吃东西了'


tiger = Tiger('candy', 7, 70)
print(tiger.__str__(), tiger.__repr__())


class Dog:
    color = '黄色'
    name = '大黄'

    def like(s):
        if 1:
            print('wangwang!')
        else:
            print('摇尾巴！')


dog = Dog
print(dog.color, dog.name)
dog.like(1)


class Dog:
    def __init__(self):
        # 固定属性：黄色、名字叫大黄
        self.color = '黄色'
        self.name = '大黄'

    def react(self, is_stranger):
        """根据是否生人触发不同行为"""
        if is_stranger:
            print("汪汪叫！")
        else:
            print("摇尾巴！")


# 创建实例
dog = Dog()

# 打印属性
print(f"狗狗颜色：{dog.color}, 名字：{dog.name}")

# 调用方法（生人触发汪汪叫）
dog.react(is_stranger=True)  # 输出：汪汪叫！
dog.react(is_stranger=False)  # 输出：摇尾巴！
s = 'hello'
print(dir(s))


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"


p = Person("Alice")
print(dir(p))  # 包含'name', 'greet'及默认方法（如'__class__'）
print(p.greet())


class Cat:
    def eat(self):
        return f'我最爱吃鱼啦！'

    def drink(self):
        return f'到喝水时间了'
cat = Cat()
print(cat.eat())
print(cat.drink())