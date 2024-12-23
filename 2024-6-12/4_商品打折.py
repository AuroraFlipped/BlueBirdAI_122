# 根据购买的商品数量和单价计算总价，并根据满足条是否打折，如果总价超过1000打1折，否者不打折
quantity = int(input("请输入商品数量"))
unit_price = float(input("请输入单价"))
Total_price1 = quantity * unit_price
print(Total_price1)
if Total_price1 >= 1000:
    Total_price2 = Total_price1 * 0.9
    print(f'你的总价为{Total_price1}\n已享受折扣{Total_price2}')
else:
    print(f'您的总价为{Total_price1}为满足折扣条件')
