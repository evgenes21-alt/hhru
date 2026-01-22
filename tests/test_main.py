import sys
import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import MagicMock, patch

from main import run_user_interface


class TestMainInterface(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'python', '4'])
    @patch('src.head_hunter.HeadHunterAPI.fetch_data')
    @patch('data.file_handlers.JSONFileHandler.save_data')
    def test_full_workflow(self, mock_input, mock_fetch, mock_save):
        # Мокируем ответ API
        mock_fetch.return_value = [
            {
                "title": "Python‑разработчик",
                "link": "https://hh.ru/vacancy/1",
                "salary": {"from": 100000, "to": 150000, "currency": "RUB"},
                "description": "Опыт от 3 лет"
            }
        ]

        # Захватываем вывод с помощью StringIO
        with StringIO() as captured_output:
            # Перенаправляем stdout в captured_output
            with redirect_stdout(captured_output):
                run_user_interface()

            # Получаем текст после выполнения
            output = captured_output.getvalue()

        # Проверки
        self.assertIn("Вакансии успешно загружены", output)
        self.assertIn("Работа завершена.", output)

    @patch('builtins.input', side_effect=['999', '4'])  # неверный выбор
    def test_invalid_choice(self, mock_input):
        with StringIO() as captured_output:
            with redirect_stdout(captured_output):
                run_user_interface()
            output = captured_output.getvalue()

        self.assertIn("Неверный выбор", output)

    @patch('builtins.input', side_effect=['4'])
    def test_quit_application(self, mock_input):
        with StringIO() as captured_output:
            with redirect_stdout(captured_output):
                run_user_interface()
            output = captured_output.getvalue()

        self.assertIn("Работа завершена.", output)



if __name__ == '__main__':
    unittest.main()
