'''
带返回值函数代码中使用 try except finally
'''


def fun():
    try:
        num = float(input('请输入一个数值:'))
        result = 10 / num
        return result
    except:
        print('输入内容不是数值类型')
    finally:
        print('必须要被执行的代码')
        return -1


print(fun())