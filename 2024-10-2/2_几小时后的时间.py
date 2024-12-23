import time


def after(hours):
    t = time.time() + hours * 3600
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))


h = int(input('请输入小时：'))
shijian = after(h)
print(f'{h}小时后的时间为{shijian}')
