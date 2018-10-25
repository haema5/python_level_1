import json
import sqlite3
import os
from urllib.request import urlopen


class City:
    def __init__(self, id, name, country, coord):
        self.id = id
        self.city = name
        self.country = country
        self.coord = coord


def get_api_key(path, file_name):
    path = os.path.join(path, file_name)
    with open(path, encoding='UTF-8') as f:
        return f.readline()


def open_city(path, file_name):
    path = os.path.join(path, file_name)
    with open(path, encoding='UTF-8') as f:
        return json.load(f)


def create_db(path, file_name, data):
    path = os.path.join(path, file_name)
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute(
        'CREATE TABLE IF NOT EXISTS cities (id_city INTEGER PRIMARY KEY, city VARCHAR(225), country VARCHAR(2), temperature INTEGER)')

    for i in data:
        u = City(**i)
        c.execute('INSERT OR REPLACE INTO cities VALUES (?,?,?,?)', (u.id, u.city, u.country, 'null'))

    conn.commit()


def get_data(city):
    inp_city = city.split(', ')[0]
    inp_coun = city.split(', ')[1]
    key = get_api_key('data', 'api_key.txt')
    path = os.path.join('data', 'mydb.db')
    conn = sqlite3.connect(path)
    c = conn.cursor()

    for row in c.execute(
            'SELECT id_city FROM cities WHERE city = \'{}\' AND country = \'{}\''.format(inp_city, inp_coun)):
        url = 'http://api.openweathermap.org/data/2.5/weather?units=metric&id={}&appid={}'.format(row[0], key)
        temp = json.load(urlopen(url))['main']['temp']

        c.execute(
        'UPDATE cities SET temperature = {} WHERE city = \'{}\' AND country = \'{}\''.format(temp, inp_city,
                                                                                             inp_coun))
        conn.commit()

        for row in c.execute(
            'SELECT * FROM cities WHERE city = \'{}\' AND country = \'{}\''.format(inp_city, inp_coun)):
            return row


data = open_city('data', 'city.list.json')
create_db('data', 'mydb.db', data)

answer = input('Пожалуйста введите название города и индекс страны (Пример: Novinki, RU): ')
answer = get_data(answer)

print('Температура в городе {}, {}: {}c'.format(answer[1], answer[2], answer[3]))
