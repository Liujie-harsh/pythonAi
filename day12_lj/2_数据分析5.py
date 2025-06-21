# 作者:python11-刘杰
# 2025年06月09日22时02分48秒
# xxx@qq.com

"""
此脚本用于分析商品在春节期间和平时的购买转化率差异：
1. 读取商品的销售和浏览数据
2. 提取特定商品（三星充电器）的数据
3. 计算春节期间和非春节期间的平均转化率
4. 比较两个时期的转化率差异
"""

import pandas as pd

# 从Excel文件中读取销售和浏览数据
sales_df = pd.read_excel('./data.xls', sheet_name='商品销售情况')  # 销售数据表
views_df = pd.read_excel('./data.xls', sheet_name='商品浏览情况')  # 浏览数据表

# 提取"三星 充电器"的每日数据
# iloc[0, 1:]表示选择第一行（索引0）的所有列，从第二列开始（跳过商品名列）
sales_row = sales_df[sales_df['商品名'] == '三星 充电器'].iloc[0, 1:]  # 提取销量数据
views_row = views_df[views_df['商品名（单位：浏览次数）'] == '三星 充电器'].iloc[0, 1:]  # 提取浏览量数据

# 获取日期列表（即Excel表中的列名，从第二列开始）
dates = sales_df.columns[1:]

# 构造新的DataFrame，包含日期、销量和浏览量三列
# 这样可以更方便地进行后续分析
df = pd.DataFrame({
    '日期': dates,
    '销量': sales_row.values,
    '浏览量': views_row.values
})

# 将日期列转换为datetime类型，便于后续的日期筛选操作
df['日期'] = pd.to_datetime(df['日期'])

# 计算每天的转化率（销量/浏览量）
df['转化率'] = df['销量'] / df['浏览量']

# 定义2018年春节时间段（2月15日至2月21日）
spring_start = pd.to_datetime('2018-02-15')  # 春节开始日期
spring_end = pd.to_datetime('2018-02-21')    # 春节结束日期

# 使用布尔索引筛选出春节期间和非春节期间的数据
# 春节期间：日期在spring_start和spring_end之间的数据
spring_df = df[(df['日期'] >= spring_start) & (df['日期'] <= spring_end)]
# 非春节期间：日期在spring_start之前或spring_end之后的数据
normal_df = df[(df['日期'] < spring_start) | (df['日期'] > spring_end)]

# 计算两个时期的平均转化率
spring_rate = spring_df['转化率'].mean()  # 春节期间平均转化率
normal_rate = normal_df['转化率'].mean()  # 平时平均转化率

# 输出结果，使用.2%格式化显示百分比（保留两位小数）
print(f"春节期间购买转化率：{spring_rate:.2%}")
print(f"平时购买转化率：{normal_rate:.2%}")
