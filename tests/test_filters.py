import unittest

from data.vacancy import Vacancy
from utils.filters import filter_vacancies, get_top_vacancies


class TestFilters(unittest.TestCase):
    def setUp(self):
        self.vacancies = [
            Vacancy(
                title="A",
                link="https://vacancy1.com",
                salary_from=100000,
                salary_to=120000,
                description="Опыт Python",  # ← теперь здесь описание
                currency="RUB"           # ← теперь здесь валюта
            ),
            Vacancy(
                title="B",
                link="https://vacancy2.com",
                salary_from=80000,
                salary_to=90000,
                description="Опыт Java",
                currency="RUB"
            ),
            Vacancy(
                title="C",
                link="https://vacancy3.com",
                salary_from=150000,
                salary_to=160000,
                description="Python и Django",
                currency="RUB"
            )
        ]

    def test_get_top_vacancies(self):
        top = get_top_vacancies(self.vacancies, 2)
        self.assertEqual(len(top), 2)
        self.assertEqual(top[0].title, "C")
        self.assertEqual(top[1].title, "A")

    def test_filter_vacancies_keywords(self):
        filtered = filter_vacancies(self.vacancies, ["python"])
        self.assertEqual(len(filtered), 2)  # A и C содержат "python"

    def test_filter_case_insensitive(self):
        filtered = filter_vacancies(self.vacancies, ["JAVA"])
        self.assertEqual(len(filtered), 1)  # находит "Java"

if __name__ == '__main__':
    unittest.main()
