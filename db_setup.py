import sqlite3

conn = sqlite3.connect('spirent.db')
cur = conn.cursor()
#cur.execute("drop table spirent")

#cur.execute("UPDATE spirent SET username='maha' where username='lakshmi'")

#cur.execute("create table spirent(username varchar(255) UNIQUE ,password varchar(255))")
#cur.execute("select * from spirent")
#for row in cur.fetchall():
       #print(row)