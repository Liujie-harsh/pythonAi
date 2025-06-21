# 作者:python11-刘杰
# 2025年06月02日15时38分31秒
# xxx@qq.com
class Animal:
    """基类：动物"""

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("子类必须实现此方法")


class Runner:
    """混入类：跑步能力"""

    def run(self):
        print(f"{self.name} 正在快速奔跑！")


class Elephant(Animal, Runner):  # 多继承
    """子类：大象（继承Animal和Runner）"""

    def __init__(self, name, weight):
        super().__init__(name)  # 调用父类构造方法
        self.weight = weight

    # 方法重写（Override）
    def speak(self):
        print(f"{self.name} 发出喇叭声：嘟嘟！")

    # 扩展新方法
    def spray_water(self):
        print(f"{self.name} 用鼻子喷水")


class BabyElephant(Elephant):
    """孙子类：小象（继承Elephant）"""

    def speak(self):  # 再次重写方法
        print(f"{self.name} 发出稚嫩的叫声：吱吱~")

    def play(self):
        print(f"{self.weight}公斤的小象在泥坑里打滚")


# 实例化测试
if __name__ == '__main__':
    dumbo = Elephant("Dumbo", 500)
    dumbo.speak()  # 输出: Dumbo 发出喇叭声：嘟嘟！
    dumbo.run()  # 输出: Dumbo 正在快速奔跑！
    dumbo.spray_water()  # 输出: Dumbo 用鼻子喷水

    baby = BabyElephant("小飞象", 200)
    baby.speak()  # 输出: 小飞象 发出稚嫩的叫声：吱吱~
    baby.play()  # 输出: 200公斤的小象在泥坑里打滚
    buddy = Elephant('buddy', 200)
    buddy.speak()
    buddy.spray_water()
    buddy.run()
    print(buddy.name, buddy.weight,f'kg')
