# import json
# import requests
# from abc import ABC, abstractmethod
# import os
#
# #  pip3 install google-api-python-client
# from googleapiclient.discovery import build
# #
# # # import isodate
# #
# # # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
# # api_key: str = "AIzaSyDzK-EuKi2DdmdlIl9Pl0Xs1HKEVoOk2HI"
# #
# # # создать специальный объект для работы с API
# # youtube = build('youtube', 'v3', developerKey=api_key)
# #
# #
# # # https://api.hh.ru/vacancies/{vacancy_id}
#
#
# import requests
#
# url = 'https://api.superjob.ru/2.0/vacancies'
# api_key = 'ваш_ключ_приложения'
# params = {
#     'keyword': 'Python'
# }
#
# vacancies = []
#
# while True:
#     headers = {'X-Api-App-Id': api_key}
#     response = requests.get(url, params=params, headers=headers)
#
#     if response.status_code == 200:
#         data = response.json()
#         vacancies.extend(data['objects'])
#         if data['more']:
#             params['page'] += 1
#         else:
#             break
#     else:
#         print('Ошибка при выполнении запроса')
#         break
#
# # Обработка результатов
# for vacancy in vacancies:
#     print(vacancy['title'])
