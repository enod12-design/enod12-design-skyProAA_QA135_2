import requests
import pytest
from config import BASE_URL_API


# 1. Позитивный: Поиск по названию
def test_api_search_by_name(api_headers: dict[str, str]) -> None:
    params: dict[str, str] = {"query": "Мстители: Война бесконечности"}
    response = requests.get(f"{BASE_URL_API}/movie/search", headers=api_headers, params=params)

    assert response.status_code == 200
    data = response.json()
    assert "docs" in data
    assert isinstance(data["docs"], list)
    assert len(data["docs"]) > 0


# 2. Позитивный: Фильтрация по году выпуска
def test_api_filter_by_year(api_headers: dict[str, str]) -> None:
    params: dict[str, str] = {"year": "2018"}
    response = requests.get(f"{BASE_URL_API}/movie", headers=api_headers, params=params)

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2.0


# 3. Позитивный: Поиск актера/режиссера по имени (Параметризованный)
@pytest.mark.parametrize("person_name", ["Роберт Дауни мл.", "Кристофер Нолан"])
def test_api_search_person(api_headers: dict[str, str], person_name: str) -> None:
    params: dict[str, str] = {"query": person_name}
    response = requests.get(f"{BASE_URL_API}/person/search", headers=api_headers, params=params)

    assert response.status_code == 200
    assert len(response.json().get("docs", [])) > 0


# 4. Негативный: Запрос без API-ключа
def test_api_unauthorized_access() -> None:
    response = requests.get(f"{BASE_URL_API}/movie/search?query=test")
    assert response.status_code in [401, 403]


# 5. Негативный: Поиск с пустым параметром query
def test_api_search_empty_query(api_headers: dict[str, str]) -> None:
    params: dict[str, str] = {"query": ""}
    response = requests.get(f"{BASE_URL_API}/movie/search", headers=api_headers, params=params)

    assert response.status_code in [400, 422, 200]
    if response.status_code == 200:
        assert len(response.json().get("docs", [])) == 0

