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

    @staticmethod
    def add_summary_info(user_id, content):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = f'''INSERT INTO summary (user_id, content) VALUES (%s, %s)'''

                cursor.execute(query, (user_id, content))
                conn.commit()



        except Exception as e:
            print(str(e))
            return e

        finally:
            conn.close()

    @staticmethod
    def add_competencies_info(user_id, competency, rating):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = f'''INSERT INTO competencies (user_id, name, rating) VALUES (%s, %s, %s)'''

                cursor.execute(query, (user_id, competency, rating))
                conn.commit()



        except Exception as e:
            print(str(e))
            return e

        finally:
            conn.close()

    @staticmethod
    def add_strength_info(user_id, strength):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = f'''INSERT INTO strength_weak (user_id, strong_side) VALUES (%s, %s)'''

                cursor.execute(query, (user_id, strength))
                conn.commit()



        except Exception as e:
            print(str(e))
            return e

        finally:
            conn.close()

    @staticmethod
    def add_weak_info(user_id, weakness):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = f'''INSERT INTO strength_weak (user_id, weak_side) VALUES (%s, %s)'''

                cursor.execute(query, (user_id, weakness))
                conn.commit()



        except Exception as e:
            print(str(e))
            return e

        finally:
            conn.close()

    @staticmethod
    def add_recommendation_info(user_id, recommendation):
        conn = connection_db()

        try:
            with conn.cursor() as cursor:
                query = f'''INSERT INTO strength_weak (user_id, recomm) VALUES (%s, %s)'''

                cursor.execute(query, (user_id, recommendation))
                conn.commit()



        except Exception as e:
            print(str(e))
            return e

        finally:
            conn.close()