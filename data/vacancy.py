from dataclasses import dataclass
from typing import Optional, Union
import re

@dataclass
class Vacancy:
    title: str
    link: str
    salary: Optional[Union[int, str]]
    description: str

    def normalize_salary(self) -> Optional[int]:
        """
        Приводит зарплату к числовому значению для корректного сравнения.
        Если зарплата не указана, возвращает None.
        """
        if isinstance(self.salary, int):
            return self.salary
        elif isinstance(self.salary, str):
            # Парсим зарплату, оставляя только числа
            match = re.search(r"\d+", self.salary)
            if match:
                return int(match.group())
        return None

    def __lt__(self, other):
        """
        Сравнивает вакансии по зарплате. Если зарплата неизвестна,
        считается самой низкой среди остальных.
        """
        my_salary = self.normalize_salary() or 0
        other_salary = other.normalize_salary() or 0
        return my_salary < other_salary

    def validate(self):
        """
        Проверяет наличие всех важных полей.
        """
        if not all((self.title, self.link, self.description)):
            raise ValueError("Недостаточно данных для вакансии.")
        if self.salary is None:
            raise ValueError("Зарплата не указана.")