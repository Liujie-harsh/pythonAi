# 作者:python11-刘杰
# 2025年06月02日10时18分21秒
# xxx@qq.com
def demo1(*arge,**kwargs):
    print(arge)
    print(kwargs.items())
def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)
    demo1(*args,**kwargs)


demo(1, 2, 3, 4, 5, 7, name="小明", age=18, gender=True)
