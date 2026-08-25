import pytest
from yougile_api import YougileApi

# Инициализация API
api = YougileApi("https://ru.yougile.com")
LOGIN = "ВАШ ЛОГИН"
PASSWORD = "ВАШ ПАРОЛЬ"


@pytest.fixture(autouse=True)
def setup_auth():
    """Фикстура для автоматической авторизации перед каждым тестом"""
    api.get_token(LOGIN, PASSWORD)


def test_create_project():
    """Тест создания проекта (позитивный)"""
    title = "Новый тестовый проект"
    response = api.create_project(title)

    assert response.status_code == 201
    data = response.json()
    assert "id" in data

    # Сохраняем id для последующих проверок при необходимости
    return data["id"]


def test_get_project_by_id():
    """Тест получения проекта по ID (позитивный)"""
    # 1. Создаем проект, чтобы было что получать
    create_res = api.create_project("Проект для чтения")
    project_id = create_res.json()["id"]

    # 2. Запрашиваем проект по ID
    response = api.get_project_by_id(project_id)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id
    assert data["title"] == "Проект для чтения"


def test_update_project():
    """Тест обновления названия проекта (позитивный)"""
    # 1. Создаем проект
    create_res = api.create_project("Старое название")
    project_id = create_res.json()["id"]

    # 2. Обновляем название
    new_title = "Обновленное название"
    response = api.update_project(project_id, new_title)

    assert response.status_code == 200

    # 3. Проверяем, что название действительно изменилось
    get_res = api.get_project_by_id(project_id)
    assert get_res.json()["title"] == new_title


def test_get_project_not_found():
    """Негативный тест: запрос несуществующего проекта"""
    non_existent_id = "00000000-0000-0000-0000-000000000000"
    response = api.get_project_by_id(non_existent_id)

    assert response.status_code == 404
