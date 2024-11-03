import json
import requests

def prepare_prompt(reviews):
    # Декларация полей
    field_definitions = (
        "Поля для сводки в формате JSON:\n"
        "1. summary: Краткое описание сотрудника на основе отзывов. Строка.\n"
        "2. parameters: Оценки ключевых параметров сотрудника. Объект со следующими полями:\n"
        "   - Коммуникабельность: Оценка от 1 до 5\n"
        "   - Ответственность: Оценка от 1 до 5\n"
        "   - Дополнительные параметры также принимаются с оценками от 1 до 5\n"
        "3. strengths: Сильные стороны сотрудника. Массив строк.\n"
        "4. weaknesses: Слабые стороны сотрудника. Массив строк.\n"
        "5. recommendations: Рекомендации по улучшению. Массив строк.\n"
    )

    # Инструкции и формат JSON
    instructions = (
        "Ты профессиональный HR-специалист.\n"
        "Вот определенное количество отзывов о сотруднике:\n\n"
    )

    # Добавляем отзывы в промпт
    for i, review in enumerate(reviews, start=1):
        instructions += f"Отзыв {i}:\n{review[2]}\n\n"

    instructions += f"user_id: {reviews[1][1]}\n"

    # Упоминание формата JSON и требование строго следовать структуре
    instructions += (
        "На основе этих отзывов нужно создать подробную сводку в формате JSON, используя следующие поля:\n\n"
        '  "user_id": "",\n'
        '  "role": "Предположительная роль сотрудника только 1 вариант",\n'
        + field_definitions +
        "\nСгенерируй JSON-объект, который строго следует указанной структуре. Пример:\n\n"
        "{\n"
        '  "summary": "Краткое описание сотрудника",\n'
        '  "parameters": {\n'
        '      "Коммуникабельность": 5,\n'
        '      "Ответственность": 4,\n'
        '      // Дополнительные параметры\n'
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
        "Пожалуйста, соблюдай формат JSON и используй кодировку UTF-8. Работай только с текущими данными, не учитывая контекст прошлых ответов."
        "Также, прошу заполнить все пункты, weakness и recommendations в том числе, даже если нечего добавить, то добавь что нибудь пожалуйста, это важно!"
    )

    return instructions

def process_lama(prompt):
    url = "https://vk-scoreworker-case.olymp.innopolis.university/generate"

    # Регулярное выражение для валидации JSON-ответа
    regex_pattern = r'^\{\s*"summary":\s*".+?",\s*"parameters":\s*\{(?:\s*".+?":\s*[1-5],?\s*)+\},\s*"strengths":\s*\[.+?\],\s*"weaknesses":\s*\[.+?\],\s*"recommendations":\s*\[.+?\]\s*\}$'

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
