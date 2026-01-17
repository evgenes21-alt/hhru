import unittest
from unittest.mock import patch
from src.head_hunter import HeadHunterAPI

class TestHeadHunterAPI(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_data(self, mock_get):
        # Эмулируем ответ от API
        mock_response = {'items': []}
        mock_get.return_value.json.return_value = mock_response
        hh_api = HeadHunterAPI()
        result = hh_api.fetch_data('developer')
        self.assertEqual(result, [])

    @patch('requests.get')
    def test_connect_exception(self, mock_get):
        # Эмулируем неудачную попытку соединения
        mock_get.side_effect = Exception('Network Error')
        hh_api = HeadHunterAPI()
        with self.assertRaises(Exception):
            hh_api.fetch_data('developer')

if __name__ == '__main__':
    unittest.main()