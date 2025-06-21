# 作者:python11-刘杰
# 2025年06月09日19时55分02秒
# xxx@qq.com
#1 月 7 日当天的 DAU 是多少？
import pandas as pd

df = pd.read_excel(r"./data.xls", sheet_name="新增及留存")
print(df.iloc[:, 0].head(10))
# 找出日期为“1月7日”的那一行
row = df[df.iloc[:, 0] == pd.Timestamp("2018-01-07")]
#
# 计算该行的 DAU 总和（从第2列开始求和，跳过日期列）
dau_sum = row.iloc[:, 1:].sum(axis=1).values[0]
#
print("1月7日的DAU为：", dau_sum)