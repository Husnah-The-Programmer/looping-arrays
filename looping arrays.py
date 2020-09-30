cars = ["Ford Escape", "BMW", "Toyota", "Lexus", "BMW"]

for x in cars:
    print(x)

print("\n")

cars.append("jeep")
for x in cars:
    print(x)

print("\n")

cars.pop(5)
for x in cars:
    print(x)

print("\n")

cars.remove("BMW")
for x in cars:
    print(x)