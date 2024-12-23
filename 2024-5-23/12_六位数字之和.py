# 作业
# 定义一个六位卡号，求6为数字之和
# 定义一个任意六位数
ID = int(input('请输入一个任意六位卡号'))
# 先取余再求整
gewei = ID % 10
shiwei = ID % 100 // 10
baiwei = ID % 1000 // 100
qianwei = ID % 10000 // 1000
wanwei = ID % 100000 // 10000
shiwanwei = ID % 1000000 // 100000
sum = gewei + shiwei + baiwei + qianwei + wanwei + shiwanwei
print(gewei, shiwei, baiwei, qianwei, wanwei, shiwanwei, sum)
