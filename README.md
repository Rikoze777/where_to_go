# Куда пойти

Cайт о самых интересных местах в Москве. 


## Как установить

* Скачайте репозиторий

* Установите зависимости командой

```
pip install -r requirements.txt
```

* Cоздайте файл .env и записав в нём настройки базы данных с которой предстоит работать.

1. DEBUG=True    ***# True для режима отладки. False - для публикации сайта.***

2. SECRET_KEY='Your project secret key'     ***# Серкретный ключ проекта***

3. ALLOWED_HOSTS='127.0.0.1'        ***# Список адрессов хостов, на которых отображается проект***

4. DATABASE_ENGINE='django.db.backends.sqlite3'

   DATABASE_NAME='db.sqlite3'           ***# По умолчанию база данных - SQLite3.***

Ниже приведены значения, по умолчанию, для значения путей и папок вашей статики и медиа.

5. STATIC_URL = '/static/'          

6. MEDIA_URL = '/media/'            

7. STATICFILES_DIRS = 'assets'      

8. STATIC_ROOT = 'static'

9. MEDIA_ROOT =  'media'

## Приготовление к запуску

```
python3 manage.py makemigrations
python3 manage.py migrate
```

## Запуск проекта

```
python3 manage.py runserver
```

