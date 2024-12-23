employee = ['张三', '李四', '王五', '赵六']
salary = [4000, 5600, 3400, 6000]
for i in range(len(salary)):
    if salary[i] < 5000:
        salary[i] = 5000
print(salary)
