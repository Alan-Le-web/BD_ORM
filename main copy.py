import sqlalchemy
from sqlalchemy.orm import sessionmaker
import os.path
import json
from pprint import pprint
from dotenv import load_dotenv
from models import create_tables, Publisher, Shop, Book, Stock, Sale



dotenv_path = 'config.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

DSN = os.getenv("dsn")
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)


Session = sessionmaker(bind=engine)
session = Session()

# with open('import/tests_data.json', 'r') as fd:
#     data = json.load(fd)

# for record in data:
#     model = {
#         'publisher': Publisher,
#         'shop': Shop,
#         'book': Book,
#         'stock': Stock,
#         'sale': Sale,
#     }[record.get('model')]
#     session.add(model(id=record.get('pk'), **record.get('fields')))

pub1 = Publisher(name = "Пушкин")
pub2 = Publisher(name = "Гоголь")
pub3 = Publisher(name = "Бессон")
pub4 = Publisher(name = "Сталоне")
pub5 = Publisher(name = "Архимед")
session.add(pub1)
session.add(pub2)
session.add(pub3)
session.add(pub4)
session.add(pub5)

shop1 = Shop(name = "Магазин Комиксы")
shop2 = Shop(name = "Блохастый рынок")
shop3 = Shop(name = "Детский мир")
shop4 = Shop(name = "Лавка старых книг")
shop5 = Shop(name = "Любимая книга")
session.add(shop1)
session.add(shop2)
session.add(shop3)
session.add(shop4)
session.add(shop5)


book1 = Book(title = "Квазимодо", publisher = pub1)
book2 = Book(title = "Гарри Поттер - 1", publisher = pub2)
book3 = Book(title = "Гарри Поттер - 2", publisher = pub2)
book4 = Book(title = "Детектив", publisher = pub4)
book5 = Book(title = "Спайдер Мэн", publisher = pub3)
book6 = Book(title = "Физика 6 класс", publisher = pub5)
session.add(book1)
session.add(book2)
session.add(book3)
session.add(book4)
session.add(book5)
session.add(book6)



stock1 = Stock(shop = shop1, book = book5, count = 10)
stock2 = Stock(shop = shop1, book = book2, count = 15)
stock3 = Stock(shop = shop2, book = book1, count = 13)
stock4 = Stock(shop = shop3, book = book2, count = 13)
stock5 = Stock(shop = shop3, book = book3, count = 4)
stock6 = Stock(shop = shop4, book = book1, count = 5)
stock7 = Stock(shop = shop4, book = book6, count = 22)
stock8 = Stock(shop = shop5, book = book2, count = 12)
stock9 = Stock(shop = shop5, book = book3, count = 31)
stock10 = Stock(shop = shop5, book = book4, count = 12)

session.add_all([stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8, stock9, stock10])


sale1 = Sale(price = 22, date_sale = "2018-10-24",  stock = stock1, count = 2)
sale2 = Sale(price = 12, date_sale = "2018-10-27",  stock = stock1, count = 1)
sale3 = Sale(price = 44, date_sale = "2018-10-26",  stock = stock1, count = 3)
sale4 = Sale(price = 234, date_sale = "2018-10-20",  stock = stock1, count = 8)
sale5 = Sale(price = 41, date_sale = "2018-10-22",  stock = stock1, count = 3)
sale6 = Sale(price = 55, date_sale = "2018-10-29",  stock = stock1, count = 4)
session.add_all([sale1, sale2, sale3, sale4, sale5, sale6])




session.commit()


# for i in session.query(Book).join(Publisher).filter(Publisher.name == autor).all():
#     print(i)

# запросы
# q = session.query(Stock).join(Homework.course).filter(Homework.number == 1)
# print(q)
# for s in q.all():
#     print(s.id, s.name)
#     for hw in s.homeworks:
#         print("\t", hw.id, hw.number, hw.description)

# # вложенный запрос
# subq = session.query(Homework).filter(Homework.description.like("%сложн%")).subquery("simple_hw")
# q = session.query(Course).join(subq, Course.id == subq.c.course_id)
# print(q)
# for s in q.all():
#     print(s.id, s.name)
#     for hw in s.homeworks:
#         print("\t", hw.id, hw.number, hw.description),

# results = (session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
#            .join(Stock)
#            .join(Sale)
#            .join(Publisher)
#            .filter(Publisher.name == author)
#            .all())
print(pub1)
print(pub2)
print(pub3)
print(pub4)
print(pub5)
# author = input("Введите имя автора: ")
author = "Пушкин"
results = (session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
           .join(Stock)
           .join(Sale)
           .join(Publisher)
           .filter(Publisher.name == author)
           .all())
# Вывод результата
for title, shop_name, price, date in results:
    print(f"{title} | {shop_name} | {price} | {date.strftime('%Y-%m-%d')}")

session.close()