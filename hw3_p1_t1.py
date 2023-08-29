# ООП Концепции:
# Создайте класс Person, который имеет атрибуты name, age и метод introduce(), 
# выводящий информацию о человеке. Создайте несколько объектов этого класса и вызовите метод introduce() для каждого из них.

class Person:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def introduce(self):

        pronoun = None

        match self.sex:
            case "m":
                pronoun = "ему"
            case "f":
                pronoun = "ей"

        print(f"Это {self.name}, {pronoun} {self.age} лет")

p1 = Person("Alice", 25, "f")
p2 = Person("Mike", 16, "m")

p1.introduce()
p2.introduce()