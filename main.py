import json
from sqlalchemy.orm import sessionmaker
from models import *
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
USER = os.getenv('user')
PASSWORD = os.getenv('password')
BDNAME = os.getenv('bdname')
DSN = f'postgresql://{USER}:{PASSWORD}@localhost:5432/{BDNAME}'
engine = sq.create_engine(DSN)

if __name__ == '__main__':
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # 1 вариант заполнения БД
    # data = json.load(open('data.json'))
    # for inf in data:
    #     if inf['model'] == 'publisher':
    #         bd = Publisher(name=inf['fields']['name'])
    #     if inf['model'] == 'book':
    #         bd = Book(title=inf['fields']['title'], id_publisher=inf['fields']['id_publisher'])
    #     if inf['model'] == 'shop':
    #         bd = Shop(name=inf['fields']['name'])
    #     if inf['model'] == 'stock':
    #         bd = Stock(id_book=inf['fields']['id_book'], id_shop=inf['fields']['id_shop'], count=inf['fields']['count'])
    #     if inf['model'] == 'sale':
    #         bd = Sale(price=inf['fields']['price'], date_sale=inf['fields']['date_sale'],
    #                   id_stock=inf['fields']['id_stock'], count=inf['fields']['count'])
    #     session.add(bd)
    # session.commit()

    with open('data.json', 'r') as fd:
        data = json.load(fd)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()


    def select_publisher():
        publisher = input('Input publisher id or publisher name: ')
        if publisher.isdigit():
            for p in session.query(Publisher).filter(Publisher.id == publisher).all():
                print(p)
        if publisher.isalpha():
            for p in session.query(Publisher).filter(Publisher.name == publisher).all():
                print(p)


    def select_shop():
        publisher = input('Input publisher id or publisher name: ')
        if publisher.isdigit():
            for p in session.query(Shop).join(Stock).join(Book).join(Publisher).filter(Publisher.id == publisher).all():
                print(p)
        if publisher.isalpha():
            for p in session.query(Shop).join(Stock).join(Book).join(Publisher).filter(
                    Publisher.name.ilike(f'%{publisher}%')).all():
                print(p)


    select_shop()

    session.close()
