import json
import requests

def prepare_prompt(reviews):
    field_definitions = (
        "Поля для сводки в формате JSON:\n"
        "1. summary: Краткое описание сотрудника на основе отзывов. Строка.\n"
        "2. parameters: Оценки ключевых параметров сотрудника. Объект, где каждый параметр представлен объектом с полями:\n"
        "   - rating: Оценка от 1 до 5\n"
        "   - description: Краткая характеристика, описывающая данный параметр на основе оценки и отзывов.\n"
        "3. strengths: Сильные стороны сотрудника. Массив строк.\n"
        "4. weaknesses: Слабые стороны сотрудника. Массив строк.\n"
        "5. recommendations: Рекомендации по улучшению. Массив строк.\n"
    )

    instructions = (
        "Ты профессиональный HR-специалист.\n"
        "Вот определенное количество отзывов о сотруднике:\n\n"
    )

    if not reviews:
        return "Нет отзывов для анализа."

    for i, review in enumerate(reviews, start=1):
        if review[2].strip():  # Проверка на пустые отзывы
            instructions += f"Отзыв {i}:\n{review[2]}\n\n"

    instructions += f"user_id: {reviews[0][1]}\n"

    instructions += (
        "На основе этих отзывов нужно создать подробную сводку в формате JSON, используя следующие поля:\n\n"
        '  "user_id": "",\n'
        '  "role": "Предположительная роль сотрудника только 1 вариант",\n'
        + field_definitions +
        "\nСгенерируй JSON-объект, который строго следует указанной структуре. Пример:\n\n"
        "{\n"
        '  "summary": "Краткое описание сотрудника",\n'
        '  "parameters": {\n'
        '      "Коммуникабельность": {\n'
        '          "rating": 5,\n'
        '          "description": "Отличные навыки общения, легко взаимодействует с коллегами."\n'
        '      },\n'
        '      "Ответственность": {\n'
        '          "rating": 4,\n'
        '          "description": "Ответственный и надежный сотрудник, почти всегда выполняет задачи в срок."\n'
        '      }\n'
        '      // Другие параметры\n'
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
        "Пожалуйста, соблюдай формат JSON и используй кодировку UTF-8. Работай только с текущими данными, не учитывая контекст прошлых ответов. "
        "Также, прошу заполнить все пункты, включая weakness и recommendations, даже если нечего добавить. Это важно!\n"
        "Прошу объективно оценивать, чтобы избежать предвзятости в присвоении премии. Если отзыв несет негативный контекст, "
        "учти это при оценке, если ты видишь негативную оценку, то пусть это влияет на окончательный ответ, пожалуйста.\n"
    )

    return instructions


def proccess_lama(prompt):
    url = "https://vk-scoreworker-case.olymp.innopolis.university/generate"

    # Регулярное выражение для валидации JSON-ответа
    regex_pattern = r'^\{\s*"summary":\s*".+?",\s*"parameters":\s*\{(?:\s*".+?":\s*[1-5],?\s*)+\},\s*"strengths":\s*\[.+?\],\s*"weaknesses":\s*\[.+?\],\s*"recommendations":\s*\[.+?\]\s*\}$'

    data = {
        "prompt": [prompt],
        "apply_chat_template": True,
        "system_prompt": "Ты профессиональный инструмент для HR специалиста",
        "max_tokens": 100000,
        "temperature": 0.7,
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
