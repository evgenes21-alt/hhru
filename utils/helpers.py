from typing import List
from data.vacancy import Vacancy

def get_top_vacancies(vacancies: List[Vacancy], n: int) -> List[Vacancy]:
    return sorted(vacancies, reverse=True)[:n]


def filter_vacancies(vacancies: List[Vacancy], keywords: List[str]) -> List[Vacancy]:
    return [
        v for v in vacancies
        if any(keyword.lower() in (v.description.lower() if v.description else "") for keyword in keywords)
    ]

