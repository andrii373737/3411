import sqlite3
connection = sqlite3.connect("AnimalKingdom.sl3", timeout = 15)

cur = connection.cursor()

#cur.execute("CREATE TABLE Animals (name TEXT, type TEXT);")
connection.commit()

#cur.execute("INSERT INTO Animals (name, type) VALUES ('Лев', 'Ссавець'), ('Крокодил', 'Плазун'), ('Орел', 'Птах'), ('Морська черепаха', 'Плазун'), ('Мавпа', 'Ссавець');")
connection.commit()

cur.execute("SELECT * FROM Animals")
connection.commit()

result = cur.fetchall()
print(result)

cur.execute("SELECT * FROM Animals WHERE name = 'Лев'")
connection.commit()

result = cur.fetchall()
print(result)

cur.execute("UPDATE Animals SET type = 'Хижак' WHERE name = 'Лев'")

cur.execute("SELECT * FROM Animals")
result = cur.fetchall()
print(result)

cur.execute("DELETE FROM Animals WHERE name = 'Лев'")

cur.execute("SELECT * FROM Animals")
result = cur.fetchall()
print(result)

cur.execute("DROP TABLE Animals")
cur.execute("SELECT * FROM Animals")
result = cur.fetchall()
print(result)

connection.close()