# 作者:python11-刘杰
# 2025年05月30日14时13分32秒
# xxx@qq.com
xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75}
print(xiaoming['age'])
print(xiaoming)
print("xiaoming['name']:", xiaoming['name'])
print("xiaoming['age']:", xiaoming['age'])
print("xiaoming['gender']:", xiaoming['gender'])
print("xiaoming['height']:", xiaoming['height'])
xiaoming['age'] = 22
xiaoming['gender'] = False
print('-' * 50)
print("xiaoming['age']:", xiaoming['age'])
print("xiaoming['gender']:", xiaoming['gender'])
print('-' * 100)
xiaoming['zhiye'] = "stundets"
print(xiaoming['zhiye'])
del xiaoming['zhiye']
print(xiaoming)
print(len(xiaoming))
print(str(xiaoming))
print('-' * 100)
for k in xiaoming:
    print("%s: %s" % (k, xiaoming[k]), end='\t')
print('\n')
xiaoming.pop('gender')
print('-' * 100)
print(xiaoming)

xiaoming1 = xiaoming
print(xiaoming1)
xiaoming1.pop('age')
print(xiaoming1)
xiaoming1 = xiaoming1.copy()
print(xiaoming1)
xiaoming['sex'] = 'male'
print(xiaoming1)
print('-' * 100)
print(xiaoming)
print(xiaoming1)
print('-' * 100)
poem = ["\t\n 登鹳雀楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for poem_str in poem:
# 先使用strip方法去除字符串中的空白字符
# 再使用center方法居中显示文本
    print("|%s|" % poem_str.strip().center(10, " "))
