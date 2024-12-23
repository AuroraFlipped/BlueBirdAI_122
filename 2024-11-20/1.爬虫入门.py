str = '''
    <!-- 科技 信息流静态化 -->
    <a href="https://www.163.com/tech/article/J7VCGOM600098IEO.html">俞敏洪透露董宇辉离职幕后：深陷舆论风暴</a>
    <a href="https://www.163.com/dy/article/J7ULIOFR05118DFD.html">估值超200亿，百川智能完成50亿元A轮融资</a>
    <a href="https://www.163.com/tech/article/J7UM9CVT00097U81.html">7月25日外媒科学网站摘要：安慰剂是如何缓解疼痛的？</a>
    <a href="https://www.163.com/tech/article/J7U9OTHO00097U7T.html">为什么OpenAI今年可能会亏损50亿美元？</a>
    <a href="https://www.163.com/tech/article/J7U9LG7700097U7T.html">马斯克称考虑取消投资，墨西哥总统回击：说这话太草率</a>
    <a href="https://www.163.com/tech/article/J7U9I0D300097U7T.html">马斯克询问网友：特斯拉向xAI投50亿美元行不行</a>
    <a href="https://www.163.com/tech/article/J7V4OLU400098IEO.html">巴黎奥运会系列报道｜商汤日日新大模型亮相</a>
    <a href="https://www.163.com/dy/article/J7V47TFA0511B8LM.html">本田拟削减中国燃油车产能：149万辆→100万辆，关闭或停产两家工厂</a>
    <a href="https://www.163.com/dy/article/J7V1ONQ9051481US.html">马斯克要跟扎克伯格“笼斗”！随时随地、任何规则</a>
    <a href="https://www.163.com/tech/article/J7URIJRP00098IEO.html">抖音电商否认“上半年GMV未达预期”传闻</a>
    <a href="https://www.163.com/dy/article/J7UQ5M2L05198NMR.html"> “最懂苹果”分析师郭明錤：苹果将停产iPhone 17 Plus</a>
    <a href="https://www.163.com/dy/article/J7UI2RGL05476C4F.html">李斌回应蔚来“千站计划”迟缓问题：最多推迟一两个月</a>
    <a href="https://www.163.com/dy/article/J7UHQE7O0514R9P4.html">美股七巨头一夜市值蒸发近6万亿元，创下12年以来最大单日跌幅</a>
    <a href="https://www.163.com/tech/article/J7UFGHVC00098IEO.html">报告｜同程旅行：奥运会开幕首周巴黎酒店预订热度同比涨4倍</a>
    <a href="https://www.163.com/dy/article/J7SP2K20051180F7.html">扎克伯格深度专访：中美AI竞争完全错误，美国别想长期领先中国</a>
    <a href="https://www.163.com/dy/article/J7SMODLV05198NMR.html">OpenAI老板做的全民发钱实验，结果出来了！</a>
    <a href="https://www.163.com/dy/article/J7SQBHRO0511B8LM.html">雷克萨斯将在华生产全新纯电车型，并销往日本？官方：不予置评</a>
    <a href="https://www.163.com/dy/article/J7SU69NT051492T3.html">起步价1.5元只能骑10分钟，哈啰单车变相涨价</a>
    <a href="https://www.163.com/dy/article/J7T2DVUB0519U3I5.html">武汉萝卜快跑涨价，基本与网约车持平？我们测了一下</a>
    <a href="https://www.163.com/dy/article/J7T90BH20511B8LM.html">小米汽车：近年内还没有在海外市场销售汽车的计划</a>
    <a href="https://www.163.com/dy/article/J7UDK8C00519APGA.html">网红企业家风云榜：雷军成顶流，俞敏洪反超董明珠</a>
    <a href="https://www.163.com/dy/article/J7UC02TG05198R91.html">小红书变局：卖老股、边裁员边扩招，为上市“加速”</a>
    <a href="https://www.163.com/dy/article/J7UBV0LU0514R9OJ.html">微软Bing搜索结果引入AI摘要功能，逐步推进智能搜索体验</a>
    <a href="https://www.163.com/dy/article/J7UA0SUH05564B6E.html">抖音再攻图文，不止“围猎”小红书</a>
    <a href="https://www.163.com/dy/article/J7T1CR9L0539M9HP.html">非洲之王，为何在印度栽跟头？</a>
    <a href="https://www.163.com/dy/article/J7U6TVB60511B8LM.html">企业蒙受巨额损失，CrowdStrike向受灾客户发放10美元礼品卡，又收回了</a>
    <a href="https://www.163.com/dy/article/J7U6MLJR0519DDQ2.html">特斯拉股价重挫12%，市值蒸发超800亿美元</a>
    <a href="https://www.163.com/dy/article/J7U53BVN0511B8LM.html">全球最大清洁能源滚装船完成交付，上汽自营船队扩容至32艘</a>
    <a href="https://www.163.com/dy/article/J7U465G90527822Q.html">面对价格战，马斯克也无能为力了</a>
    <a href="https://www.163.com/dy/article/J7TBFVAI0514R9OJ.html">环球时报：美媒指责中国隐瞒超算实力毫无道理，美国才是元凶</a>
'''
str_list = str.split('>')
# print(str_list)
for i in range(2,len(str_list),2):
    print(str_list[i][:-3])

