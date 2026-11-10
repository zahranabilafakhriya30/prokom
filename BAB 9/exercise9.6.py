class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Cokelat", "Vanila", "Stroberi", "Matcha"]

    def display_flavors(self):
        print("Daftar rasa es krim:")
        for flavor in self.flavors:
            print("-", flavor)


kedai = IceCreamStand("Es Krim Ceria", "Dessert")
kedai.display_flavors()