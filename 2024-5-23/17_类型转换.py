# 类型转换
tel = '123456'
print(tel, type(tel))
aaa = int(tel)
print(aaa, type(aaa))
sex = 0
bb = bool(sex)  # 凡是布尔型，非0即真
print(sex, type(sex))
print(bb, type(bb))
xingbie = '男'
cc = bool(xingbie)  # 凡是布尔型，非空即真
print(cc, type(cc))
xingbie = ''
dd = bool(xingbie)
print(dd, type(dd))
