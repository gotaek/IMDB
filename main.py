import pymysql
import csv

f = open('title.akas.tsv', 'r', encoding='utf=8')
rd = csv.reader(f, delimiter='\t')
for line in rd:
    print(line)
f.close()
