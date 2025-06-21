# 作者:python11-刘杰
# 2025年06月03日16时58分58秒
# xxx@qq.com
import random
random1=random.randrange(1,11)
print(random1)
for i in range(1,11):
    print(random.randint(1,11),end=' ')

from random import randint
print('\n')
for i in range(10):
    print(randint(1,11),end=' ')
print(random.__file__)