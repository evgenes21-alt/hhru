from abc import ABC, abstractmethod


class BaseAPI(ABC):
    def __init__(self, base_url: str):
        self._base_url = base_url

    @abstractmethod
    def connect(self) -> None:
        """Подключение к API"""
        pass

    @abstractmethod
    def fetch_data(self, keyword: str) -> list:
        """Загрузка данных о вакансиях"""
        pass
