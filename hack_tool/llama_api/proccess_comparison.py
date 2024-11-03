import json
import requests

def prepare_prompt_comparison(summary):

    field_definitions = (
        "Поля для текста сравнения в формате JSON:\n"
        "1. comparison: Сравнение двух специалистов и определение лучшего по его сводкам и качествам.Строка.\n"
    )


    instructions = (
        "Ты профессиональный HR-специалист.\n"
        "У тебя сводка и характеристики двух работников:\n\n"
        "Если сравниваются два одинаковых сотрудника (то есть id сотрудников одинаковы), пиши, что сравнение невозможно, так как сравниваются одинаковые сотрудники."
    )
    instructions += "На основе данных двух описаний сотрудников определи, кто из них будет компетентнее. Опиши какие качества могут сыграть решающую роль в выборе именно этого сотрудника"
    instructions += summary
    instructions += field_definitions

    return instructions

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
