import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="your_database",
    user="your_user",
    password="your_password",
    host="localhost"
)
cursor = conn.cursor()

def insert_employee_data(response, user_id):
    # Добавление краткой сводки в таблицу summary
    summary_text = response['summary']
    cursor.execute(
        "INSERT INTO summary (user_id, context) VALUES (%s, %s)",
        (user_id, summary_text)
    )

    # Добавление параметров в таблицу competencies
    for competency, rating in response['parameters'].items():
        content = f"Оценка {competency} - {rating}"
        cursor.execute(
            "INSERT INTO competencies (user_id, name, rating, content) VALUES (%s, %s, %s, %s)",
            (user_id, competency, rating, content)
        )

    # Добавление сильных сторон в таблицу strength_weak
    for strength in response['strengths']:
        cursor.execute(
            "INSERT INTO strength_weak (user_id, strong_side) VALUES (%s, %s)",
            (user_id, strength)
        )

    # Добавление слабых сторон в таблицу strength_weak
    for weakness in response['weaknesses']:
        cursor.execute(
            "INSERT INTO strength_weak (user_id, weak_side) VALUES (%s, %s)",
            (user_id, weakness)
        )

    # Добавление рекомендаций в таблицу strength_weak
    for recommendation in response['recommendations']:
        cursor.execute(
            "INSERT INTO strength_weak (user_id, recomm) VALUES (%s, %s)",
            (user_id, recommendation)
        )

    # Сохранение изменений
    conn.commit()

# Пример JSON-ответа от ИИ
response = {
    "summary": "Сотрудник демонстрирует высокий уровень профессионализма...",
    "parameters": {
        "Коммуникабельность": 5,
        "Организованность": 4,
        "Профессионализм": 5
    },
    "strengths": [
        "Высокий уровень экспертизы",
        "Отличные коммуникативные навыки"
    ],
    "weaknesses": [
        "Необходимость улучшить делегирование задач"
    ],
    "recommendations": [
        "Пройти курс по управлению проектами"
    ]
}

# Предположим, что user_id уже известен
user_id = 1
insert_employee_data(response, user_id)

# Закрытие соединения
cursor.close()
conn.close()
