import json

# Базовый класс Animal
class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

    def eat(self):
        return f"{self.name} ест."


# Подкласс Bird
class Bird(Animal):
    def make_sound(self):
        return "Чирик!"


# Подкласс Mammal
class Mammal(Animal):
    def make_sound(self):
        return "Рррр!"


# Подкласс Reptile
class Reptile(Animal):
    def make_sound(self):
        return "Шшш!"


# Класс ZooKeeper
class ZooKeeper:
    def __init__(self, name: str):
        self.name = name

    def feed_animal(self, animal: Animal):
        return f"{self.name} кормит {animal.name}."


# Класс Veterinarian
class Veterinarian:
    def __init__(self, name: str):
        self.name = name

    def heal_animal(self, animal: Animal):
        return f"{self.name} лечит {animal.name}."


# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} говорит: {animal.make_sound()}")


# Класс Zoo
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def save_to_file(self, filename: str):
        data = {
            "animals": [
                {"type": type(animal).__name__, "name": animal.name, "age": animal.age}
                for animal in self.animals
            ],
            "staff": [{"type": type(staff_member).__name__, "name": staff_member.name} for staff_member in self.staff],
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename: str):
        with open(filename, 'r') as f:
            data = json.load(f)
            for animal_data in data["animals"]:
                if animal_data["type"] == "Bird":
                    animal = Bird(animal_data["name"], animal_data["age"])
                elif animal_data["type"] == "Mammal":
                    animal = Mammal(animal_data["name"], animal_data["age"])
                elif animal_data["type"] == "Reptile":
                    animal = Reptile(animal_data["name"], animal_data["age"])
                self.add_animal(animal)

            for staff_data in data["staff"]:
                if staff_data["type"] == "ZooKeeper":
                    staff_member = ZooKeeper(staff_data["name"])
                elif staff_data["type"] == "Veterinarian":
                    staff_member = Veterinarian(staff_data["name"])
                self.add_staff(staff_member)


# Пример использования программы
if __name__ == "__main__":
    zoo = Zoo()

    # Добавление животных
    parrot = Bird("Попугай", 2)
    lion = Mammal("Лев", 5)
    snake = Reptile("Змея", 3)
    zoo.add_animal(parrot)
    zoo.add_animal(lion)
    zoo.add_animal(snake)

    # Добавление сотрудников
    keeper = ZooKeeper("Алексей")
    vet = Veterinarian("Мария")
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # Демонстрация полиморфизма
    animal_sound(zoo.animals)

    # Кормление животных и лечение
    print(keeper.feed_animal(parrot))
    print(vet.heal_animal(lion))

    # Сохранение состояния зоопарка в файл
    zoo.save_to_file("zoo_data.json")

    # Загрузка состояния зоопарка из файла
    another_zoo = Zoo()
    another_zoo.load_from_file("zoo_data.json")