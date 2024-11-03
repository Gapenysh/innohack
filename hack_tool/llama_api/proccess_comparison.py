import json

import requests


def prepare_prompt_comparison(data1, data2):
    if data1[0] == data2[0]:  # проверка, чтобы убедиться, что это разные пользователи
        return None

    # Формируем инструкции для HR-специалиста
    instructions = "Ты профессиональный HR-специалист.\nУ тебя есть сводка и характеристики двух работников:\n\n"
    instructions += "На основе данных двух описаний сотрудников определи, кто из них будет компетентнее. "
    instructions += "Опиши, какие качества могут сыграть решающую роль в выборе именно этого сотрудника.\n"
    instructions += "Вот исходные данные:\n\n"

    # Преобразуем данные сотрудников в формат JSON для удобного вывода
    data1_str = json.dumps(data1, ensure_ascii=False, indent=2)
    data2_str = json.dumps(data2, ensure_ascii=False, indent=2)

    # Добавляем данные в инструкции
    instructions += f"Данные сотрудника 1:\n{data1_str}\n\n"
    instructions += f"Данные сотрудника 2:\n{data2_str}\n"

    return instructions


def process_lama_comparison(prompt):
    url = "https://vk-scoreworker-case.olymp.innopolis.university/generate"

    # Регулярное выражение для валидации JSON-ответа
    regex_pattern = r'^\{\s*"summary":\s*".+?",\s*"parameters":\s*\{(?:\s*".+?":\s*[1-5],?\s*)+\},\s*"strengths":\s*\[.+?\],\s*"weaknesses":\s*\[.+?\],\s*"recommendations":\s*\[.+?\]\s*\}$'

    data = {
        "prompt": [prompt],
        "apply_chat_template": True,
        "system_prompt": "Ты профессиональный инструмент для HR специалиста",
        "max_tokens": 10000,
        "temperature": 0.5,
        "n": 3,
        "best_of": 3
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