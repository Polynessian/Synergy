
class Transport:
    def __init__(self, name, max_speed, mileage) -> None:
        self.name = name
        self.max_speed = str(max_speed)
        self.mileage = str(mileage)
        
class Autobus(Transport):
    def __init__(self, name='Renault Logan', max_speed=180, mileage=12) -> None:
        super().__init__(name, max_speed, mileage)
        
    def show(self):
        return f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}"
        

print(Autobus().show())



