import unittest

from data.vacancy import Vacancy


class TestVacancy(unittest.TestCase):

    def test_creation(self):
        vacancy = Vacancy(
            title="Python‑разработчик",
            link="https://example.com",  # ← исправлено
            salary_from=100000,
            salary_to=150000,
            currency="RUB",
            description="Опыт от 3 лет"
        )
        self.assertEqual(vacancy.title, "Python‑разработчик")
        self.assertEqual(vacancy.link, "https://example.com")

    def test_description_must_be_string(self):
        with self.assertRaises(ValueError):
            Vacancy(
                title="Test",
                link="https://valid.com",
                salary_from=None,
                salary_to=None,
                currency="",
                description=123  # не строка
            )

    def test_description_empty_to_default(self):
        vacancy = Vacancy(
            title="Test",
            link="https://valid.com",
            salary_from=None,
            salary_to=None,
            currency=None,
            description=""  # пустая строка
        )
        self.assertEqual(vacancy.description, "Описание отсутствует")

    def test_link_validation(self):
        # Некорректная ссылка
        with self.assertRaises(ValueError):
            Vacancy(
                title="Test",
                link="invalid-link",  # нет http/https
                salary_from=None,
                salary_to=None,
                currency="",
                description="Desc"
            )

        # Корректная ссылка
        vacancy = Vacancy(
            title="Test",
            link="http://valid.com",
            salary_from=None,
            salary_to=None,
            currency="",
            description="Desc"
        )
        self.assertEqual(vacancy.link, "http://valid.com")

if __name__ == '__main__':
    unittest.main()
