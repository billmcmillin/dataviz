import csv

with open('cincy_food.csv', mode='r') as infile:
	with open('part1.csv', mode='w') as outfile:
		writer = csv.writer(outfile)
		reader = csv.reader(infile)
		for row in reader:
			lat = row[7]
			lat = lat[:7]
			lat.ljust(6, '0')
			print lat
			lon = row[8]
			lon = lon[:8]
			lon.ljust(6, '0')
			print lon
			row[7] = lat
			row[8] = lon
			writer.writerow(row)

