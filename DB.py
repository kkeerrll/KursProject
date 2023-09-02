import psycopg2
def connect_sql(self, query):
    # Подключение к базе данных
    conn = psycopg2.connect(
        dbname="kurs",
        user="postgres",
        password="lika2244",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(query)

    # Получение результатов запроса
    return cursor.fetchall()

    # Закрытие соединения
    cursor.close()
    conn.close()


class DBManager():
    def __init__(self):
        pass

    def get_companies_and_vacancies_count(self):
        # print("получает список всех компаний и количество вакансий у каждой компании")
        query = "SELECT name, open_vacancies FROM employers"
        for row in connect_sql(self, query):
            print(f'Компания: {row[0]}, Количество вакансий: {row[1]}')

    def get_all_vacancies(self):
        # print("получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию")
        query = "SELECT * FROM public.vacancy"
        for row in connect_sql(self, query):
            print(f'Название компании: {row[0]}, Название вакансии: {row[1]}, Зарплата: {row[2]} руб, Ссылка: {row[5]}')

    def get_avg_salary(self):
        # print("получает среднюю зарплату по вакансиям")
        query = "SELECT salary_from, salary_to FROM public.vacancy"

        count_try = 0
        c_try = 0
        c_false = 0
        count_false = 0

        for item in connect_sql(self, query):
            if item is not None:
                split_values = [i for value in item if value is not None for i in value.split(',')]
                if split_values != ['']:
                    min_value = int(''.join([letter for letter in split_values[0] if letter.isdigit()]) or 0)
                    max_value = int(''.join([letter for letter in split_values[-1] if letter.isdigit()]) or min_value)
                    if min_value == 0:
                        # print(int(max_value))
                        count_try = int(max_value) + count_try
                        c_try = c_try + 1
                    else:
                        # print(int((min_value + max_value) / 2))
                        count_false = int(max_value) + count_false
                        c_false = c_false + 1

                else:
                    raise ValueError("Invalid salary format")

        result = int((count_try + count_false) / (c_try + c_false))
        print(f'Средняя зарплата {result} руб')
        return result


    def get_vacancies_with_higher_salary(self):
        # print("получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.")
        result = DBManager().get_avg_salary()

        query = "SELECT name, salary_to FROM public.vacancy"
        # result = self.get_avg_salary()
        for item in connect_sql(self, query):
            if int(item[1] or 0) > result:
                print(f'Вакансия, у которой зарплата выше средней: {item[0]}')


    def get_vacancies_with_keyword(self, keyword):
        # print("получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python")

        query = "SELECT name FROM public.vacancy"
        matching_vacancies = []
        for vacancy in connect_sql(self, query):
            if keyword in vacancy[0]:
                matching_vacancies.append(vacancy[0])
        result_string = ", ".join(str(element) for element in matching_vacancies)
        print(f'Cписок всех вакансий, в названии которых содержатся переданные в метод слова: {result_string}')





