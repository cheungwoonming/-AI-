import csv
import tool


# reader = csv.reader(open('power_total.csv'))
# reader = list(reader)
# su = 0
# for i in range(213, 244):
#     print(reader[i])
#     la = float(reader[i][1])
#     ne = float(reader[i+366][1])
#     su += (ne-la)
# print(su/31)

# add = 116583
#
# date = tool.date_range('20160901', '20160930', '%Y%m%d')
#
# writer = csv.writer(open('result/Tianchi_power_predict_table.csv', 'w', newline='', encoding='utf-8'))
# writer.writerow(['predict_date', 'predict_power_consumption'])
# reader = csv.reader(open('power_last.csv'))
# reader = list(reader)
# for index, i in enumerate(date):
#     value = float(reader[index][1]) + add
#     writer.writerow([i, str(int(value))])


writer = csv.writer(open('result/Tianchi_power_predict_table.csv', 'w', newline='', encoding='utf-8'))
writer.writerow(['predict_date', 'predict_power_consumption'])
reader = csv.reader(open('Tianchi_power_predict_table.csv'))
reader = list(reader)
for i in reader[1:]:
    temp = int(i[1])
    temp *= 1.1
    temp = int(round(temp, 0))
    writer.writerow([i[0], str(temp)])
