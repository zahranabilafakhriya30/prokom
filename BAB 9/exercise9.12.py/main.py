from admin import Admin

admin = Admin("Zahra", "Nabila")

print("Hak akses administrator:")
admin.privileges.show_privileges()