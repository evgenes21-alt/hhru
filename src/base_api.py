
"""
Базовый абстрактный класс для работы с API сервисов вакансий.
"""


from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """
    Абстрактный класс для работы с API вакансий.

    :ivar base_url: Базовый URL API
    """

    def __init__(self, base_url: str):
        """
        Инициализирует экземпляр класса с базовым URL.

        :param base_url: Базовый URL API
        """
        self.base_url = base_url

    @abstractmethod
    def fetch_data(self, keyword: str, page: int = 1, per_page: int = 10) -> list:
        """
        Загружает данные о вакансиях по ключевому слову.

        :param keyword: Ключевое слово для поиска
        :param page: Номер страницы (по умолчанию 1)
        :param per_page: Количество вакансий на странице (по умолчанию 10)
        :return: Список словарей с результатами поиска
        """
        pass