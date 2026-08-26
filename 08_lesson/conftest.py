import pytest
from yougile_api import YougileApi


@pytest.fixture
def api():
    base_url = "https://ru.yougile.com"
    api_client = YougileApi(base_url)

    # Укажите здесь ваши реальные данные от аккаунта YouGile
    LOGIN = "ВАШ_ЛОГИН"
    PASSWORD = "ВАШ_ПАРОЛЬ"
    COMPANY_ID = "ВАЩ_ID_КОМПАНИИ"

    # Динамически получаем ключ и передаем его в заголовки
    token = api_client.get_api_key(LOGIN, PASSWORD, COMPANY_ID)
    api_client.set_token(token)

    return api_client


@pytest.fixture
def created_project(api):
    """Фикстура создаёт изолированный проект перед
    тестом и гарантированно удаляет его после."""
    title = "Автотест: Временный проект"
    res = api.create_project(title)
    assert res.status_code == 201
    project_id = res.json()["id"]

    yield {"id": project_id, "title": title}

    api.delete_project(project_id)
