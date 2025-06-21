# 作者:python11-刘杰
# 2025年05月29日17时21分02秒
# xxx@qq.com
def w_xunhuan(num):
    while num <= 10:
        print(num)
        num += 1
        print(f'i的值为：{num}')
    print('-' * 100)

# w_xunhuan(5)
def qiuhe(num):
    i=1
    sum=0
    while i<=num:
        if i%2!=0:
            i+=1
            continue
        sum+=i
        i+=1
    print(sum)
qiuhe(100)
