from hack_tool.dal_models.hr_dal import HrDal
from hack_tool.llama_api.proccess import prepare_prompt, proccess_lama
class HrBl:
    @staticmethod
    def create_summary(id):
        reviews = HrDal.make_summary_test_by_id(id)
        print(reviews)
        prompt = prepare_prompt(reviews)
        result = proccess_lama(prompt)
        return result

