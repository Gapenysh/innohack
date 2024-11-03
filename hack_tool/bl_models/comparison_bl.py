from hack_tool.dal_models.comparison_dal import ComparisonDAL
from hack_tool.llama_api.proccess_comparison import prepare_prompt_comparison, process_lama_comparison
class ComparisonBL:
    @staticmethod
    def get_info_about_user(id_1):
        data1 = ComparisonDAL.get_all_info_by_id(id_1)

        return data1

    @staticmethod
    def comparison_two_users_ai(id_1, id_2):
        data1 = ComparisonDAL.get_all_info_by_id_list(id_1)
        data2 = ComparisonDAL.get_all_info_by_id_list(id_2)


        prompt = prepare_prompt_comparison(data1, data2)

        if not prompt:
            return {"message": "data1 и data2 имеют одинаковые id",
                    "Data1_id": f"{data1[0]}",
                    "Data2_id": f"{data2[0]}"}

        result = process_lama_comparison(prompt)
        print(result)
        return result



