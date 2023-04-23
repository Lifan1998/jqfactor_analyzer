# 获取因子数据：以5日平均换手率为例，该数据可以直接用于因子分析
# 具体使用方法可以参照jqdatasdk的API文档
import jqdatasdk
jqdatasdk.auth('15055735530', 'JoinQuant1998')
# # 获取聚宽因子库中的VOL5数据
# factor_data=jqdatasdk.get_factor_values(
#     # securities=jqdatasdk.get_index_stocks('000300.XSHG'),
#     securities=['003000.XSHG'],
#     factors=['VOL5'],
#     start_date='2022-04-28',
#     end_date='2023-04-10')['VOL5']

# 申万一级行业
data = jqdatasdk.get_industries(name='sw_l1')
data = data.drop(columns=['start_date'])
print(f'data:{data}')

data = jqdatasdk.get_security_info2('801750')
print(f'data:{data=}')


# data = jqdatasdk.get_concepts()
# print(f'data:{data=}')


data = jqdatasdk.get_price(security='000300.XSHG', start_date = '2023-04-10', end_date = '2023-04-24', frequency='daily')
print(f'data:\n{data}')

data = jqdatasdk.get_bars(security='000300.XSHG', count=10, unit='1d', include_now=True, fields=("date", "open", "high", "low", "close",'volume','money'))
print(f'data:\n{data}')

#



