

from dataclasses import dataclass
from typing import Optional


@dataclass
class Vacancy:
    """
    Класс для представления вакансии.

    :ivar title: Название вакансии
    :ivar link: Ссылка на вакансию
    :ivar salary_from: Нижняя граница зарплаты
    :ivar salary_to: Верхняя граница зарплаты
    :ivar currency: Валюта зарплаты
    """
    title: str
    link: str
    salary_from: Optional[int]
    salary_to: Optional[int]
    description: str
    currency: Optional[str] = ""

    def __post_init__(self):

        # 1. Проверка, что description — строка
        if not isinstance(self.description, str):
            raise ValueError("Описание должно быть строкой")

        # 2. Очищаем от пробелов и проверяем на пустоту
        self.description = self.description.strip()
        if not self.description:  # если пусто после strip()
            self.description = "Описание отсутствует"
        """
        Проверяет валидность полей при инициализации.
        """
        self._validate_title()
        self._validate_link()
        self._validate_currency()
        if not isinstance(self.description, str):
            raise ValueError("Описание должно быть строкой")



    def __lt__(self, other):
        """
        Сравнивает вакансии по нижней границе зарплаты.
        Если зарплата не указана, считается минимальной (-inf).

        :param other: Другая вакансия для сравнения
        :return: True, если эта вакансия дешевле другой
        """
        if self.salary_from is None:
            return True
        if other.salary_from is None:
            return False
        return self.salary_from < other.salary_from

    def _validate_title(self):
        """
        Проверяет, что название вакансии не пустое.
        """
        if not self.title.strip():
            raise ValueError("Название вакансии не может быть пустым")

    def _validate_link(self):
        """
        Проверяет, что ссылка начинается с HTTP(S).
        """
        if not self.link.startswith(('http:', 'https:')):
            raise ValueError("Ссылка должна начинаться с http или https")



    def _validate_currency(self):
        if self.currency:
            valid_currencies = {"USD", "EUR", "RUB"}
            if self.currency.upper() not in valid_currencies:
                raise ValueError(f"Валютой может быть только USD, EUR или RUB, а не {self.currency}")