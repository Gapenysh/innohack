from hack_tool.dal_models.comparison_dal import ComparisonDAL
from hack_tool.llama_api.proccess_comparison import prepare_prompt_comparison, process_lama_comparison
class ComparisonBL:
    @staticmethod
    def get_info_about_user(id_1):
        data1 = ComparisonDAL.get_all_info_by_id(id_1)

        return data1

    @staticmethod
    def get_info_two_users_ai(id_1, id_2):
        data1 = ComparisonDAL.get_all_info_by_id(id_1)
        data2 = ComparisonDAL.get_all_info_by_id(id_2)
        summary = {
            "Данные 1го работника":data1,
            "Данные 2го работника":data2,
        }
        prompt = prepare_prompt_comparison(summary)
        print(prompt)
        result = process_lama_comparison(prompt)
        print(result)
        return result



