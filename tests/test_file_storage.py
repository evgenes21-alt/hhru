import unittest
from data.file_storage import FileStorage
from data.vacancy import Vacancy

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage('test_vacancies.json')
        self.vacancies = [
            Vacancy('Разработчик', 'https://example.com/job', '100000 руб.', 'опыт работы от 3-х лет'),
            Vacancy('Специалист', 'https://example.com/specialist', '150000 руб.', 'опыт работы от 5-ти лет')
        ]

    def tearDown(self):
        import os
        if os.path.exists('test_vacancies.json'):
            os.remove('test_vacancies.json')

    def test_save_and_load_vacancies(self):
        self.storage.save_vacancies(self.vacancies)
        loaded_vacancies = self.storage.load_vacancies()
        self.assertEqual(len(loaded_vacancies), 2)

if __name__ == '__main__':
    unittest.main()