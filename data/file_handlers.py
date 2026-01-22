import json
from abc import ABC, abstractmethod
from typing import Dict, List

from data.vacancy import Vacancy


class BaseFileHandler(ABC):
    """
    Абстрактный класс для работы с файлами.

    :ivar filepath: Путь к файлу
    """

    def __init__(self, filepath: str):
        """
        Инициализирует экземпляр класса с путем к файлу.

        :param filepath: Путь к файлу
        """
        self.filepath = filepath

    @abstractmethod
    def load_data(self) -> List[Dict]:
        """
        Загружает данные из файла.
        """
        pass

    @abstractmethod
    def save_data(self, data: List[Dict]) -> None:
        """
        Сохраняет данные в файл.
        """
        pass

    @abstractmethod
    def delete_data(self, identifier: str) -> None:
        """
        Удаляет данные из файла по уникальному идентификатору.
        """
        pass


class JSONFileHandler(BaseFileHandler):
    """
    Класс для работы с JSON-файлами.
    """

    def load_data(self) -> List[Dict]:
        """
        Загружает данные из JSON-файла.
        """
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self, data: List[Dict]) -> None:
        """
        Сохраняет данные в JSON-файл.
        """
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_data(self, identifier: str) -> None:
        """
        Удаляет данные из JSON-файла по уникальному идентификатору.
        """
        data = self.load_data()
        updated_data = [entry for entry in data if entry.get('id') != identifier]
        self.save_data(updated_data)