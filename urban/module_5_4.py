class House:
    # Атрибут класса для хранения истории зданий
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # Добавляем название строения в историю
        name = args[0]  # Название передаётся первым аргументом
        cls.houses_history.append(name)
        # Создаем новый экземпляр класса
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __del__(self):
        # Выводим сообщение при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")


# Создаём объекты класса House и проверяем историю
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)