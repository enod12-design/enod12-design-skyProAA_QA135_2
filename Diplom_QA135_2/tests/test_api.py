import requests
import pytest
import allure
from config import BASE_URL_API

pytestmark = pytest.mark.api


# Тест 1
@allure.story("Поиск фильмов")
@allure.title("Позитивный тест: Поиск фильма по названию")
def test_api_search_by_name(api_headers: dict[str, str]) -> None:
    with allure.step("Отправка запроса на поиск фильма по названию"):
        params: dict[str, str] = {"query": "Мстители: Война бесконечности"}
        response = requests.get(
            url=f"{BASE_URL_API}/movie/search", headers=api_headers,
            params=params
        )

    with allure.step("Проверка статуса ответа и структуры данных"):
        assert response.status_code == 200
        data = response.json()
        assert "docs" in data
        assert isinstance(data["docs"], list)
        assert len(data["docs"]) > 0


# Тест 2
@allure.story("Фильтрация фильмов")
@allure.title("Позитивный тест: Фильтрация по году выпуска")
def test_api_filter_by_year(api_headers: dict[str, str]) -> None:
    with allure.step("Отправка запроса с фильтром по году (2018)"):
        params: dict[str, str] = {"year": "2018"}
        response = requests.get(
            url=f"{BASE_URL_API}/movie", headers=api_headers, params=params
        )

    with allure.step("Проверка статус-кода и времени ответа"):
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 2.0


# Тест 3
@allure.story("Поиск персон")
@allure.title("Позитивный тест: Поиск актера/режиссера (параметризованный)")
@pytest.mark.parametrize(
    "person_name", ["Роберт Дауни мл.", "Кристофер Нолан"]
)
def test_api_search_person(
    api_headers: dict[str, str], person_name: str
) -> None:
    with allure.step(f"Отправка запроса на поиск персоны: {person_name}"):
        params: dict[str, str] = {"query": person_name}
        response = requests.get(
            url=f"{BASE_URL_API}/person/search", headers=api_headers,
            params=params
        )

    with allure.step("Проверка успешности ответа и наличия результатов"):
        assert response.status_code == 200
        assert len(response.json().get("docs", [])) > 0


# Тест 4
@allure.story("Безопасность и авторизация")
@allure.title("Негативный тест: Запрос без API-ключа")
def test_api_unauthorized_access() -> None:
    with allure.step("Отправка запроса без заголовков авторизации"):
        response = requests.get(f"{BASE_URL_API}/movie/search?query=test")

    with allure.step("Проверка ограничения доступа (код 401 или 403)"):
        assert response.status_code in [401, 403]


# Тест 5
@allure.story("Валидация параметров")
@allure.title("Негативный тест: Поиск с пустым параметром query")
def test_api_search_empty_query(api_headers: dict[str, str]) -> None:
    with allure.step("Отправка запроса с пустым параметром query"):
        params: dict[str, str] = {"query": ""}
        response = requests.get(
            url=f"{BASE_URL_API}/movie/search", headers=api_headers,
            params=params
        )

    with allure.step(
            "Проверка корректности обработки пустого запроса сервером"
    ):
        assert response.status_code in [400, 422, 200]
        if response.status_code == 200:
            assert "docs" in response.json()
