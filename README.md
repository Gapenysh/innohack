 # Система для генерации коротких сводок о человеке на основе отзывов

## Описание

Это система, позволяющая получать короткие сводки, рекомендации и оценки работника путем обработки отзывов о сотруднике 

## Технологический стек

- Python (3.12)
- Flask(фреймворк для бэкэнд части системы)
- psycopg2 (для работы с PostgreSQL)
- Poetry (для управления зависимостями)
- заранее обученная языковая модель llama 3.1 70b


## Как запустить проект

1. Клонируйте репозиторий:

   git clone https://github.com/Gapenysh/innohack.git
    

2. Инициализируйте Poetry:

    
   poetry install
    

3. Cоздайте файл .env добавьте необходимые переменные окружения вида:

USER=
PASSWORD=
HOST_NAME=
DB_NAME=


4. Запустите программу через файл run:

run python run.py

5. Описание основных URL маршрутов для работы со системой

'/profile/<int:user_id>', methods=['GET'] - выводит все данные, сгенерированные llama

"/comparison", methods=["GET"] - из базы данных отправляются данные для двух работников

"/comparison/ai", methods=["GET"]) - сравнение двух работников с использованием llama

6. После запуска сервер будет доступен по ссылке http://localhost:5000
7. Для проверки работы программы с базой данных сделайте restore и выберите файл 'innohack5' из репозитория в приложении pgadmin4
## Команда авторов

- Инсаф Ахметзянов 
- Булат Хайруллин
- Рамзиль Абдуллин 

## Лицензия

Этот проект лицензирован под [MIT License](LICENSE).
