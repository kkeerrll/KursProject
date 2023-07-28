import json
import requests
from abc import ABC, abstractmethod
from vacancy import Vacancy

class Api(ABC):
    @abstractmethod
    def get_vacancies(self, search):
        pass


class HeadHunterAPI(Api):
    """Класс для hh"""

    def get_vacancies(self, search):
        api_response = requests.get(f'https://api.hh.ru/vacancies?text={search}')
        data = api_response.text
        parsed_json = json.loads(data)
        print(parsed_json)
        print()
        return [Vacancy(item['name'],
                        item['alternate_url'],
                        item['salary']['to'],
                        item['snippet']['requirement']) for item in parsed_json['items'] if item['salary'] != None]


class SuperJobAPI(Api):
    """Класс для superjob"""

    def get_vacancies(self, search):
        url = 'https://api.superjob.ru/2.0/vacancies/'
        api_key = 'v3.r.137692338.bc02cb4c593534e45098114689e8c19f977b0b8d.a951a3ddf5665533a40af06a68e7cdcdc37a3ce3'
        headers = {'X-Api-App-Id': api_key}
        api_response = requests.get(url, headers=headers)
        data = api_response.text
        parsed_json = json.loads(data)

        return [Vacancy(item['profession'], item['link'], f"{item['payment_to']}-{item['payment_from']}", item['candidat'])
                for item in parsed_json['objects']]
