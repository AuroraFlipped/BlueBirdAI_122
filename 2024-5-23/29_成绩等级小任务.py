# 输入一个成绩输出成绩的等级
# 如a级90~100 b级 80~90 c级 60~80 d级 0~60
score = int(input('请输入你的成绩分数：'))
if score > 90 & score <= 100:
    print('您的成绩为A级')
elif score > 80 & score <= 90:
    print('您的成绩为B级')
elif score > 60 & score <= 80:
    print('您的成绩为C级')
elif score > 0 & score <= 60:
    print('您的成绩为D级')
else:
    print('您的成绩不存在')
