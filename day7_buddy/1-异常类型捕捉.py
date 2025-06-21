# 作者:python11-刘杰
# 2025年06月03日11时28分29秒
# xxx@qq.com
if __name__=='__main__':
    try:
        num=int(input("输入一个整数:"))
        result=8/num
        print(result)
    except ZeroDivisionError:
        print("请不要输入0！")
    except ValueError:
        print("请输入一个整数")
