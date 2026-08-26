# --- ПОЗИТИВНЫЕ ТЕСТЫ ---
def test_create_project(api):
    """Позитивный тест: Создание проекта (POST)."""
    title = "Тестовый проект"
    response = api.create_project(title)

    assert response.status_code == 201
    data = response.json()
    assert "id" in data

    # Удаляем созданный в тесте объект для соблюдения чистоты
    api.delete_project(data["id"])


def test_get_project_by_id(api, created_project):
    """Позитивный тест: Получение проекта по ID (GET)."""
    project_id = created_project["id"]

    response = api.get_project_by_id(project_id)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id
    assert data["title"] == created_project["title"]


def test_update_project(api, created_project):
    """Позитивный тест: Обновление названия проекта (PUT)."""
    project_id = created_project["id"]
    new_title = "Обновленное название"

    response = api.update_project(project_id, new_title)
    assert response.status_code == 200

    # Проверяем, что изменения применились
    get_res = api.get_project_by_id(project_id)
    assert get_res.json()["title"] == new_title


# --- НЕГАТИВНЫЕ ТЕСТЫ ---


def test_get_project_not_found(api):
    """Негативный тест GET: Запрос несуществующего проекта."""
    non_existent_id = "00000000-0000-0000-0000-000000000000"
    response = api.get_project_by_id(non_existent_id)

    assert response.status_code == 404


def test_create_project_empty_title(api):
    """Негативный тест POST: Попытка создания проекта с пустым названием."""
    response = api.create_project("")

    assert response.status_code == 400


def test_update_non_existent_project(api):
    """Негативный тест PUT: Попытка обновления несуществующего проекта."""
    non_existent_id = "00000000-0000-0000-0000-000000000000"
    response = api.update_project(non_existent_id, "Новое название")

    assert response.status_code == 404
