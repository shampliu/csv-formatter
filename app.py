import csv

r1 = csv.reader(open('sanders.csv', 'rb'))
r1.next()	# skip first line

r2 = csv.reader(open('clinton.csv', 'rb'))
r2.next()

writer = csv.writer(open('result.csv', 'wb'))

for row in r1:
	writer.writerow(row)

for row in r2:
	writer.writerow(row)

# d = {}
# d['column1name'] = []
# d['column2name'] = []
# d['column3name'] = []

# dictReader = csv.DictReader(open('sanders.csv', 'rb'), fieldnames = ['column1name', 'column2name', 'column3name'], delimiter = ',', quotechar = '"')

# for row in dictReader:
#     for key in row:
#         d[key].append(row[key])
#         print "%s : %s " % (key, row[key])