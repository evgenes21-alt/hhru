import unittest
from data.vacancy import Vacancy

class TestVacancy(unittest.TestCase):
    def test_create_vacancy(self):
        vacancy = Vacancy('Разработчик', 'https://example.com/job', '100000 руб.', 'опыт работы от 3-х лет')
        self.assertEqual(vacancy.title, 'Разработчик')
        self.assertEqual(vacancy.salary, '100000 руб.')

    def test_comparison(self):
        vacancy1 = Vacancy('Разработчик', 'https://example.com/job', '100000 руб.', 'опыт работы от 3-х лет')
        vacancy2 = Vacancy('Специалист', 'https://example.com/specialist', '150000 руб.', 'опыт работы от 5-ти лет')
        self.assertLess(vacancy1, vacancy2)

if __name__ == '__main__':
    unittest.main()