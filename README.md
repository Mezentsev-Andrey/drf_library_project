# Проект "Библиотечное API на Django REST Framework"

## Описание проекта

Этот проект предоставляет API для управления библиотечным каталогом и процессом выдачи книг. API разработан с использованием Django REST Framework и позволяет читателям аутентифицироваться, получать список книг, брать и возвращать книги, а также просматривать список книг, находящихся на руках.

## Основные возможности API

### 1. Аутентификация

- **Поддержка аутентификации по токенам:** в проекте поддерживается аутентификация по токенам JWT.
- **Регистрация пользователя осуществляется:** запрос POST: http://127.0.0.1:8000/users/user/ по `username`, `password`, `role`.
- **Аутентификации пользователя осуществляется:** запрос POST: http://127.0.0.1:8000/users/login/ по `username`, `password`.

### 2. Работа с книгами и связанные с ними запросы в Postman
После аутентификации в качестве читателя становятся доступными:
- **Получение списка книг:** читатель может получить список доступных книг с указанием названия, автора и жанра:
    
    Запрос GET: http://127.0.0.1:8000/books/;
- **Взять книгу:** читатель может взять книгу из библиотеки по её id:
    
    Запрос GET: http://127.0.0.1:8000/books/borrow/{id}/;
- **Вернуть книгу:** читатель может вернуть ранее взятую книгу по её id:
    
    Запрос POST: http://127.0.0.1:8000/books/return/{id}/;
- **Список книг на руках:** читатель может получить список книг, которые находятся у него на руках, с указанием названия, даты взятия и количества дней, сколько книга находится у него:

    Запрос GET http://127.0.0.1:8000/my_books/.

### 3. Администрирование

Администраторы библиотеки могут управлять основной информацией через админ-панель:

- **Пользователи:** просмотр, создание, изменение и удаление пользователей.
- **Книги:** просмотр, создание, изменение и удаление записей о книгах.
- **Списки взятых книг:** просмотр, создание, изменение и удаление записей о том, кто и когда брал книги в библиотеке, с возможностью фильтрации по тем, кто еще не вернул книгу.

## Дополнительные возможности

- **Документация API:** подключена с использованием  `drf-spectacular` и `drf-yasg`.
   Она доступна после запуска сервера по адресам: http://127.0.0.1:8000/redoc/, http://127.0.0.1:8000/swagger/ и http://127.0.0.1:8000/schema/
- **История изменений:** для фиксации истории изменений в моделях книг используется библиотека Django Simple History.

## Установка и настройка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Mezentsev-Andrey/drf_library_project.git

2. Перейдите в директорию проекта:
   ```bash
   cd drf_library_project
   
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt

4. Произведите настройку базы данных PostgreSQL в `settings.py`:

    - POSTGRES_DB=`"имя базы данных"`;
    - POSTGRES_USER=`"пользователь базы данных"`;
    - POSTGRES_PASSWORD=`"пароль базы данных"`;
    - POSTGRES_PORT=`"порт базы данных"`;
    - POSTGRES_HOST=`"хост базы данных"`.
   
5. Выполните миграции базы данных:
   ```bash
   python manage.py migrate

6. Создайте суперпользователя:
   ```bash
   python manage.py createsuperuser
   
7. Запуск приложения:
    - Заполнение базы данных произведено в админке. Загруженные данные представлены по адресу: library/fixtures/all_data.json, library/fixtures/library_data.json; users/fixtures/users_data.json. Для их загрузки в базу данных проекта воспользуйтесь командой: `python manage.py loaddatautf8 all_data.json`
    - Для выгрузки данных из базы данных проекта используйте команду: `python manage.py dumpdatautf8 library --output library/fixtures/library_data.json` (в данном примере команды приведена выгрузка всех данных из приложения library.)

8. Запустите сервер разработки:
   ```bash
   python manage.py runserver

9. Откройте браузер и перейдите по адресу http://127.0.0.1:8000/ для доступа к приложению.
