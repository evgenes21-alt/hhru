import unittest

from src.base_api import BaseAPI


class TestBaseAPI(unittest.TestCase):
    def test_base_api_creation(self):
        # Проверим, что нельзя создать экземпляр абстрактного класса
        with self.assertRaises(TypeError):
            BaseAPI('https://example.com')

    def test_subclassing(self):
        # Создадим фиктивный класс-наследник
        class MyAPI(BaseAPI):
            def fetch_data(self, keyword):
                pass
        # Проверим, что теперь класс можно создать
        MyAPI('https://example.com')

if __name__ == '__main__':
    unittest.main()