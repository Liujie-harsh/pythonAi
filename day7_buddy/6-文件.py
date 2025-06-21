# 作者:python11-刘杰
# 2025年06月03日17时59分17秒
# xxx@qq.com
f=open("readme","a+")
f.write("\nhei liujie!\n")
f.seek(0)
a=f.read()
print(a)
f.close()