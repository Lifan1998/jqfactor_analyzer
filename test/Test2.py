import pandas as pd

sample_data = pd.DataFrame(
    [[0.84, 0.43, 2.33, 0.86, 0.96],
     [1.06, 0.51, 2.60, 0.90, 1.09],
     [1.12, 0.54, 2.68, 0.94, 1.12],
     [1.07, 0.64, 2.65, 1.33, 1.15],
     [1.21, 0.73, 2.97, 1.65, 1.19]],
    index=['2018-01-02', '2018-01-03', '2018-01-04', '2018-01-05', '2018-01-08'],
    columns=['000001.XSHE', '000002.XSHE', '000063.XSHE', '000069.XSHE', '000100.XSHE']
)

print(sample_data)

factor_data = sample_data.copy()
# 将 index 转换为 DatetimeIndex
factor_data.index = pd.to_datetime(factor_data.index)
# 将 DataFrame 按照日期顺序排列
factor_data = factor_data.sort_index()
# 检查 columns 是否满足聚宽股票代码格式
if not sample_data.columns.astype(str).str.match('\d{6}\.XSH[EG]').all():
    print("有不满足聚宽股票代码格式的股票")
    print(sample_data.columns[~sample_data.columns.astype(str).str.match('\d{6}\.XSH[EG]')])

print(factor_data)