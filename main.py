

from pprint import pprint
from typing import List

from data.file_handlers import JSONFileHandler
from data.vacancy import Vacancy
from src.head_hunter import HeadHunterAPI
from utils.filters import filter_vacancies, get_top_vacancies


def run_user_interface():
    hh_api = HeadHunterAPI()
    handler = JSONFileHandler('vacancies.json')

    while True:
        action = input("\nВыберите действие:\n"
                      "1. Загрузить вакансии\n"
                      "2. Показать TOP-вакансии\n"
                      "3. Найти вакансии по ключевым словам\n"
                      "4. Завершить работу\n")

        if action == '1':
            # Загрузка вакансий из API
            keyword = input("Введите ключевой запрос: ")
            try:
                raw_data = hh_api.fetch_data(keyword)
            except Exception as e:
                print(f"Ошибка при запросе к API: {e}")
                continue

            vacancies = []
            for item in raw_data:
                # 1. Обработка поля description
                desc = item.get('description', None)
                if desc is None:
                    desc = ""
                description = str(desc).strip()
                if not description:
                    description = "Описание отсутствует"

                # 2. Обработка зарплаты
                salary_data = item.get('salary', {})
                salary_from = salary_data.get('from')
                salary_to = salary_data.get('to')
                currency = salary_data.get('currency', '')

                # 3. Проверка обязательных полей
                if not item.get('title') or not item.get('link'):
                    print("Пропущена вакансия: нет названия или ссылки")
                    continue

                # 4. Создание объекта Vacancy
                try:
                    vacancy = Vacancy(
                        title=item['title'],
                        link=item['link'],
                        salary_from=salary_from,
                        salary_to=salary_to,
                        currency=currency,
                        description=description
                    )
                    vacancies.append(vacancy)
                except Exception as e:
                    print(f"Ошибка при создании вакансии: {e}")
                    continue

            # 5. Сохранение в файл
            try:
                handler.save_data([v.__dict__ for v in vacancies])
                print(f"Вакансии успешно загружены и сохранены ({len(vacancies)} шт.).")
            except Exception as e:
                print(f"Ошибка при сохранении в файл: {e}")

        elif action == '2':
            # Показать TOP-вакансии по зарплате
            try:
                count = int(input("Введите количество вакансий для вывода: "))
                if count <= 0:
                    print("Число должно быть положительным.")
                    continue
            except ValueError:
                print("Введите число.")
                continue

            try:
                vacancies_data = handler.load_data()
                vacancies = []
                for v in vacancies_data:
                    # Гарантируем, что description — строка
                    desc = v.get('description', '')
                    if desc is None:
                        desc = ""
                    description = str(desc).strip()
                    if not description:
                        description = "Описание отсутствует"

                    try:
                        vacancy = Vacancy(
                            title=v['title'],
                            link=v['link'],
                            salary_from=v.get('salary_from'),
                            salary_to=v.get('salary_to'),
                            currency=v.get('currency', ''),
                            description=description
                        )
                        vacancies.append(vacancy)
                    except Exception as e:
                        print(f"Ошибка при восстановлении вакансии: {e}")
                        continue

                top_vacancies = get_top_vacancies(vacancies, count)
                if top_vacancies:
                    pprint([v.__dict__ for v in top_vacancies])
                else:
                    print("Вакансий для отображения нет.")
            except Exception as e:
                print(f"Ошибка при загрузке данных: {e}")

        elif action == '3':
            # Поиск вакансий по ключевым словам в описании
            keywords_input = input("Введите ключевые слова через запятую: ")
            keywords = [k.strip().lower() for k in keywords_input.split(',') if k.strip()]
            if not keywords:
                print("Введите хотя бы одно ключевое слово.")
                continue

            try:
                vacancies_data = handler.load_data()
                vacancies = []
                for v in vacancies_data:
                    desc = v.get('description', '')
                    if desc is None:
                        desc = ""
                    description = str(desc).strip()

                    try:
                        vacancy = Vacancy(
                            title=v['title'],
                            link=v['link'],
                            salary_from=v.get('salary_from'),
                            salary_to=v.get('salary_to'),
                            currency=v.get('currency', ''),
                            description=description
                        )
                        vacancies.append(vacancy)
                    except Exception as e:
                        print(f"Ошибка при восстановлении вакансии: {e}")
                        continue

                filtered = filter_vacancies(vacancies, keywords)
                if filtered:
                    pprint([v.__dict__ for v in filtered])
                else:
                    print("Вакансий, соответствующих критериям, не найдено.")
            except Exception as e:
                print(f"Ошибка при поиске: {e}")

        elif action == '4':
            print("Работа завершена.")
            break

        else:
            print("Неверный выбор. Попробуйте ещё раз.")



if __name__ == '__main__':
    run_user_interface()