# 作者:python11-刘杰
# 2025年06月03日22时16分16秒
# xxx@qq.com
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.arange(0, 6, 0.1)  # 以0.1为单位，生成0到6的数据
y = np.sin(x)

# 绘制图形
plt.plot(x, y)
plt.show()
