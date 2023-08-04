class Vacancy():
    def __init__(self, name, url, salary, currency, requirement):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        try:
            self.salary = self.validate_salary(salary)
            self.name = name
            self.url = url
            self.currency = currency
            self.requirement = requirement
        except:
            pass

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

    def validate_salary(self, salary_range: str):
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