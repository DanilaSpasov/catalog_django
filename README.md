# Catalog Django Project

## Описание проекта

**catalog_django** — Django-проект, в котором реализовано базовое веб-приложение с простыми страницами и структурой приложения `catalog`.

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
