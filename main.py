from typing import List
from pprint import pprint
from src.head_hunter import HeadHunterAPI
from data.file_storage import FileStorage
from data.vacancy import Vacancy
from utils.helpers import get_top_vacancies, filter_vacancies

def run_user_interface():
    hh_api = HeadHunterAPI()
    storage = FileStorage()

    while True:
        action = input("\nВыберите действие:\n"
                      "1. Загрузить вакансии\n"
                      "2. Показать ТОП-вакансии\n"
                      "3. Найти вакансии по ключевым словам\n"
                      "4. Завершить работу\n")

        if action == '1':
            keyword = input("Введите ключевой запрос: ")
            raw_data = hh_api.fetch_data(keyword)
            vacancies = [Vacancy(item['name'], item['alternate_url'], item.get('salary'), item['snippet']['responsibility']) for item in raw_data]
            storage.save_vacancies(vacancies)
            print("Вакансии успешно загружены и сохранены.")

        elif action == '2':
            n = int(input("Введите количество вакансий для вывода: "))
            vacancies = storage.load_vacancies()
            top_vacancies = get_top_vacancies(vacancies, n)
            pprint([v.__dict__ for v in top_vacancies])

        elif action == '3':
            keywords = input("Введите ключевые слова через пробел: ").split()
            vacancies = storage.load_vacancies()
            filtered_vacancies = filter_vacancies(vacancies, keywords)
            pprint([v.__dict__ for v in filtered_vacancies])

        elif action == '4':
            print("Завершение работы.")
            break

        else:
            print("Некорректный выбор. Выберите пункт меню снова.")

if __name__ == "__main__":
    run_user_interface()