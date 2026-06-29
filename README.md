# Catalog Django Project

**catalog_django** — Django‑проект, в котором реализовано базовое веб‑приложение с простыми страницами и структурой приложения `catalog`. Проект включает полноценную работу с базой данных на PostgreSQL, модели каталога товаров, админ‑панель с фильтрацией и поиском, а также инструменты для наполнения и сброса данных.

---

## Технологии и стек

- **Фреймворк**: Django 3.14
- **СУБД**: PostgreSQL
- **ORM**: Django ORM (`ForeignKey`, `DecimalField`, `DateTimeField` и др.)
- **Миграции**: `makemigrations` / `migrate`
- **Администрирование**: Django Admin с расширенной настройкой (`list_display`, `list_filter`, `search_fields`)
- **Инструменты**: Django shell, фикстуры, кастомные management‑команды
- **IDE**: PyCharm
- **Контроль версий**: Git, репозиторий на GitHub

---

## База данных и подключение

Проект настроен на работу с PostgreSQL. Подключение задаётся в `settings.py` через параметр `DATABASES`:

Для подключения своих данных установите библиотеку `.dotenv` и в файл `.env` вставьте свои необходимые данные по шаблону из файла `.env_example`. Не забудьте про `SECRET_KEY`!

База данных catalog_django создаётся вручную в PostgreSQL (например, через pgAdmin или psql).

---

## Модели приложения catalog
### Category
* `name` — наименование категории (обязательное).
* `description` — описание категории (необязательное).

### Product
* `name` — наименование товара.
* `description` — описание товара.
* `image` — поле для хранения пути к изображению (можно расширить до ImageField при необходимости).
* `category` — связь «многие к одному» с Category (ForeignKey).
* `price` — цена товара, тип DecimalField(max_digits=10, decimal_places=2) для точной арифметики.
* `created_at` — дата создания (автоматически при создании).
* `updated_at` — дата последнего изменения (обновляется при каждом сохранении).

---

## Администрирование (Django Admin)
Для входа в админку необходимо создать суперпользователя. Модели зарегистрированы в админке с расширенной настройкой:

* Для Category: в списке отображаются id и name.

* Для Product: в списке — id, name, price, category.

* Включена фильтрация продуктов по категории (list_filter).

* Настроен поиск по полям name и description (search_fields).

---

## Фикстуры (fixtures)
Сформированы фикстуры для моделей `Category` и `Product`. Они позволяют быстро восстановить тестовые данные:

```
python manage.py loaddata categories.json
python manage.py loaddata products.json
```

---

### 5. Запуск сервера

```
python manage.py runserver
```

---

## Доступные страницы

После запуска проекта доступны маршруты:

* `/home/` — главная страница
* `/contacts/` — страница контактов
* `/admin/` — панель администратора Django

---

## Основные возможности

### Views

```
def home(request):
    return render(request, "catalog/home.html")

def contacts(request):
    return render(request, "catalog/contacts.html")
```

---

### URL routing

```
urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
]
```

---

### Templates

Шаблоны находятся в:

```
catalog/templates/
```

## Контакты
- Email: spasov2000@mail.ru
