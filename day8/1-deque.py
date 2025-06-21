# 作者:python11-刘杰
# 2025年06月04日15时20分53秒
# xxx@qq.com
from collections import deque
queue = deque(['A', 'B', 'C'])
queue.append('D')
queue.append('E')
queue.pop()
print(queue)
queue.popleft()
print(queue)
queue.append('F')
queue.extend(['G', 'H', 'I'])
print(queue)
queue.rotate()
print(queue)