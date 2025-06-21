# 作者:python11-刘杰
# 2025年06月09日21时02分30秒
# xxx@qq.com

"""
此脚本用于分析用户留存数据：
1. 从Excel文件中读取用户新增和留存数据
2. 计算7日留存率
3. 找出7日留存率最高的日期
"""

import pandas as pd

# 从Excel文件中读取数据，指定sheet名称为"新增及留存"
df = pd.read_excel("./data.xls", sheet_name="新增及留存")

# 提取关键数据列
dates = df.iloc[:, 0]  # 第一列：日期
new_users = df.iloc[:, 1]  # 第二列：新增用户数
retention_day7 = df.iloc[:, 9]  # 第八列：7日后的留存用户数

# 计算7日留存率：7日后的留存用户数除以新增用户数
retention_rate_day7 = retention_day7 / new_users

# 将计算得到的7日留存率添加为新的列
df["Retention Rate Day 7"] = retention_rate_day7

# 找出留存率最高的记录
max_index = retention_rate_day7.idxmax()  # 获取最大留存率的索引
best_date = dates[max_index]  # 获取对应的日期
max_retention_rate = retention_rate_day7[max_index]  # 获取最大留存率

# 打印结果，使用百分比格式显示留存率
print(f"The highest 7-day retention rate is on: {best_date}, with a rate of {max_retention_rate:.2%}")
