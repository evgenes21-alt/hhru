from typing import List

from data.vacancy import Vacancy


def get_top_vacancies(vacancies: List[Vacancy], count: int) -> List[Vacancy]:
    """
    Возвращает топ-N вакансий по зарплате.

    :param vacancies: Список вакансий
    :param count: Количество вакансий для выбора
    :return: Список лучших вакансий
    """
    return sorted(vacancies, reverse=True)[:count]


def filter_vacancies(vacancies: List[Vacancy], keywords: List[str]) -> List[Vacancy]:
    """
    Фильтрует вакансии по ключевым словам.

    :param vacancies: Список вакансий
    :param keywords: Список ключевых слов для фильтрации
    :return: Список отфильтрованных вакансий
    """
    return [
        vacancy for vacancy in vacancies
        if any(keyword.lower() in vacancy.description.lower() for keyword in keywords)
    ]


