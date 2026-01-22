import unittest
from unittest.mock import MagicMock, patch

from src.head_hunter import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_data_success(self, mock_get):
        # Мокируем успешный ответ API
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json = MagicMock(return_value={
            "items": [
                {
                    "id": "1",
                    "title": "Python‑разработчик",
                    "link": "https://hh.ru/vacancy/1",
                    "salary": {"from": 100000, "to": 150000, "currency": "RUB"},
                    "description": "Требуется опыт"
                }
            ]
        })
        mock_get.return_value = mock_response

        api = HeadHunterAPI()
        data = api.fetch_data("python")

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], "Python‑разработчик")


    @patch('requests.get')
    def test_fetch_data_no_items(self, mock_get):
        # Ответ API без вакансий
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json = MagicMock(return_value={"items": []})
        mock_get.return_value = mock_response


        api = HeadHunterAPI()
        data = api.fetch_data("python")
        self.assertEqual(data, [])


    @patch('requests.get')
    def test_fetch_data_http_error(self, mock_get):
        # Ошибка HTTP
        mock_get.side_effect = Exception("Connection error")

        api = HeadHunterAPI()
        with self.assertRaises(Exception):
            api.fetch_data("python")

if __name__ == '__main__':
    unittest.main()
