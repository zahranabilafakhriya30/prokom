class User:
    def __init__(self, first_name, last_name, umur, pekerjaan, kota):
        self.first_name = first_name
        self.last_name = last_name
        self.umur = umur
        self.pekerjaan = pekerjaan
        self.kota = kota

    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.umur}")
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Kota: {self.kota}")

    def greet_user(self):
        print(f"Halo, {self.first_name}! Selamat datang.")


user1 = User("Zahra", "Nabila", 18, "Mahasiswa", "Kediri")
user2 = User("Matin", "Azka", 20, "Mahasiswa", "Surabaya")
user3 = User("Nadia", "Putri", 19, "Pelajar", "Malang")

user1.describe_user()
user1.greet_user()

print()
user2.describe_user()
user2.greet_user()

print()
user3.describe_user()
user3.greet_user()