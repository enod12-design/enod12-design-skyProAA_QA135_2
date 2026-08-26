import requests


class YougileApi:

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.headers = {"Content-Type": "application/json"}

    def get_api_key(self, login: str, password: str, company_id: str) -> str:
        """Получает список API-ключей или
        создает новый через логин и пароль."""
        url = f"{self.base_url}/api-v2/auth/keys"
        payload = {
            "login": login,
            "password": password,
            "companyId": company_id
        }
        response = requests.post(
            url, json=payload, headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        # Вызовет ошибку, если логин/пароль неверные

        # Эндпоинт возвращает список ключей [{'name': '...', 'key': '...'}]
        # Забираем строку самого ключа из первого элемента списка
        keys_list = response.json()
        if isinstance(keys_list, list) and len(keys_list) > 0:
            return keys_list[0]["key"]
        elif isinstance(keys_list, dict) and "key" in keys_list:
            return keys_list["key"]
        else:
            raise ValueError("Не удалось извлечь API-ключ из ответа сервера")

    def set_token(self, token: str):
        """Установка токена авторизации в заголовки."""
        self.headers["Authorization"] = f"Bearer {token}"

    def create_project(self, title: str):
        url = f"{self.base_url}/api-v2/projects"
        payload = {"title": title}
        return requests.post(url, json=payload, headers=self.headers)

    def get_project_by_id(self, project_id: str):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        return requests.get(url, headers=self.headers)

    def update_project(self, project_id: str, title: str):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        payload = {"title": title}
        return requests.put(url, json=payload, headers=self.headers)

    def delete_project(self, project_id: str):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        return requests.delete(url, headers=self.headers)
