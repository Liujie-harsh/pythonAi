# 作者:python11-刘杰
# 2025年06月03日21时18分29秒
# xxx@qq.com
import os


def deepscan(path, width):
    list_files = os.listdir(path)
    for file_name in list_files:
        print(' ' * width, file_name)
        new_path = os.path.join(path, file_name)  # 确保子目录下的目录，路径正确
        if os.path.isdir(new_path):  # 判断如果是文件夹
            deepscan(new_path, width + 4)

print("当前目录：", os.getcwd())
deepscan(".", 0)
