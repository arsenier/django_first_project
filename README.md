# Демо-проект по Django

## Установка

### Установка Python

```
sudo apt install python3.12 python3.12-dev python3.12-pip python3.12-venv
```

### Настройка venv и установка зависимостей

```
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Создание миграции (если необходимо)

```
python3 manage.py makemigrations
python3 manage.py migrate
```

### Запуск сервера

```
python3 manage.py runserver
```

После этого по адресу http://127.0.0.1:8000/ вы увидите простую страницу с таблицей сравнения и сеткой контейнеров, а по адресу http://127.0.0.1:8000/advanced/ можно увидеть страничку с бэкэндом, базами данных и другими приколами.