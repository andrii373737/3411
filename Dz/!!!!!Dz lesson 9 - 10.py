import sqlite3
import requests
from bs4 import BeautifulSoup

response = requests.get('https://books.toscrape.com/')
soup = BeautifulSoup(response.text, 'html.parser')
prices = soup.find_all('p', class_='price_color')
prices_list = []

for price in prices:
    clean_price = price.get_text() 
    prices_list.append(clean_price)
    print(clean_price)









                                                                            #DZ 2









import sqlite3


connection = sqlite3.connect('AnimalKingdom.db')
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Animals (
    ID INTEGER PRIMARY KEY,
    "Назва звіра" TEXT NOT NULL,
    "Тип звіра" TEXT NOT NULL
)
''')


animals_data = [
    ('Лев', 'Ссавець'),
    ('Крокодил', 'Плазун'),
    ('Орел', 'Птах'),
    ('Морька черепаха', 'Плазун'),
    ('Мава', 'Ссавець')
]


cursor.executemany('''
INSERT INTO Animals ("Назва звіра", "Тип звіра") 
VALUES (?, ?)
''', animals_data)


connection.commit()


cursor.execute('SELECT * FROM Animals')
rows = cursor.fetchall()

print("ID | Назва звіра | Тип звіра")
print("-" * 30)
for row in rows:
    print(f"{row[0]}  | {row[1]:<12} | {row[2]}")


connection.close()