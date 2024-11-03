from psycopg2 import Error

from hack_tool.db_connection import connection_db
class ComparisonDAL:
    @staticmethod
    def get_all_info_by_id(id):
        conn = connection_db()
        try:
            with conn.cursor() as cur:

                stmt_competencies = """SELECT name, rating, content FROM competencies WHERE user_id = %s"""
                cur.execute(stmt_competencies, (id,))
                competencies_data = cur.fetchall()


                stmt_summary = """SELECT content FROM summary WHERE user_id = %s"""
                cur.execute(stmt_summary, (id,))
                summary_data = cur.fetchall()


                stmt_strong_side = """SELECT content FROM strong_side WHERE user_id = %s"""
                cur.execute(stmt_strong_side, (id,))
                strong_side_data = cur.fetchall()

                stmt_weak_side = """SELECT content FROM weak_side WHERE user_id = %s"""
                cur.execute(stmt_weak_side, (id,))
                weak_side_data = cur.fetchall()

                stmt_recommendation = """SELECT content FROM recommendation WHERE user_id = %s"""
                cur.execute(stmt_recommendation, (id,))
                recommendation_data = cur.fetchall()

                return {
                    "user_id": id,
                    "competencies": competencies_data,
                    "summary": summary_data,
                    "strong_side": strong_side_data,
                    "weak_side": weak_side_data,
                    "recommendation": recommendation_data
                }
        finally:
            conn.close()

    @staticmethod
    def compare_two_summary_ai(id, id_2):
        pass