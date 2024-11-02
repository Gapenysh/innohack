
import json

import requests

def prepare_prompt(reviews):
    prompt = (
        "Ты профессиональный HR-специалист.\n"
        "Вот несколько отзывов о сотруднике:\n\n"
    )

    # Добавляем отзывы в формате "Отзыв 1:", "Отзыв 2:" и так далее
    for i, review in enumerate(reviews, start=1):
        prompt += f"Отзыв {i}:\n{review[2]}\n\n"

    # Инструкции по созданию структурированной сводки в формате JSON
    prompt += (
        "На основе этих отзывов нужно создать подробную сводку в формате JSON, "
        "чтобы она включала ключевые параметры, сильные и слабые стороны, и рекомендации.\n\n"
        "Используй следующий формат JSON:\n\n"
        "{\n"
        '  "summary": "Краткое описание сотрудника",\n'
        '  "parameters": {\n'
        '      "Коммуникабельность": <rating>,\n'
        '      "Организованность": <rating>,\n'
        '      "Профессионализм": <rating>\n'
        '      // и другие параметры с оценками от 1 до 5\n'
        "  },\n"
        '  "strengths": [\n'
        '      "Сильная сторона 1",\n'
        '      "Сильная сторона 2"\n'
        "  ],\n"
        '  "weaknesses": [\n'
        '      "Слабая сторона 1",\n'
        '      "Слабая сторона 2"\n'
        "  ],\n"
        '  "recommendations": [\n'
        '      "Рекомендация 1",\n'
        '      "Рекомендация 2"\n'
        "  ]\n"
        "}\n\n"
        "Пожалуйста, строго соблюдай этот формат JSON и следуй структуре, чтобы все данные были корректно записаны."
    )

    return prompt

def proccess_lama(prompt):


    url = "https://vk-scoreworker-case.olymp.innopolis.university/generate"
    data = {
        "prompt": [prompt],
        "apply_chat_template": True,
        "system_prompt": "Вы полезный помощник.",
        "max_tokens": 5000,
        "n": 1,
        "temperature": 0.7
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
