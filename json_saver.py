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
        """
        Метод `save()` сохраняет в файл значения
        """

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
            min_value = int(''.join([letter for letter in salaries[0] if letter.isdigit()]))
            max_value = int(''.join([letter for letter in salaries[-1] if letter.isdigit()]))

            return [vacancy for vacancy in vacancies if vacancy['salary'] in range(min_value, max_value)]
        else:
            raise ValueError("Invalid salary format")

    def delete_vacancy(self, vacancy: Vacancy):
        vacancies = [v for v in self.get_vacancies() if v['url'] != vacancy.url]
        self.save(vacancies)
