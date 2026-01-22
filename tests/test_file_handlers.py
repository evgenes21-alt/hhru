


import unittest
from data.file_handlers import JSONFileHandler
from data.vacancy import Vacancy
import os

class TestFileHandlers(unittest.TestCase):
    def setUp(self):
        self.filename = 'test_vacancies.json'
        self.handler = JSONFileHandler(self.filename)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_and_load_vacancies(self):
        vacancies = [
            Vacancy(
                title='Разработчик',
                link='https://example.com',
                salary_from=50000,
                salary_to=70000,
                currency='USD',
                description='Опыт работы от 3-х лет'
            ),
            Vacancy(
                title='Менеджер',
                link='https://example.net',
                salary_from=80000,
                salary_to=100000,
                currency='USD',
                description='Высокая зарплата'
            )
        ]
        # Заменяем save_vacancies на save_data
        self.handler.save_data([v.__dict__ for v in vacancies])
        loaded_vacancies = self.handler.load_data()
        self.assertEqual(len(loaded_vacancies), 2)
        self.assertEqual(loaded_vacancies[0]['title'], 'Разработчик')
        self.assertEqual(loaded_vacancies[1]['title'], 'Менеджер')

    def test_delete_data(self):
        vacancies = [
            Vacancy(
                title='Разработчик',
                link='https://example.com',
                salary_from=50000,
                salary_to=70000,
                currency='USD',
                description='Опыт работы от 3-х лет'
            ),
            Vacancy(
                title='Менеджер',
                link='https://example.net',
                salary_from=80000,
                salary_to=100000,
                currency='USD',
                description='Высокая зарплата'
            )
        ]
        # Заменяем save_vacancies на save_data
        self.handler.save_data([v.__dict__ for v in vacancies])
        self.handler.delete_data('1')
        remaining_vacancies = self.handler.load_data()
        self.assertEqual(len(remaining_vacancies), 2)
        self.assertEqual(remaining_vacancies[0]['title'], 'Разработчик')

if __name__ == '__main__':
    unittest.main()