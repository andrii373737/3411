import requests
import sqlite3
import logging
from bs4 import BeautifulSoup


logging.basicConfig(filename="news.log", level=logging.ERROR)

class NewsParser:
    def __init__(self, url):
        self.url = url

    def get_news(self):
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, "html.parser")

            news = []

            for a in soup.find_all("a"):
                title = a.get_text(strip=True)
                link = a.get("href")

                if title and link and link.startswith("/"):
                    full_link = "https://edition.cnn.com" + link
                    news.append((title, full_link))

            return news[:10]  # беремо тільки 10 новин

        except Exception:
            logging.error("Сайт недоступний")
            print("Помилка: сайт недоступний")
            return []

    def save_news(self, news):
        with sqlite3.connect("news.db") as db:
            db.execute("""
                CREATE TABLE IF NOT EXISTS news (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    link TEXT
                )
            """)

            for title, link in news:
                db.execute(
                    "INSERT INTO news (title, link) VALUES (?, ?)",
                    (title, link)
                )


# запуск
parser = NewsParser("https://edition.cnn.com/")
news = parser.get_news()

if news:
    parser.save_news(news)
    print("Новини збережено!")
    for title, link in news:
        print(title)
        print(link)
        print("------")