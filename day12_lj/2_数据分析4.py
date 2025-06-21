# 作者:python11-刘杰
# 2025年06月09日21时47分44秒
# xxx@qq.com

"""
此脚本用于分析商品详情页的购买转化率：
1. 读取商品的销售和浏览数据
2. 计算特定商品（三星充电器）的详情页转化率
3. 找出转化率最高的日期
4. 转化率 = 销售量 / 浏览量
"""

import pandas as pd

# 从Excel文件中读取销售和浏览数据，分别在不同的工作表中
sales_df = pd.read_excel('./data.xls', sheet_name='商品销售情况')  # 销售数据
views_df = pd.read_excel('./data.xls', sheet_name='商品浏览情况')  # 浏览数据

# 以下注释掉的打印语句用于调试，可以查看数据结构
# print(sales_df['商品名'].tolist())  # 查看所有商品名称
# print(views_df.columns.tolist())    # 查看浏览数据的所有列
# print(sales_df.columns.tolist())    # 查看销售数据的所有列



# 提取目标商品"三星 充电器"的数据
# 使用布尔索引从两个DataFrame中分别提取该商品的数据行
sales_row = sales_df[sales_df['商品名'] == '三星 充电器']
views_row = views_df[views_df['商品名（单位：浏览次数）'] == '三星 充电器']

# 数据清洗：删除商品名称列，只保留日期数据
# 这样处理后，两个DataFrame只包含各个日期的数值数据
sales_data = sales_row.drop(columns='商品名')
views_data = views_row.drop(columns='商品名（单位：浏览次数）')

# 数据类型转换：将数据转换为float类型
# 这样做可以确保数值计算的准确性，并防止除零错误
sales_data = sales_data.astype(float)
views_data = views_data.astype(float)

# 计算每个日期的详情页购买转化率
# 转化率 = 销售量 / 浏览量
# values[0]获取DataFrame的第一行数据（因为只有一行）
conversion_rate = (sales_data.values[0] / views_data.values[0])

# 寻找最高转化率及其对应日期
max_index = conversion_rate.argmax()  # 获取最大值的索引位置
max_date = sales_data.columns[max_index]  # 根据索引获取对应的日期
max_rate = conversion_rate[max_index]  # 获取最大转化率

# 输出结果，使用.2%格式化显示百分比（保留两位小数）
print(f'「三星 充电器」详情页购买转化率最高的日期是：{max_date}，转化率为：{max_rate:.2%}')
