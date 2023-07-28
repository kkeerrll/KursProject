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
