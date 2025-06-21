# 作者:python11-刘杰
# 2025年06月09日21时34分59秒
# xxx@qq.com

"""
此脚本用于分析商品销售数据：
1. 计算系统中的SKU（库存量单位）总数
2. 计算特定日期的SKU销售激活率
3. 包含数据验证以确保日期列存在
"""

import pandas as pd
import datetime

# 读取Excel文件中的商品销售数据
df = pd.read_excel("./data.xls", sheet_name="商品销售情况")

# 计算不重复的SKU数量（使用商品名列去重）
sku_count = df["商品名"].nunique()
print(f"SKU 总数量为：{sku_count}")

# 设定要分析的目标日期
target_date = datetime.datetime(2018, 2, 5, 0, 0)

# 验证目标日期列是否存在于数据中
# 这是一个重要的数据验证步骤，可以防止因日期列不存在而导致的错误
if target_date in df.columns:
    # 计算在目标日期有销量（>0）的SKU数量
    activated_sku = (df[target_date] > 0).sum()
    # 计算激活率：有销量的SKU数量除以总SKU数量
    activation_rate = activated_sku / sku_count
    # 输出结果，使用百分比格式（.2%表示保留两位小数）
    print(f"{target_date} 的 SKU 销售激活率为：{activation_rate:.2%}")
else:
    # 如果目标日期不存在，输出错误提示
    print(f"{target_date} 不在数据列中，请检查日期是否正确。")

