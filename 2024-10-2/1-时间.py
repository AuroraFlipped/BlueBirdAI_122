# 引入时间模块
import time

# 取当前时间
t = time.time()
# 本地化创建一个时间对样
dui = time.localtime()
# 格式化输出
str = time.strftime("%Y-%m-%d %H:%M:%S", dui)
print(str)
