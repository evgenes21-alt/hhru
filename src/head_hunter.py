from typing import Dict, List

import requests

from data.vacancy import Vacancy
from src.base_api import BaseAPI


# from src.data.vacancy import Vacancy
class HeadHunterAPI(BaseAPI):
    def __init__(self):
        super().__init__("https://api.hh.ru/")

    def connect(self) -> None:
        pass  # Головхантер API не требует аутентификации

    def fetch_data(self, keyword: str) -> List[Dict]:
        params = {"text": keyword}
        response = requests.get(f"{self._base_url}vacancies", params=params)
        response.raise_for_status()
        return response.json()["items"]
