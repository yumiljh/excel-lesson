#-*- coding:utf-8 -*-

import pandas as pd

df = pd.read_excel('Excel练习数据源5.xlsx','Sheet1')
data = df.ix[:].values

list_male = ''
list_female = ''

for x,y in data:
    if y == u'男':
        list_male = list_male + x + u'；'
    else:
        list_female = list_female + x + u'；'

test_data = {u'性别':[u'男',u'女'], u'列表':[list_male,list_female]}
test_df = pd.DataFrame(data = test_data, columns=[u'性别',u'列表'])
test_df.to_excel('Excel练习数据源5_数据结果.xlsx')

