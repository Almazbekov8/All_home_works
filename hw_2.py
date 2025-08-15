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


friend = Friend(name="Азирет", birth_date="5.12.2000", occupation="Программист", higher_education=True)
friend.introduce()

classmate = Classmate(name="Адилет", birth_date="5.12.2000", occupation="Программист", higher_education=True)
classmate.introduce()