import pytest
from sqlalchemy import text

TEST_SUBJECT_ID = 1211


@pytest.fixture(autouse=True)
def cleanup(db_connection):
    # 1. Очищаем данные до теста
    db_connection.execute(
        text("DELETE FROM subject WHERE subject_id = :id"),
        {"id": TEST_SUBJECT_ID}
    )
    yield

    # 2. Очищаем данные после теста
    db_connection.execute(
        text("DELETE FROM subject WHERE subject_id = :id"),
        {"id": TEST_SUBJECT_ID}
    )


def test_add_subject(db_connection):
    """Тест 1: Добавление нового предмета (INSERT)"""
    title = "Автотестирование Python"

    db_connection.execute(
        text("INSERT INTO subject (subject_id, subject_title) "
             "VALUES (:id, :title)"),
        {"id": TEST_SUBJECT_ID, "title": title}
    )

    result = db_connection.execute(
            text("SELECT * FROM subject WHERE subject_id = :id"),
            {"id": TEST_SUBJECT_ID}
    ).fetchone()

    assert result is not None, "Запись не была найдена в БД после INSERT"
    assert result[1] == title, f"Ожидалось имя {title}, получено {result[1]}"


def test_update_subject(db_connection):
    """Тест 2: Изменение предмета (UPDATE)"""
    initial_title = "Автотестирование Python"
    update_title = "Обновлённое автотестирование Python"

    db_connection.execute(
        text("INSERT INTO subject (subject_id, subject_title) "
             "VALUES (:id, :title)"),
        {"id": TEST_SUBJECT_ID, "title": initial_title}
    )

    db_connection.execute(
        text("UPDATE subject SET subject_title = :title "
             "WHERE subject_id = :id"),
        {"id": TEST_SUBJECT_ID, "title": update_title}
    )

    result = db_connection.execute(
        text("SELECT subject_title FROM subject WHERE subject_id = :id"),
        {"id": TEST_SUBJECT_ID}
    ).fetchone()

    assert result is not None
    assert result[0] == update_title, \
        f"Ожидалось {update_title}, но получи {result[0]}"


def test_delete_subject(db_connection):
    """Тест 3: Удаление предмета (DELETE)"""
    title = "Предмет для удаления"

    db_connection.execute(
        text("INSERT INTO subject (subject_id, subject_title) "
             "VALUES (:id, :title)"),
        {"id": TEST_SUBJECT_ID, "title": title}
    )

    db_connection.execute(
        text("DELETE FROM subject WHERE subject_id = :id"),
        {"id": TEST_SUBJECT_ID}
    )

    result = db_connection.execute(
        text("SELECT * FROM subject WHERE subject_id = :id"),
        {"id": TEST_SUBJECT_ID}
    ).fetchone()

    assert result is None, "Запись всё ещё существует в БД после DELETE"
