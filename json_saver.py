import json
from abc import ABC, abstractmethod
from api import HeadHunterAPI, SuperJobAPI, Api
from vacancy import Vacancy

class Abstract_action(ABC):
    def add_vacancy(self, vacancy: Vacancy):
        pass

    def get_vacancies_by_salary(self, salary_range: str):
        pass

    def delete_vacancy(self, vacancy: Vacancy):
        pass


class JSONSaver(Abstract_action):
    """Класс работает с данными файла"""
    file_name: str = 'vacancies.json'

    @staticmethod
    def get_vacancies():
        with open(JSONSaver.file_name, 'r', encoding='utf-8') as file:
            contents = file.read()
            if contents == "":
                return []
            else:
                return json.loads(contents)

    def save(self, vacancies):
        data = json.dumps(
            vacancies,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4,
            ensure_ascii=False
        )

        with open(JSONSaver.file_name, 'w', encoding='utf-8') as file:
            file.write(data)



    def add_vacancy(self, vacancy: Vacancy):
        vacancies = self.get_vacancies()
        vacancies.append(vacancy)
        self.save(vacancies)

    def get_vacancies_by_salary(self, salary_range: str):
        vacancies = self.get_vacancies()
        salaries = salary_range.split('-')

        if salaries != ['']:
            min_value = int(''.join([letter for letter in salaries[0] if letter.isdigit()]) or 0)
            max_value = int(''.join([letter for letter in salaries[-1] if letter.isdigit()]) or min_value)
            if min_value == 0:
                return int(max_value)
            else:
                return int((min_value + max_value) / 2)
        else:
            raise ValueError("Invalid salary format")

    def delete_vacancy(self, vacancy: Vacancy):
        vacancies = [v for v in self.get_vacancies() ]
        # if v['url'] != vacancy.url]
        # vacancies = [v for v in self.get_vacancies() if v.get('url') != vacancy.url]
        self.save(vacancies)
