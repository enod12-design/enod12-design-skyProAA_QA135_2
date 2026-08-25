import requests


class YougileApi:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Content-Type": "application/json"
        }

    def get_token(self, login: str, password: str) -> str:
        """[POST] /api-v2/auth/keys/get — получение токена авторизации"""
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(
            f"{self.base_url}/api-v2/auth/keys/get", json=payload
        )

        # Проверяем успешный ответ
        if response.status_code in (200, 201):
            token = response.json()[0]["key"]
            self.headers["Authorization"] = f"Bearer {token}"
            return token
        return None

    def create_project(self, title: str):
        """[POST] /api-v2/projects"""
        payload = {"title": title}
        return requests.post(
            f"{self.base_url}/api-v2/projects",
            json=payload,
            headers=self.headers
        )

    def get_project_by_id(self, project_id: str):
        """[GET] /api-v2/projects/{id}"""
        return requests.get(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=self.headers
        )

    def update_project(self, project_id: str, title: str):
        """[PUT] /api-v2/projects/{id}"""
        payload = {"title": title}
        return requests.put(
            f"{self.base_url}/api-v2/projects/{project_id}",
            json=payload,
            headers=self.headers
        )
