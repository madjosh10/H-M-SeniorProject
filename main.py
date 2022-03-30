import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Baski\Desktop\SeniorProject\customers.csv")
article = pd.read_csv(r"C:\Users\Baski\Desktop\SeniorProject\articles.csv")
df2 = pd.read_csv(r"C:\Users\Baski\Desktop\SeniorProject\H-M-SeniorProject\first_500.csv")
#
# # 2)What is the distribution of the number of purchases made by various club member statuses?
# types_of_memberships = df.loc[:, ['customer_id','club_member_status']]
# amount_spent = df2.loc[:200, ['customer_id', 'price']]
#
# club_status = types_of_memberships['club_member_status'].value_counts()
# plt.xlabel('customer_status')
# plt.ylabel('customer_count')
# club_status.plot(kind="bar")
# # print(club_status)
#
# right_total = amount_spent['price'] * 1000
# print(round(right_total, 2))
#
# # amount_spent['price'].value_counts()
# right_total = right_total.value_counts()
# right_total.plot(kind='hist')
#
#
# # types_of_memberships['club_member_status'].value_counts()
# amount_spent.plot(kind = 'scatter', x = 'customer_id', y = 'price')
# # plt.show()
# plt.show()

print(df.isnull())
df = df.fillna(0)

print(article.isnull().sum())
article = article.fillna('No Description')
print(article.isnull().sum())


article.to_csv(r'SeniorProject\article2.csv')

df.to_csv('SeniorProject\customer2.csv')

