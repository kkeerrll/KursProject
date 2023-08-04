# Создание экземпляра класса для работы с API сайтов с вакансиями
import sys
from api import HeadHunterAPI, SuperJobAPI
from json_saver import JSONSaver
import json
import os

# Функция для взаимодействия с пользователем
json_saver = JSONSaver()
def user_interaction():
    #Подготовка к началу работы
    json_saver.delete_file()
    if os.path.exists("total.txt"):
        os.remove("total.txt")

    # Выбор платформы и запись данных в файл
    platforms = input("Выберете платформу для поиска работы:\n1 - HeadHunter, 2 - SuperJob\n")
    if platforms == '1':
        hh_api = HeadHunterAPI()
        hh_vacancies = hh_api.get_vacancies("Python")
        json_saver.add_vacancy(hh_vacancies)
        # json_saver.get_vacancies_by_salary("1-150 000 руб.")
    elif platforms == '2':
        superjob_api = SuperJobAPI()
        superjob_vacancies = superjob_api.get_vacancies("Python")
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
        list = []
        list.append([i['currency'] for i in json_get])
        currency = [item for sublist in list for item in sublist]
    else:
        print("Не указана валюта, попробуйте еще раз")
        sys.exit()

    salary = int(input("Введите зарплату, которую хотите получать:\n"))


    # for i in json_get:
    #     if i['currency'] in currency and i['salary'] >= salary:
    #         data = json.dumps(
    #             i,
    #             default=lambda o: o.__dict__,
    #             sort_keys=True,
    #             indent=4,
    #             ensure_ascii=False
    #         )
    #         with open("total.txt", "a", encoding="utf-8") as file:
    #             file.append(data)
    for i in json_get:
        if i['currency'] in currency and i['salary'] >= salary:
            data = json.dumps(
                i,
                default=lambda o: o.__dict__,
                sort_keys=True,
                indent=4,
                ensure_ascii=False
            )
            with open("total.txt", "a", encoding="utf-8") as file:
                file.write(data)
            print(i['name'])

    with open("total.txt", "a", encoding="utf-8") as file:
        with open("total.txt", 'r', encoding='utf-8') as file:
            contents = file.read()
            if contents == "":
                print("Нет вакансий, соответствующих заданным критериям.")




if __name__ == "__main__":
    user_interaction()



