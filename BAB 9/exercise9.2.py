class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restoran: {self.restaurant_name}")
        print(f"Jenis makanan: {self.cuisine_type}")


restoran1 = Restaurant("Sederhana", "Padang")
restoran2 = Restaurant("KFC", "Ayam Goreng")
restoran3 = Restaurant("HokBen", "Jepang")

restoran1.describe_restaurant()
print()

restoran2.describe_restaurant()
print()

restoran3.describe_restaurant()