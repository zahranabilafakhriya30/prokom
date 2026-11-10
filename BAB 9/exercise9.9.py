class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

    def get_range(self):
        if self.battery_size == 75:
            jarak = 260
        elif self.battery_size == 65:
            jarak = 225
        else:
            jarak = 0

        print(f"Jarak tempuh mobil: {jarak} km")


class ElectricCar:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.battery = Battery()


mobil = ElectricCar("Tesla", "Model S")

mobil.battery.get_range()

mobil.battery.upgrade_battery()

mobil.battery.get_range()