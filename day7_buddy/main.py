# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


def divide(a, b):
    return a / b  # 若b=0，异常会传递到外层


def check_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    print(10 / 2)  # ZeroDivisionError
    try:
        divide(2, 1)
        # 可能出错的代码
        # x = 10 / 0
    except ZeroDivisionError:
        print("不能除以零！")  # 处理异常

    try:
        check_age(-1)
    except ValueError as e:
        print(f"捕获到异常：{e}")
    try:
        1 / 0
    except Exception as e:
        print("错误文件:", e.__traceback__.tb_frame.f_globals["__file__"])
        print("错误行号:", e.__traceback__.tb_lineno)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
