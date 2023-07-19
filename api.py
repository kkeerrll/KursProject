import json
import requests
from abc import ABC, abstractmethod
import os

#  pip3 install google-api-python-client
from googleapiclient.discovery import build

# import isodate

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = "AIzaSyDzK-EuKi2DdmdlIl9Pl0Xs1HKEVoOk2HI"

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


# https://api.hh.ru/vacancies/{vacancy_id}

class Api(ABC):
    @staticmethod
    @abstractmethod
    def api_response():
        pass


class Hh(Api):
    """Класс для hh"""

    @staticmethod
    def api_response():
        api_response = requests.get('https://api.hh.ru/vacancies')
        data = api_response.text
        parsed_json = json.loads(data)
        return [Vacancy(item['id'], item['name'], item['snippet']['responsibility'], item['alternate_url'],
                        item['salary']['to'], item['snippet']['requirement']) for item in parsed_json['items']]


class Superjob(Api):
    """Класс для superjob"""

    def api_response(self):
        api_response = requests.get('https://api.hh.ru/vacancies')
        print(api_response.status_code)
        data = api_response.text
        parsed_json = json.loads(data)
        print("Todos:", parsed_json)
        print(parsed_json['items'][0]['id'])
        return [Vacancy(item['id'], item['name'], item['snippet']['responsibility'], item['alternate_url'], item['salary']['to'], item['snippet']['requirement']) for item in parsed_json['items']]



class Vacancy():

    def __init__(self, vacancy_id, name, responsibility, url, salary, requirement):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.vacancy_id = vacancy_id
        self.name = name
        self.responsibility = responsibility
        self.url = url
        self.salary = salary
        self.requirement = requirement

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def validate_salary(self, salary):
        if isinstance(salary, (int, float)):
            return salary
        else:
            raise ValueError("Invalid salary format")


class Abstract_action(ABC):
    @abstractmethod
    def to_json(self, file_name: str):
        pass

    def print_json(self):
        pass

    def delete_json(self):
        pass

class Action(Abstract_action):
    def to_json(self, file_name: str):
        """
        Метод `to_json()` сохраняет в файл значения
        """

        data = json.dumps(Hh.api_response() + Hh.api_response(), default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(data)











