class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # Название дома
        self.number_of_floors = number_of_floors  # Количество этажей

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:  # Проверка на существование этажа
            for floor in range(1, new_floor + 1):
                print(floor)  # Вывод значений от 1 до new_floor (включительно)
        else:
            print("Такого этажа не существует")  # Вывод сообщения, если этаж не существует


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
