import csv

with open('test.csv', mode='r') as infile:
	with open('part2.csv', mode='w') as outfile:
		writer = csv.writer(outfile)
		reader = csv.reader(infile)
		for row in reader:
			addy = row[1]
			if addy[-2:] == 'AV':
				addy += 'E'
				print addy
			if addy[-2:] == 'WY':
				addy.replace('WY', 'WAY')
			if addy[-2:] == 'RD':
				addy.replace('RD', 'ROAD')
				print addy
			row[1] = addy
			writer.writerow(row)

