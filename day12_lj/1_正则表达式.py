# 作者:python11-刘杰
# 2025年06月09日17时30分19秒
# xxx@qq.com
import re


def func():
    # 正则表达式匹配
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'  # 匹配格式为 YYYY-MM-DD HH:MM:SS 的字符串
    test_string = '2025-06-09 17:30:19'

    if re.match(pattern, test_string):
        print("字符串格式正确")
    else:
        print("字符串格式不正确")
    ret = re.match("h", "hello")
    print("匹配结果:", ret.group())
    ret = re.match("[hH]", "Hello")
    print("匹配结果:", ret.group())
    ret = re.match("[01234]hello", "2hello,wangdao")
    print("匹配结果:", ret.group())  # None，因为没有匹配到
    text = "My phone number is 13812345678, call me!"
    match = re.search(r"\d{11}", text)

    if match:
        print("找到了号码：", match.group())

    text = "张三：100分，李四：95分，王五：88分"
    scores = re.findall(r"\d+", text)
    print("所有分数：", scores)

    text = "<p>Hello&nbsp;World</p>\n<h1>Title</h1>"
    cleaned = re.sub(r"<[^>]*>|&nbsp;|\n", "", text)
    print("清理后的内容：", cleaned)

def find_second_match(pattern, text):
    matches = re.finditer(pattern, text)  # 使用 finditer 返回一个迭代器
    try:
        next(matches)  # 跳过第一个匹配项
        second_match = next(matches)  # 获取第二个匹配项
        return second_match.group()
    except StopIteration:
        return None


func()
text = "abc123def456ghi789"
pattern = r"\d+"
second_match = find_second_match(pattern, text)
print(second_match)
