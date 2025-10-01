# Блог система

Веб-приложение для ведения блога с REST API и HTML интерфейсом.

## Функциональность

- Создание, просмотр, редактирование и удаление постов
- Управление пользователями
- REST API для всех операций
- Веб-интерфейс

## Технологии

- FastAPI
- Pydantic
- Jinja2
- Uvicorn

## Скрины проекта на разных этапах работы
<img width="906" height="498" alt="код1" src="https://github.com/user-attachments/assets/d0cccf11-be1c-4afd-85d0-bc523bacea05" />
<img width="953" height="452" alt="код2" src="https://github.com/user-attachments/assets/a61e18ac-3eca-4414-a93a-d9577c85ef9a" />
<img width="350" height="185" alt="код3" src="https://github.com/user-attachments/assets/20ffaa4e-aaf6-4328-8757-ff9e56c8e245" />
<img width="732" height="469" alt="код4" src="https://github.com/user-attachments/assets/1ada42b9-e8ff-4b71-9bec-de2aea08965b" />

## Установка и запуск

1. Установите зависимости:
```bash
pip install -r requirements.txt

2. Запустите сервер
uvicorn app.main:app --reload

3. Откройте в браузере:
http://localhost:8000 - веб-интерфейс
