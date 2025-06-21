# 作者:python11-刘杰
# 2025年06月02日14时23分47秒
# xxx@qq.com
# 家具类
class HouseItem:
    def __init__(self, name, area):
        self.name = name  # 家具名称
        self.area = area  # 占地面积

    def __str__(self):
        return f"{self.name} 占地 {self.area}平米"


# 房子类
class House:
    def __init__(self, house_type, total_area):
        self.house_type = house_type  # 户型
        self.total_area = total_area  # 总面积
        self.free_area = total_area  # 剩余面积
        self.item_list = []  # 家具列表

    def add_item(self, item):
        if item.area > self.free_area:
            print(f"无法添加 {item.name}，剩余面积不足")
        else:
            self.item_list.append(item.name)
            self.free_area -= item.area
            print(f"添加 {item.name} 成功，剩余面积：{self.free_area}平米")

    def __str__(self):
        return f"户型：{self.house_type}\n总面积：{self.total_area}\n剩余面积：{self.free_area}\n家具列表：{self.item_list}"


# 实例化
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

house = House("两室一厅", 60)
house.add_item(bed)  # 添加家具
house.add_item(table)
print(house)

print('-' * 50)


class Elephant:
    """大象类，封装跑步行为"""

    def __init__(self, name, weight):
        # 封装属性：名字和体重（外部无法直接修改）
        self.name = name
        self.weight = weight

    def run(self):
        """封装方法：跑步行为"""
        print(f"{self.name}正在跑步，消耗能量中...")
        self.weight -= 0.5  # 跑步后体重减少

    def eat(self):
        """封装方法：进食行为"""
        print(f"{self.name}需要补充能量，开始进食...")
        self.weight += 1  # 进食后体重增加

    def __str__(self):
        # 封装对象信息输出
        return f"大象【{self.name}】当前体重：{self.weight}公斤"


# 实例化测试
dumbo = Elephant("Dumbo", 100)
print(dumbo)  # 初始状态
dumbo.run()  # 调用封装方法
print(dumbo)  # 跑步后状态
dumbo.eat()  # 调用封装方法
print(dumbo)  # 进食后状态
buddy=Elephant("Buddy", 100)
print(buddy)
buddy.eat()
print(buddy)
buddy.eat()
