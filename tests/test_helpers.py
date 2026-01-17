import unittest
from utils.helpers import get_top_vacancies, filter_vacancies
from data.vacancy import Vacancy

class TestHelpers(unittest.TestCase):
    def setUp(self):
        self.vacancies = [
            Vacancy('Разработчик', 'https://example.com/job', '100000 руб.', 'опыт работы от 3-х лет'),
            Vacancy('Специалист', 'https://example.com/specialist', '150000 руб.', 'опыт работы от 5-ти лет')
        ]

    def test_get_top_vacancies(self):
        top_vacancies = get_top_vacancies(self.vacancies, 1)
        self.assertEqual(len(top_vacancies), 1)
        self.assertEqual(top_vacancies[0].title, 'Специалист')

    def test_filter_vacancies(self):
        filtered_vacancies = filter_vacancies(self.vacancies, ['3-х'])
        self.assertEqual(len(filtered_vacancies), 1)
        self.assertEqual(filtered_vacancies[0].title, 'Разработчик')

if __name__ == '__main__':
    unittest.main()