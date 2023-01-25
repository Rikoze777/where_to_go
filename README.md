# Яндекс.Афиша

[Сайт](http://rikoz.pythonanywhere.com) о самых интересных местах в Москве. 


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

[Итоговая страница сайта](http://rikoz.pythonanywhere.com)

## Админка сайта

Для входа в админку для начала нужно вести команду, а после ввести свои данные
```
python3 manage.py createsuperuser
```

В [админке](http://127.0.0.1:8000/admin) доступно ручное добавление и удаление мест, а также изменение очередности фотографий.

## Добавление мест, путем загрузки через JSON файл
```
python3 manage.py load_place <json-url>
```
Где `<json-url>` - это адрес JSON файла, который имеет вид:
```json
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```

