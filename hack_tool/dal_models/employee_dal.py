import psycopg2
from flask import jsonify

from hack_tool.db_connection import connection_db


class EmployeeDAL(object):
    @staticmethod
    def get_employees():
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = f'''SELECT id FROM users;'''

                cursor.execute(query)
                employees = cursor.fetchall()

            return employees

        except Exception as e:
            print(str(e))
            return e

        finally:
            conn.close()

    @staticmethod
    def get_employee(user_id):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = f'''SELECT * FROM users WHERE id = %s;'''

                cursor.execute(query, (user_id,))
                employee = cursor.fetchone()
                print(employee)

            return employee

        except Exception as e:
            print(str(e))
            return e

        finally:
            conn.close()