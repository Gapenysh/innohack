from psycopg2 import Error

from hack_tool.db_connection import connection_db
class HrDal:
    @staticmethod
    def get_reviews_by_id(id: int):
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt = """SELECT * FROM reviews WHERE user_id = %s"""
                cur.execute(stmt, (id,))
                result = cur.fetchall()
                print(result)
            return result
        except Error as e:
            return str(e)
        finally:
            conn.close()