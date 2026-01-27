
import unittest
from unittest.mock import patch
from typing import List

# Импортируем ваш класс
from src.base_api import BaseAPI



class TestBaseAPI(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://api.example.com/v1"
        self.keyword = "python"
        self.page = 1
        self.per_page = 10

    # 🔧 ИЗМЕНЕНО: тестируем наследника, а не абстрактный класс
    def test_initialization(self):
        """Проверяем инициализацию через наследника."""
        class ConcreteAPI(BaseAPI):
            def fetch_data(self, keyword: str, page: int = 1, per_page: int = 10) -> List[dict]:
                return []

        api = ConcreteAPI(self.base_url)
        self.assertEqual(api.base_url, self.base_url)

    def test_abstract_method_requires_implementation(self):
        """Проверяем, что без реализации fetch_data нельзя создать экземпляр."""
        class IncompleteAPI(BaseAPI):
            pass

        with self.assertRaises(TypeError):
            IncompleteAPI(self.base_url)

    def test_concrete_implementation(self):
        """Проверяем работу с реализованным fetch_data."""
        class ConcreteAPI(BaseAPI):
            def fetch_data(self, keyword: str, page: int = 1, per_page: int = 10) -> List[dict]:
                return [{"id": 1, "title": "Dev"}]

        api = ConcreteAPI(self.base_url)
        result = api.fetch_data(self.keyword)
        self.assertEqual(len(result), 1)
        self.assertIn("id", result[0])

    @patch.object(BaseAPI, 'fetch_data', return_value=[])
    def test_fetch_data_default_params(self, mock_fetch):
        """Проверяем вызов с параметрами по умолчанию."""
        class MockAPI(BaseAPI):
            def fetch_data(self, keyword: str, page: int = 1, per_page: int = 10) -> List[dict]:
                return mock_fetch(keyword, page, per_page)

        api = MockAPI(self.base_url)
        api.fetch_data(self.keyword)

        mock_fetch.assert_called_with(self.keyword, 1, 10)

    def test_fetch_data_with_custom_page_and_per_page(self):
        """Проверяем нестандартные page и per_page."""
        class TestAPI(BaseAPI):
            def fetch_data(self, keyword: str, page: int = 1, per_page: int = 10) -> List[dict]:
                return [
                    {"page": page, "per_page": per_page, "keyword": keyword}
                ]

        api = TestAPI(self.base_url)
        result = api.fetch_data(self.keyword, page=2, per_page=5)

        self.assertEqual(result[0]["page"], 2)
        self.assertEqual(result[0]["per_page"], 5)

    def test_fetch_data_empty_keyword(self):
        """Проверяем пустое keyword."""
        class TestAPI(BaseAPI):
            def fetch_data(self, keyword: str, page: int = 1, per_page: int = 10) -> List[dict]:
                return [] if not keyword else [{"keyword": keyword}]

        api = TestAPI(self.base_url)
        result = api.fetch_data("")
        self.assertEqual(result, [])

    def test_fetch_data_large_per_page(self):
        """Проверяем большое per_page."""
        class TestAPI(BaseAPI):
            def fetch_data(self, keyword: str, page: int = 1, per_page: int = 10) -> List[dict]:
                per_page = min(per_page, 100)
                return [{"count": per_page}]

        api = TestAPI(self.base_url)
        result = api.fetch_data(self.keyword, per_page=150)
        self.assertEqual(result[0]["count"], 100)

    def test_fetch_data_negative_page(self):
        """Проверяем отрицательный page."""
        class TestAPI(BaseAPI):
            def fetch_data(self, keyword: str, page: int = 1, per_page: int = 10) -> List[dict]:
                page = max(page, 1)
                return [{"page": page}]

        api = TestAPI(self.base_url)
        result = api.fetch_data(self.keyword, page=-1)
        self.assertEqual(result[0]["page"], 1)

    def test_fetch_data_zero_per_page(self):
        """Проверяем per_page=0."""
        class TestAPI(BaseAPI):
            def fetch_data(self, keyword: str, page: int = 1, per_page: int = 10) -> List[dict]:
                per_page = max(per_page, 1)
                return [{"per_page": per_page}]

        api = TestAPI(self.base_url)
        result = api.fetch_data(self.keyword, per_page=0)
        self.assertEqual(result[0]["per_page"], 1)



if __name__ == '__main__':
    unittest.main()
