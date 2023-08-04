# Создание экземпляра класса для работы с API сайтов с вакансиями
import sys
from api import HeadHunterAPI, SuperJobAPI
from json_saver import JSONSaver
from vacancy import Vacancy

hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()

# Получение вакансий с разных платформ
# hh_vacancies = hh_api.get_vacancies("Python")
# superjob_vacancies = superjob_api.get_vacancies("Python")

# Создание экземпляра класса для работы с вакансиями
vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000",  "руб", "Требования: опыт работы от 3 лет...")

# Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
# json_saver.delete_vacancy(vacancy)

# # Функция для взаимодействия с пользователем

def user_interaction():
    # Выбор платформы и запись данных в файл
    platforms = input("Выберете платформу для поиска работы:\n1 - HeadHunter, 2 - SuperJob\n")
    if platforms == '1':
        hh_vacancies = hh_api.get_vacancies("Python")
        json_saver = JSONSaver()
        json_saver.add_vacancy(hh_vacancies)
        # json_saver.get_vacancies_by_salary("1-150 000 руб.")
    elif platforms == '2':
        superjob_vacancies = superjob_api.get_vacancies("Python")
        json_saver = JSONSaver()
        json_saver.add_vacancy(superjob_vacancies)
    else:
        print("Не выбрана платформа, попробуйте еще раз")
        sys.exit()

    currency =[]
    json_get = JSONSaver().get_vacancies()[0]
    # Сортирвка вакансий по зарплате
    search_query = input("Выберете валюту зарплаты:\n1 - рубли, 2 - USD, 3 - любая валюта\n")
    if search_query == '1':
        currency = ['rub', 'RUR', 'RUB']
    elif search_query == '2':
        currency = ['USD']
    elif search_query == '3':
        currency.append([i['currency'] for i in json_get])
    else:
        print("Не указана валюта, попробуйте еще раз")
        sys.exit()

    salary = int(input("Введите зарплату, которую хотите получать:\n"))

    # top_n = int(input("Введите количество вакансий для вывода в топ N:\n"))
    print(currency)
    for i in json_get:
        if i['currency'] in currency:
            print(i.JSONSaver.get_vacancies_by_salary('1-150 000'))


#     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#     filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)
#
#     if not filtered_vacancies:
#         print("Нет вакансий, соответствующих заданным критериям.")
#         return
#
#     sorted_vacancies = sort_vacancies(filtered_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)


user_interaction()

#
# if __name__ == "__main__":
#     user_interaction()





# print(Superjob().api_response())

# JSONSaver().save("pjjnkjnk.json")

