import os
import json
from typing import List
from pathlib import Path
from data.vacancy import Vacancy

class FileStorage:
    def __init__(self, filename: str = 'vacancies.json'):
        self._filename = filename

    def save_vacancies(self, vacancies: List[Vacancy]):
        data = [vars(vacancy) for vacancy in vacancies]
        with open(self._filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_vacancies(self) -> List[Vacancy]:
        if not os.path.exists(self._filename):
            return []
        with open(self._filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return [Vacancy(**item) for item in data]