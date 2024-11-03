import json
import requests


def prepare_prompt_comparison(data1, data2):

    if data1[0] == data2[0]:
        return None
    print(data1[0])
    print(data2[0])



    instructions = "Ты профессиональный HR-специалист.nУ тебя сводка и характеристики двух работников:nn"
    instructions += "На основе данных двух описаний сотрудников определи, кто из них будет компетентнее. "
    instructions += "Опиши какие качества могут сыграть решающую роль в выборе именно этого сотрудника.n"
    instructions += "Вот исходные данные:n"

    instructions +=
def process_lama_comparison(prompt):
    url = "https://vk-scoreworker-case.olymp.innopolis.university/generate"


    data = {
        "prompt": [prompt],
        "apply_chat_template": True,
        "system_prompt": "Ты профессиональный инструмент для HR специалиста",
        "max_tokens": 100000,
        "temperature": 0.7,
        "n": 1,
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.text}"
