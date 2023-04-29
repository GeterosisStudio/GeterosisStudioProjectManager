import sys, Qlib, os

PATH = os.path.abspath

if not PATH in sys.path:
    sys.path.append(PATH)


class Person:
    def print_age(self, current_year):
        print(current_year - self.data_r)
    def name(self):
        return(f"Name: {self}")
    def data_r(self, year):
        print(f"{year - self}")
    def qq(self):
        print(f"sas: {self}")


p1 = Qlib.Person("Sasi", 1996, 123)
year = 2022
print(Qlib.Person.print_testww)