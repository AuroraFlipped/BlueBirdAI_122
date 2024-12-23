# 周末计划表，根据天气预报的信息，列举周末计划表。只有输入为晴天或多云时，才外出游玩。
# 输入天气判断是晴天还是多云
weather = input('请输入周末天气情况（晴天/下雨/阴天/多云）：')
weather_case = (weather == '晴天' or weather == '多云')
print('-' * 10, '周末计划表', '-' * 10)
print(f'天气情况', '外出游玩', sep='\t\t')
print(f'{weather}\t\t\t{weather_case}')
print('-' * 31)
