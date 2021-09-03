import sqlite3
con = sqlite3.connect('example.db')
cur = con.cursor()

# Create table
cur.execute('''DROP TABLE names''')

# Insert a row of data


# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
