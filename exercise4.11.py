pizza_saya = ["Keju", "Sosis", "Blackpepper"]

pizza_teman = pizza_saya[:]

pizza_saya.append("Jagung")
pizza_teman.append("Paprika")

print("Pizza saya:")
for rasa in pizza_saya:
    print(rasa)

print("\nPizza teman:")
for rasa in pizza_teman:
    print(rasa)