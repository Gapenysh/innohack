from hack_tool.dal_models.comparison_dal import ComparisonDAL
# from hack_tool.llama_api import
class ComparisonBL:
    @staticmethod
    def get_info_two_users(id_1, id_2):
        data1 = ComparisonDAL.get_all_info_by_id(id_1)
        data2 = ComparisonDAL.get_all_info_by_id(id_2)
        return data1, data2

    @staticmethod
    def get_info_two_users_ai(id_1, id_2):
        data1 = ComparisonDAL.get_all_info_by_id(id_1)
        data2 = ComparisonDAL.get_all_info_by_id(id_2)