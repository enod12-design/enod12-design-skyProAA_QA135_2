Инструкция по запускaм и отчетам:
# Проект автотестов Selenium + Pytest + Allure

## Установка зависимостей
```bash
pip install -r requirements.txt

Запуск тестов для формирования отчета Allure
Для запуска тестов и сохранения результатов во временную папку allure-results:
pytest --alluredir=allure-results

Просмотр сформированного отчета
Чтобы сгенерировать и открыть отчет Allure в браузере:
allure serve allure-results
