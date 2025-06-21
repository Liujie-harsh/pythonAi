# 作者:python11-刘杰
# 2025年06月09日22时27分07秒
# xxx@qq.com
import pandas as pd

# 1. 读取数据
sales_df = pd.read_excel('./data.xls', sheet_name='商品销售情况')     # 销售数据
info_df = pd.read_excel('./data.xls', sheet_name='商品信息')          # 商品信息（含单价）
retention_df = pd.read_excel('./data.xls', sheet_name='新增及留存')    # 新增及留存

# 2. 设定目标日期
target_date = pd.to_datetime('2018-01-09')

# 3. 获取该日的商品总销量（所有商品加和）
sales_data = sales_df.set_index('商品名')  # 设置索引方便操作
total_sales = sales_df.loc[:, target_date].sum()

# 4. 获取商品的平均单价（如果单价不同，可以加权）
average_price = info_df['单价'].mean()

# 5. 获取新增用户数（目标日期）
retention_df['日期'] = pd.to_datetime(retention_df.iloc[:, 0])  # 确保是 datetime 类型
new_users = retention_df[retention_df['日期'] == target_date].iloc[0, 1]

# 6. 计算历史留存用户数（所有之前的日期在目标日的留存人数之和）
# 目标日为 1 月 9 日，找所有“第X天留存”中 X天前 = 1月9日-日期 的那一列
ret_df = retention_df.copy()
ret_df = ret_df[ret_df['日期'] < target_date]  # 只考虑之前日期的留存

# 计算目标日对应的第X天留存列索引
ret_df['天差'] = (target_date - ret_df['日期']).dt.days
history_retained = 0
for i, row in ret_df.iterrows():
    day_offset = row['天差']
    try:
        retained = row.iloc[day_offset + 1]  # 第1列为新增，第2列为第1天留存，所以下标+1
        history_retained += retained
    except:
        pass

# 7. 计算 ARPU
total_users = new_users + history_retained
arpu = (total_sales * average_price) / total_users

print(f"2018-01-09 的 ARPU 值为：{arpu:.2f}")
