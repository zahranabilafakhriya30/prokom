class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, jumlah):
        self.number_served = jumlah

    def increment_number_served(self, jumlah):
        self.number_served += jumlah


restaurant = Restaurant("Sederhana", "Padang")

print("Jumlah pelanggan:", restaurant.number_served)

restaurant.number_served = 20
print("Jumlah pelanggan:", restaurant.number_served)

restaurant.set_number_served(50)
print("Jumlah pelanggan:", restaurant.number_served)

restaurant.increment_number_served(10)
print("Jumlah pelanggan:", restaurant.number_served)