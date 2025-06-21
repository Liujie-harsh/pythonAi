"""
这个程序实现了一个文本分析工具，使用ELF哈希算法对文本文件中的单词进行哈希处理。
主要功能：
1. 读取文本文件并提取所有单词
2. 使用ELF哈希算法计算每个单词的哈希值
3. 统计相同哈希值的出现次数
4. 展示哈希冲突情况（多个不同单词映射到相同哈希值）
"""

import re
from collections import defaultdict

# 定义哈希表的最大键值，用于限制哈希值的范围
MAXKEY = 1000


def elf_hash(hash_str: str) -> int:
    """
    ELF哈希函数实现
    这是一个被广泛使用的字符串哈希算法，最初用于Unix系统中的目标文件格式(ELF)

    算法特点：
    1. 利用字符串中每个字符的ASCII值
    2. 使用位运算提高效率
    3. 通过特殊的位操作减少哈希冲突

    :param hash_str: 需要计算哈希值的字符串
    :return: 返回范围在[0, MAXKEY-1]的哈希值
    """
    h = 0  # 哈希值
    g = 0  # 临时变量，用于存储高位

    for i in hash_str:
        h = (h << 4) + ord(i)  # 左移4位，相当于乘以16，再加上字符的ASCII值
        g = h & 0xf0000000  # 取出高4位
        if g:
            h ^= g >> 24  # 如果高位有值，将其右移24位后与h异或
        h &= ~g  # 清除高4位

    return h % MAXKEY  # 取模确保哈希值在合理范围内


if __name__ == '__main__':
    # 读取文本文件并预处理
    with open('./Beauty and The Beast.txt', 'r', encoding='utf-8') as file:
        content = file.read().lower()  # 读取文件内容并转换为小写字母

    # 使用正则表达式提取所有单词（只包含字母的连续字符）
    words = re.findall(r'\b[a-z]+\b', content)

    # 创建两个字典用于统计和存储：
    # hash_table: 统计每个哈希值出现的次数
    # hash_word_map: 记录每个哈希值对应的具体单词
    hash_table = defaultdict(int)
    hash_word_map = defaultdict(set)  # 使用set避免重复单词

    # 处理每个单词：计算哈希值并更新统计信息
    for word in words:
        hash_value = elf_hash(word)
        hash_table[hash_value] += 1  # 增加该哈希值的计数
        hash_word_map[hash_value].add(word)  # 将单词添加到对应哈希值的集合中

    # 获取出现次数最多的前10个哈希值
    sorted_word_freq = sorted(hash_table.items(), key=lambda x: x[0], reverse=True)[:10]
    printed_hash_values = set()  # 用于跟踪已经输出的哈希值

    # 输出前10个哈希值及其对应的单词
    print("\n哈希值及其对应的单词列表（展示前10个）：")
    for hash_value, count in sorted_word_freq:
        # 跳过已经输出过的哈希值
        if hash_value in printed_hash_values:
            continue

        # 获取当前哈希值对应的所有单词
        words_for_hash = hash_word_map[hash_value]

        # 输出每个单词及其哈希值，用于展示可能的哈希冲突
        for word in words_for_hash:
            print(f"['{word}']: {hash_value}")

        # 将当前哈希值标记为已输出
        printed_hash_values.add(hash_value)
