import self
from DB import DBManager
from api import get_info

#создание БД
try:
    get_info()
except:
    pass

#Получение информации из базы
DBManager.get_companies_and_vacancies_count(self)
DBManager.get_all_vacancies(self)
DBManager.get_avg_salary(self)
DBManager.get_vacancies_with_higher_salary(self)
DBManager.get_vacancies_with_keyword(self, "1С")



