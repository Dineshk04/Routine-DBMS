import sqlite3


def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS routine(Id INTEGER primary key , date text, earnings integer, exercise text, study text, diet text, others text)")
    conn.commit()
    conn.close()


def insert(date, earnings, exercise, study, diet, others):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO routine VALUES(NULL, ?, ?, ?, ?, ?, ?)', (date, earnings, exercise, study, diet, others))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM routine')
    re = cur.fetchall()
    conn.commit()
    conn.close()
    return re


def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute('DELETE from routine where id=?', (id,))
    conn.commit()
    conn.close()


def search(date='', earnings='', exercise='', study='', diet='', others=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM routine WHERE date=? or earnings=? or exercise=? or study=? or diet=? or others=?',
                (date, earnings, exercise, study, diet, others))
    re = cur.fetchall()
    conn.commit()
    conn.close()
    return re


connect()
