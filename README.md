# Skymarket (EN)

## Project Description
Skymarket is a non-commercial open-source project, a Single Page Application (SPA) web application, backend for an online classifieds platform.

## Project Idea
The main goal of the project is to create a convenient online platform for posting classified ads of any category, providing users with easy access, efficient interaction, and reliable security.

## Project Functionalities
- The application provides a Full REST API using Django Rest Framework.
- Authorization is done through JWT token mechanism.
- PostgresQL relational database is used for data storage.
- Ad model, Comment model, and custom User model are implemented.
- Data pagination is implemented.
- Password recovery via Email is provided.
- The project uses Docker-compose for containerization, with each server being individually configured.
- Asynchronous tasks are handled through Celery with Redis as the broker.
- CORS settings are configured for security.
- Project settings and dependencies can be found in the `requirements.txt` file.
- Sample environment variables for quick local deployment are provided in the `.env.sample` file.
- Swagger and Redoc are used for API documentation following the OpenAPI standard.
- Flake8 report and test coverage report are included.

## Running the Project:
1) Create a `.env` file in the project root following the `.env.sample` file template.
2) Enter `docker compose up --build` in the console.



# Skymarket (RUS)

## Описание проекта
Skymarket - некоммерческий open-source проект, веб-приложение SPA (Single Page Application), бэкенд для онлайн-платформы объявлений. 

## Идея проекта
Главная цель проекта — создать удобную онлайн-платформу для размещения объявлений любой тематики, обеспечивая пользователям простой доступ, эффективное взаимодействие и надежную безопасность.

## Функциональности проекта
- Приложение предоставляет Full REST API, используя Django Rest Framework.
- Авторизация осуществляется через механизм токенов JWT.
- Для хранения данных используется реляционная база данных PostgresQL.
- Модель объявления (Ad), модель комментария (Comment) и кастомная модель пользователя (User).
- Реализованны пагинация данных. 
- Возможность восстановлением пароля через электронную почту.
- Проект использует Docker-compose для контейнеризации, при этом каждый сервер настраивается индивидуально.
- Асинхронные задачи через Celery с брокером Redis.
- Настройки CORS для обеспечения безопасности.
- Настройки и зависимости проекта можно найти в файле `requirements.txt`.
- Примеры переменных окружения для быстрого разворачивания проекта локально представлены в файле `.env.sample`.
- Использование Swagger и Redoc для документации API по стандарту OpenAPI.
- Присутствуют отчет flake8 и отчет покрытия тестами.

## Запуск проекта:
1) В корне проекта создайте файл `.env` по образцу файла `.env.sample`.
2) Введите в консоль `docker compose up --build`
