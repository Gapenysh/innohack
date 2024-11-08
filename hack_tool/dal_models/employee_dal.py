import psycopg2
from aiohttp.web_routedef import static
from flask import jsonify
from hack_tool.dal_models.hr_dal import HrDal
from hack_tool.db_connection import connection_db
from psycopg2 import Error


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
                query = f'''SELECT name FROM users WHERE id = %s;'''

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
    def insert_employee_data(response, user_id):
        conn = connection_db()
        cursor = conn.cursor()
        summary_text = response['summary']
        cursor.execute(
            "INSERT INTO summary (user_id, context) VALUES (%s, %s)",
            (user_id, summary_text)
        )

        for competency, rating in response['parameters'].items():
            content = f"Оценка {competency} - {rating}"
            cursor.execute(
                "INSERT INTO competencies (user_id, name, rating, content) VALUES (%s, %s, %s, %s)",
                (user_id, competency, rating, content)
            )
        for strength in response['strengths']:
            cursor.execute(
                "INSERT INTO strength_weak (user_id, strong_side) VALUES (%s, %s)",
                (user_id, strength)
            )


        for weakness in response['weaknesses']:
            cursor.execute(
                "INSERT INTO strength_weak (user_id, weak_side) VALUES (%s, %s)",
                (user_id, weakness)
            )


        for recommendation in response['recommendations']:
            cursor.execute(
                "INSERT INTO strength_weak (user_id, recomm) VALUES (%s, %s)",
                (user_id, recommendation)
            )
        conn.commit()
        cursor.close()
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
    def add_competencies_info(user_id, competency, rating, description):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = '''INSERT INTO competencies (user_id, name, rating, content) VALUES (%s, %s, %s, %s)'''
                cursor.execute(query, (user_id, competency, rating, description))
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
                query = '''INSERT INTO strong_side (user_id, content) VALUES (%s, %s)'''
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
                query = '''INSERT INTO weak_side (user_id, content) VALUES (%s, %s)'''
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
                query = '''INSERT INTO recommendation (user_id, content) VALUES (%s, %s)'''
                cursor.execute(query, (user_id, recommendation))
                conn.commit()

        except Exception as e:
            print(str(e))
            return e
        finally:
            conn.close()

    @staticmethod
    def add_position_info(user_id, position):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = '''UPDATE users set job_title = %s WHERE id = %s'''
                cursor.execute(query, (position, user_id))
                conn.commit()

        except Exception as e:
            print(str(e))
            return e
        finally:
            conn.close()

    @staticmethod
    def get_user_rating(user_id):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = f'''SELECT rating FROM competencies WHERE user_id = %s'''
                cursor.execute(query, (user_id,))
                result = cursor.fetchall()
                print(f'RESULT - {result}')
                return result

        except Exception as e:
            print(str(e))
            return e
        finally:
            conn.close()

    @staticmethod
    def get_user_competencies(user_id):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = f'''SELECT name, rating, content FROM competencies WHERE user_id = %s'''

                cursor.execute(query, (user_id,))
                result = cursor.fetchall()

                return result

        except Exception as e:
            print(str(e))
            return e
        finally:
            conn.close()

    @staticmethod
    def get_user_strong_side(user_id):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = f'''SELECT content FROM strong_side WHERE user_id = %s'''

                cursor.execute(query, (user_id,))
                result = cursor.fetchall()

                return result

        except Exception as e:
            print(str(e))
            return e
        finally:
            conn.close()

    @staticmethod
    def get_user_weak_side(user_id):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = f'''SELECT content FROM weak_side WHERE user_id = %s'''

                cursor.execute(query, (user_id,))
                result = cursor.fetchall()

                return result

        except Exception as e:
            print(str(e))
            return e
        finally:
            conn.close()

    @staticmethod
    def get_user_recommendations(user_id):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = f'''SELECT content FROM recommendation WHERE user_id = %s'''

                cursor.execute(query, (user_id,))
                result = cursor.fetchall()

                return result

        except Exception as e:
            print(str(e))
            return e
        finally:
            conn.close()

    @staticmethod
    def get_user_summary(user_id):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = f'''SELECT content FROM summary WHERE user_id = %s'''

                cursor.execute(query, (user_id,))
                result = cursor.fetchall()

                return result

        except Exception as e:
            print(str(e))
            return e
        finally:
            conn.close()

    @staticmethod
    def get_user_role(user_id):
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                query = '''SELECT job_title FROM users WHERE id = %s'''

                cursor.execute(query, (user_id,))
                result = cursor.fetchone()

                return result

        except Exception as e:
            print(str(e))
            return e
        finally:
            conn.close()

    @staticmethod
    def get_all_employees_with_reviews_count():
        conn = connection_db()
        try:
            with conn.cursor() as cursor:
                # Первый запрос для получения всех пользователей с непустым content
                query = '''SELECT user_id FROM summary WHERE content IS NOT NULL'''
                cursor.execute(query)
                users = cursor.fetchall()

                result = []
                for user in users:
                    user_id = user[0]

                    # Подсчитываем среднюю оценку по критериям
                    ratings = EmployeeDAL.get_user_rating(user_id)
                    average_rating = round(sum(rating[0] for rating in ratings) / len(ratings), 2)

                    # Второй запрос для получения имени и должности пользователя
                    query = '''SELECT name, job_title FROM users WHERE id = %s'''
                    cursor.execute(query, (user_id,))
                    user_info = cursor.fetchone()

                    # Третий запрос для получения всех отзывов пользователя
                    query = '''SELECT content FROM summary WHERE user_id = %s'''
                    cursor.execute(query, (user_id,))
                    summary = cursor.fetchall()

                    # Четвертый запрос для подсчета количества отзывов
                    query = '''SELECT count(*) FROM reviews WHERE user_id = %s'''
                    cursor.execute(query, (user_id,))
                    reviews_count = cursor.fetchone()[0]

                    # Собираем результат
                    result.append({
                        'user_id': user_id,
                        'name': user_info[0],
                        'job_title': user_info[1],
                        'summary': summary,
                        'reviews_count': reviews_count,
                        'average_rating': average_rating
                    })

                return result

        except Error as e:
            return str(e)
        finally:
            conn.close()

    @staticmethod
    def get_all_employees_with_reviews_list():
        conn = connection_db()
        try:
            with conn.cursor() as cursor:

                query = '''SELECT id, name FROM users WHERE job_title IS NOT NULL'''
                cursor.execute(query)
                users = cursor.fetchall()
            return users
        except Error as e:
            return str(e)
        finally:
            conn.close()



