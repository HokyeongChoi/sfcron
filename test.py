#!/usr/bin/python3
import sqlite3
import pandas as pd
db_path = "SEOUL_FESTIVAL.db"
table_nm = "FESTIVAL_INFO"
con = sqlite3.connect(db_path)
cur = con.cursor()
cur.execute('PRAGMA table_info({})'.format(table_nm))
table_columns = [i[1] for i in cur]

cur.execute('SELECT * FROM FESTIVAL_CLUSTER')
cluster_before = pd.DataFrame(cur.fetchall(), columns=['festival_id', '축제명', '클러스터'])
cur.close()
# print(cluster_before['festival_id'].values[-1])
with open("last_id.txt", 'w') as f:
    f.write(str(cluster_before['festival_id'].values[-1]))
con.close()
