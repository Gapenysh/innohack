from hack_tool.dal_models.hr_dal import HrDal
from hack_tool.bl_models.employee_bl import EmployeeBL
from hack_tool.llama_api.process import prepare_prompt, process_lama


class HrBl:
    @staticmethod
    def create_summary(user_id):
        reviews = HrDal.get_reviews_by_id(user_id)
        print(reviews)
        prompt = prepare_prompt(reviews)
        result = process_lama(prompt)

        EmployeeBL.add_summary_info(user_id, result)
        EmployeeBL.add_competencies_info(user_id, result)
        EmployeeBL.add_weak_info(user_id, result)
        EmployeeBL.add_strength_info(user_id, result)
        EmployeeBL.add_recommendation_info(user_id, result)

        return result

