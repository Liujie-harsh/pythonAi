# 作者:python11-刘杰
# 2025年05月29日19时09分17秒
# xxx@qq.com
a = [1, 2, 2, 2, 3, 3, 3]


def zhaoshu(a):
    for i in a:
        if a.count(i) == 1:
            return i
    return -1
# print(zhaoshu(a))
# for i in range(1,21):
#     print(i,end=' ')
def say_hello(n):
    """
    具体打印几次依靠传递的参数
    :param n:
    :return:
    """
    for i in range(n):
        print('hello')
# say_hello(3)
# help(say_hello)
# print(help(say_hello.__doc__))
import mudle
a=1
b=2
c=3
mudle.mudle1(a)
mudle.mudle2(b)
mudle.mudle3(c)