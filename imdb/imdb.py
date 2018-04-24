from datetime import date, timedelta
import csv

competitionday = date(2018, 5, 7)
minutes = 0
notmissing = 0
missing = 0

with open('title.basics.tsv') as f:
    reader = csv.reader(f, delimiter='\t')
    reader.next()
    for row in reader:
        runtime = row[-2]
        if runtime == '\\N':
            missing += 1
        else:
            notmissing += 1
            minutes += int(runtime)

minutes += missing * (minutes/notmissing)

print competitionday + timedelta(minutes = minutes)
