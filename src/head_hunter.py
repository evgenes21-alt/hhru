


from typing import Dict, List

import requests

from src.base_api import BaseAPI


class HeadHunterAPI(BaseAPI):
    """
    Класс для работы с API HeadHunter.

    :ivar base_url: Базовый URL API HeadHunter
    """

    def __init__(self):
        """
        Инициализирует экземпляр класса HeadHunterAPI.
        """
        super().__init__('https://api.hh.ru/')

    def fetch_data(self, keyword: str, page: int = 1, per_page: int = 10) -> List[Dict]:
        """
        Загружает данные о вакансиях по ключевому слову.

        :param keyword: Ключевое слово для поиска
        :param page: Номер страницы (по умолчанию 1)
        :param per_page: Количество вакансий на странице (по умолчанию 10)
        :return: Список словарей с результатами поиска
        """
        params = {"text": keyword, "page": page, "per_page": per_page}
        response = requests.get(f"{self.base_url}/vacancies", params=params)
        response.raise_for_status()
        return response.json()['items']