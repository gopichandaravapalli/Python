import json
import csv

with open('Users/aravapallivenkatagopichand/Recent/sample4.json') as json_file:
	data = json.load(json_file)

people_data = data['people']

data_file = open('data_file.csv', 'w')

csv_writer = csv.writer(data_file)

count = 0

for x in people_data:
	if count == 0:
		header = x.keys()
		csv_writer.writerow(header)
		count += 1

	csv_writer.writerow(x.values())

data_file.close()
