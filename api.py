import psycopg2
import requests

def get_info():
    # Получение данных из API
    url_employers = f'https://api.hh.ru/employers/?text=IT'
    response_employers = requests.get(url_employers)
    employers_data = response_employers.json()

    # Подготовка данных для записи
    data_to_insert_employers = []  # Список для хранения данных для записи
    data_to_insert_vacancy = []  # Список для хранения данных для записи

    # for item in api_data:
    for item in employers_data['items']:
        # Преобразование данных из API в формат для записи в базу данных
        processed_data = {
            'id': item['id'],
            'Название компании:': item['name'],
            'Открытые вакансии:': item['open_vacancies'],
        }
        data_to_insert_employers.append(processed_data)

    # Подключение к базе данных
    conn = psycopg2.connect(
        dbname="kurs",
        user="postgres",
        password="lika2244",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    # Определение SQL-запроса для создания таблицы
    create_table_employers = """
        CREATE TABLE employers (
            id VARCHAR(50) NOT NULL,
            name VARCHAR(50) NOT NULL,
            open_vacancies VARCHAR(50) NOT NULL
        );
    """

    # Выполнение SQL-запроса
    cursor.execute(create_table_employers)

    create_table_vacancy = """
        CREATE TABLE  vacancy (
            name_company VARCHAR(100) NOT NULL,
            name VARCHAR(100) NOT NULL,
            salary_from VARCHAR(50),
            salary_to VARCHAR(50),
            currency VARCHAR(50),
            url VARCHAR(100)
        );
    """
    cursor.execute(create_table_vacancy)

    # Запись данных в базу данных
    for item in data_to_insert_employers:
        cursor.execute("INSERT INTO employers (id, name, open_vacancies) "
                    "VALUES (%s, %s, %s)",
                    (item['id'], item['Название компании:'], item['Открытые вакансии:']))


        # url_vacancies = f"https://api.hh.ru/vacancies?employer_id={item['id']}"
        url_vacancies = f"https://api.hh.ru/vacancies?employer_id={item['id']}"
        response_vacancies = requests.get(url_vacancies)
        vacancy_data = response_vacancies.json()

        if response_vacancies.status_code == 200:

            # for item in api_data:
            for vacancy in vacancy_data['items']:
                # Преобразование данных из API в формат для записи в базу данных
                if vacancy['salary'] != None and vacancy['salary']['currency'] == 'RUR':
                    processed_data = {
                        'Название компании': item['Название компании:'],
                        'Название вакансии:': vacancy['name'],
                        'Минимальная ЗП:': vacancy['salary']['from'],
                        'Максимальная ЗП:': vacancy['salary']['to'],
                        'Валюта:': vacancy['salary']['currency'],
                        'Ссылка:': vacancy['alternate_url']
                    }
                    data_to_insert_vacancy.append(processed_data)

                    cursor.execute("INSERT INTO vacancy (name_company, name, salary_from, salary_to, currency, url) "
                                   "VALUES (%s, %s, %s, %s, %s, %s)",
                                   (item['Название компании:'], vacancy['name'], vacancy['salary']['from'], vacancy['salary']['to'],
                                    vacancy['salary']['currency'], vacancy['alternate_url']
                                    ))
        else:
            print('Ошибка при получении данных о вакансиях:', response_vacancies.status_code)


    # Подтверждение изменений и закрытие соединения
    conn.commit()
    cursor.close()
    conn.close()


