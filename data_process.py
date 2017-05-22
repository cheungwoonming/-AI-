import csv
import tool
import pandas
import numpy


# # 找出缺失值
# dateRange = date_range('2015-01-01', '2016-08-31')
# reader = csv.reader(open('Tianchi_power.csv'))
# reader = list(reader)
# pre_id = int(reader[1][1])
# index = 0
# for item in reader[1:]:
#     now_id = int(item[1])
#     date = datetime.datetime.strptime(item[0], "%Y/%m/%d").strftime('%Y-%m-%d')
#     if date.find(dateRange[index % len(dateRange)]) == -1:
#         print(item, dateRange[index % len(dateRange)])
#         index += 1
#         if date.find(dateRange[index % len(dateRange)]) == -1:
#             print('warning!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#             print(item, dateRange[index % len(dateRange)])
#             index += 1
#     index += 1


# dateRange = date_range('2015-01-01', '2016-08-31')
# reader = csv.reader(open('Tianchi_power.csv'))
# reader = list(reader)[1:]
# writer = csv.writer(open('power.csv', 'w', newline=''))
# row = ['date']
# for i in range(1, 1455):
#     row.append(str(i))
# rows = [[i] for i in dateRange]
# for index, item in enumerate(reader):
#     rows[index % len(rows)].append(item[2])
# writer.writerow(row)
# for i in rows:
#     writer.writerow(i)


# reader = csv.reader(open('power.csv'))
# writer = csv.writer(open('power_total.csv', 'w', newline=''))
# reader = list(reader)[1:]
# for i in reader:
#     temp = i[1:]
#     temp = numpy.array(temp)
#     temp = temp.astype(float)
#     s = sum(temp)
#     writer.writerow([i[0], str(s)])

