class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

class Friend(Person):
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я друг Игоря, "
              f"я родился {self.birth_date}, работаю {self.occupation.lower()}.")



class Classmate(Person):
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одноклассник Игоря, "
              f"я родился {self.birth_date}, работаю {self.occupation.lower()}.")

