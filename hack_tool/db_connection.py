import psycopg2

from hack_tool.config import settings


def connection_db():
    dbname = settings.DB_NAME
    user = settings.USER
    password = settings.PASSWORD
    host = settings.HOST_NAME
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        return conn
    except:
        return {"message": "Can`t establish connection to database"}
