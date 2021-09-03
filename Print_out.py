import sqlite3
import os
con = sqlite3.connect('example.db')
cur = con.cursor()


cur.execute('SELECT * FROM names')
results = cur.fetchall()
  
# loop through the rows
for roww in results:
    print(roww)
    print("\n")
    
for row in cur.execute('SELECT * FROM names'):
    print(row)
con.commit()
con.close()
