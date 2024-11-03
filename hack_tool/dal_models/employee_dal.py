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
                query = """SELECT id, name, job_title FROM users WHERE job_title IS NOT NULL"""
                cursor.execute(query)
                employees = cursor.fetchall()
                user_ids = [employee[0] for employee in employees]

                if not user_ids:
                    return []


                query_count_review = """
                                    SELECT user_id, COUNT(*) as review_count
                                    FROM reviews
                                    WHERE user_id IN %s
                                    GROUP BY user_id
                                """
                cursor.execute(query_count_review, (tuple(user_ids),))
                review_counts = cursor.fetchall()

                query_competencies = """
                                    SELECT  AVG(rating) as avg_value
                                    FROM competencies
                                    WHERE user_id IN %s
                                    GROUP BY user_id
                                """
                cursor.execute(query_competencies, (tuple(user_ids),))
                competencies = cursor.fetchall()


                query_summary = """
                                    SELECT content
                                    FROM summary
                                    WHERE user_id IN %s
                                """
                cursor.execute(query_summary, (tuple(user_ids),))
                summaries = cursor.fetchall()

                # Объединение данных
                employee_reviews = []
                for employee in employees:
                    user_id = employee[0]
                    review_count = next((rc[1] for rc in review_counts if rc[0] == user_id), 0)
                    avg_competency = next((comp[1] for comp in competencies if comp[0] == user_id), None)
                    summary_text = next((summ[1] for summ in summaries if summ[0] == user_id), None)
                    employee_reviews.append({
                        'employee': employee,
                        'review_count': review_count,
                        'avg_competency': avg_competency,
                        'summary_text': summary_text
                    })

                return employee_reviews
        except Error as e:
            return str(e)
        finally:
            conn.close()

