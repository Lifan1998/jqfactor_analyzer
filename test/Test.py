# 载入函数库
import pandas as pd
import jqfactor_analyzer as ja

# 获取 jqdatasdk 授权，输入用户名、密码，申请地址：http://t.cn/EINDOxE
# 聚宽官网，使用方法参见：http://t.cn/EINcS4j
import jqdatasdk
jqdatasdk.auth('15055735530', 'JoinQuant1998')

# 获取5日平均换手率因子2018-01-01到2018-12-31之间的数据（示例用从库中直接调取）
# 聚宽因子库数据获取方法在下方
from jqfactor_analyzer.sample import VOL5
factor_data = VOL5

# 对因子进行分析
far = ja.analyze_factor(
    factor_data,  # factor_data 为因子值的 pandas.DataFrame
    quantiles=10,
    periods=(1, 10),
    industry='jq_l1',
    weight_method='avg',
    max_loss=0.1
)

# 获取整理后的因子的IC值
far.ic

# 生成统计图表
far.create_full_tear_sheet(
    demeaned=False, group_adjust=False, by_group=False,
    turnover_periods=None, avgretplot=(5, 15), std_bar=False
)