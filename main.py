
import pymysql
import numpy as np
import pandas as pd
import csv
import pymysql

conn = pymysql.connect(host='localhost', user='gotaek',
                       password='gotaek', db='movie')
curs = conn.cursor(pymysql.cursors.DictCursor)


f = open('title.akas.tsv', 'r', encoding='utf=8')
rd = csv.reader(f, delimiter='\t')
for line in rd:
    sql = "insert into title(title)values(%s)"
    curs.execute(sql, (line[2]))
    conn.commit()
    # print(line)
    print(line)
f.close()
curs.close()
conn.close()
