from psycopg2 import Error

from hack_tool.db_connection import connection_db
class HrDal:
    @staticmethod
    def make_summary_test_by_id(id):
        conn = connection_db()
        try:
            with conn.cursor() as cur:
                stmt = """SELECT * FROM reviews WHERE user_id = %s"""
                cur.execute(stmt, (id,))
                result = cur.fetchall()
            return result
        except Error as e:
            return str(e)
        finally:
            conn.close()