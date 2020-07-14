import pandas as pd

data = pd.read_csv(r'C:\Users\seong\Desktop\배성빈\VisualStudioCoding\Traffic_Accident_2017.csv', encoding='euc-kr')


from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

import matplotlib.pyplot as plt

# t = data['요일'].value_counts()
# y = t[['월', '화', '수', '목', '금', '토', '일']]
# x = ['월', '화', '수', '목', '금', '토', '일']

# plt.bar(x,y)
# plt.ylim(500, 620)
# plt.show()

# t = data[['사고유형_대분류', '발생지시도']][data['사고유형_대분류'] == '차대차']
# # t= t['발생지시도'].value.counts()

# x = t['발생지시도']
# y = t['사고유형_대분류']
# plt.bar(x,y)
# # plt.show()

# ##2번째 연습 :: 교통시간 다발 시간대 확인
# t = data['발생년월일시'][data['발생년월일시'] % 100 == 1]

# print(t)

## 카테고리

ages = [0, 2, 10, 21, 23, 37, 31, 61, 20, 41, 32, 100]
bins = [0, 15, 25, 35, 60, 99]
labels = ["미성년자", "청년", "중년", "장년", "노년"]
cats = pd.cut( ages, bins, labels=labels)
