# 作者:python11-刘杰
# 2025年06月06日17时55分44秒
# xxx@qq.com
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# 这是一个无限循环！
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello,{formatted_name}!")


def greet_users(names):
    """向列表中的每位用户发出简单的问候。"""
    for name in names:
        msg = f"Hello,{name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
