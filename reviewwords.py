import sqlite3

conn = sqlite3.connect('words.db')
c = conn.cursor()
#print("WORD, CORRECT, INCORRECT")
#c.execute("select word, correct, incorrect from words")
#rows = c.fetchall()
#for row in rows:
#    print(row)
print("------------CORRECT------------")
print("WORD, CORRECT, INCORRECT")
c.execute("select word, correct, incorrect from words order by correct DESC")
rows = c.fetchall()
for row in rows:
    print(row)
print("-----------INCORRECT-----------")
print("WORD, CORRECT, INCORRECT")
c.execute("select word, correct, incorrect from words order by incorrect DESC")
rows = c.fetchall()
for row in rows:
    print(row)