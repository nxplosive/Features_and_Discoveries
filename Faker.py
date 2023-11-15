from faker import Faker

f = Faker(["ru_RU", "fr_FR"])

print()
for _ in range(10):
    print(f.sentence())
print()

for _ in range(5):
    print(f.hexify(text="MAC: ^^:^^:^^:^^:^^:^^", upper=True))
print()

for _ in range(3):
    print(f.name())
print()

print(f.address())
print(f.ipv4_private())
print(f.ipv4_public())
#print(f.zipcode())
print(f.locale())
print(f.license_plate())
print(f.phone_number())
print()

for _ in range(10):
    print(f.unique.random_int(min=1, max=10))
print()

for _ in range(5):
    print(f.bothify(text="????-######-??", letters="abcdef"))