# 作者:python11-刘杰
# 2025年06月03日11时48分32秒
# xxx@qq.com
def input_password():


# 1. 提示用户输入密码
    pwd = input("请输入密码：")
# 2. 判断密码长度 >= 8，返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
    # 3. 如果 < 8 主动抛出异常
    print("主动抛出异常")
    # 1> 创建异常对象- 可以使用错误信息字符串作为参数
    # 2> 主动抛出异常
    raise Exception("密码长度不够")
    # 提示用户输入密码
try:
    pwd=input_password()
    print("密码合法：",pwd)
except Exception as result:
    print("错误，",result)
