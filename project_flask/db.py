from flask import g,jsonify,Flask
import pymysql
from pymysql.cursors import DictCursor

DB_CONFIG = {
    'host':'localhost',
    'port':3306,
    'user':'root',
    'password':'123456',
    'db':'testdb',
    'charset':'utf8',
    'cursorclass':DictCursor
}
def get_db():
    db = getattr(g,'_database',None)
    if db is None:
        db = g._database = pymysql.connect(**DB_CONFIG)
    return db

def close_db(exception):
    db = getattr(g,'_database',None)
    if db is not None:
        db.close()

def init_db(app):
    app.teardown_appcontext(close_db)

def query_one(sql,params=None):
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute(sql,params)
        result = cursor.fetchone()
        return result

def query_all(sql,params=None):
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute(sql,params)
        results = cursor.fetchall()
        return results

def execute(sql,params=None):
    try:
        db = get_db()
        with db.cursor() as cursor:
            cursor.execute(sql,params)
            db.commit()
            results = cursor.fetchall()
            return results
    except Exception as e:
        print(str(e))
        db.rollback()
        return str(e)