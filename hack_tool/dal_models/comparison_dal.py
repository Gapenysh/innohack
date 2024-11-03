from psycopg2 import Error

from hack_tool.db_connection import connection_db
class ComparisonDAL:
    @staticmethod
    def get_all_info_by_id(id):
        conn = connection_db()
        try:
            with conn.cursor() as cur:

                stmt_competencies = """
                                    SELECT * FROM competencies WHERE user_id = %s
                                """
                cur.execute(stmt_competencies, (id,))
                competencies_data = cur.fetchall()


                stmt_summary = """
                                    SELECT * FROM summary WHERE user_id = %s
                                """
                cur.execute(stmt_summary, (id,))
                summary_data = cur.fetchall()


                stmt_strength_weak = """
                                    SELECT * FROM strength_weak WHERE user_id = %s
                                """
                cur.execute(stmt_strength_weak, (id,))
                strength_weak_data = cur.fetchall()


                return {
                    "user_id": id,
                    "competencies": competencies_data,
                    "summary": summary_data,
                    "strength_weak": strength_weak_data
                }
        finally:
            conn.close()

    @staticmethod
    def compare_two_summary_ai(id, id_2):
        pass