from datetime import datetime as dt, date
from dateutil.relativedelta import relativedelta


class MyAge:
    def __init__(self, date_of_birth, my_name):
        # __init__ function to fill properties and use self
        # your birth date input yyyy-mm-dd
        self.__date_of_birth = dt.strptime(date_of_birth, '%Y-%m-%d')
        self.__my_name = my_name
        self.__my_age_years = relativedelta(
            date.today(), self.__date_of_birth).years

    # create print function
    def show_me_my_age(self):
        return f"{self.__my_name}, you are so young, only {self.__my_age_years} years old!"


# instantiate the class and execute the print function
age = MyAge("1982-08-04", "Mr James")
print(age.show_me_my_age())
# > 'Mr James, you are so young, only 39 years old!'