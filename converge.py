import csv

with open('part2.csv', mode='r') as infile, open('part1.csv', mode='r') as infile2:
    reader = csv.reader(infile)
    reader2 = csv.reader(infile2)
    mydict1 = {rows[1]:rows for rows in reader}
    mydict2 = {rows[3]:rows for rows in reader2}
with open('combined.csv', mode='w') as outfile:
 	writer = csv.writer(outfile)
 	for key in mydict1:
 		if key in mydict2:
 			val = mydict2[key]
 			for item in mydict1[key]:
 				val.append(item)
 			writer.writerow(val)
