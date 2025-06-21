# 作者:python11-刘杰
# 2025年06月03日19时47分12秒
# xxx@qq.com
# try:
#     a=int(input("请输入整型数: "))
#     # b=a[::-1]#整数无法切片反转
#     b=str(a)[::-1]
#     if b==b[::-1]:
#         print("这是一个对称数")
#     else:
#         raise ValueError("不是对称数")
#
# except ValueError as e:
#     if str(e) == "不是对称数":
#         print("请输入一个对称数")
#     else:
#         print("请输入有效整数")

import sys
print(sys.argv)
file_1=open(sys.argv[1],'r+')
file_2=open(sys.argv[2],'r+')
print(file_1.read())
print(file_2.read())
file_1.close()
file_2.close()
print(sys.argv)
print(sys.argv)
