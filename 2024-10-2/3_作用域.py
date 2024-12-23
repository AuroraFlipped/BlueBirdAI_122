count = 0  # 全局作用域


def fact(n):


    count = -1  # 嵌套作用域


    def act(n):


        if n <= 0:
            month = '五月'
            count = 1  # 局部作用域
            print(month, '销售额：', count)
        else:
            month = '六月'
            count = 2  # 局部作用域
            print(month, '销售额：', count)
    act(n)
fact(3)
print('销售额：', count)
