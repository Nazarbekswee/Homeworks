# T-1
fruits = ['apple', 'banana', 'orange', 'kiwi']

for i in fruits:
    print(i)
#T-2
names = ['ali', 'vali', 'hasan', 'husan']

for name in names:
    print(name.upper())
#T-3
cars = ['bmw', 'mers', 'nexia', 'malibu', 'cobalt']

for car in cars:
    print(car[0])
#T-4
countries = ['UZBEKISTAN', 'RUSSIA', 'TURKEY', 'USA']

for country in countries:
    print(country.lower())
#T-5
names = ['ali', 'sardor', 'abdulloh', 'aziz']

for name in names:
    print(name, '-', len(name), 'ta harf')
#T-6
animals = ['cat', 'dog', 'lion', 'tiger']

for i in range(len(animals)):
    animals[i] = animals[i].upper()

    print(animals)
#T-7
names = ['ali', 'vali', 'sardor', 'aziz']

for name in names:
    print(name.upper())
#T-8
names = ['ali', 'hasan', 'husan', 'sardor']

for name in names:
    print(name.capitalize())
#T-9
names = ['ali', 'vali', 'hasan', 'husan', 'sardor', 'aziz']

for i in range(len(names)):
    if i % 2 == 0:
            print(names[i])
#T-10
animals = ['tiger', 'lion', 'elephant', 'rabbit']

for animal in animals:
    print(animal[0], '-', animal[-1])
#T-11
words = ['python', 'programming', 'computer', 'developer']

for word in words:
    print(word[0].upper() + word[1:-1] + word[-1].upper())
#T-12
cars = ['bmw', 'nexia', 'malibu', 'cobalt', 'damas']

for i in range(len(cars)):
    cars[i] = cars[i].upper()

    print(cars)
#T-13
name = input("Ism kiriting: ")
n = int(input("Necha marta chiqarilsin: "))

for i in range(n):
    print(name)
#T-14
fruits = []

n = int(input("Nechta meva kiritmoqchisiz: "))

for i in range(n):
    fruit = input(f"{i+1}-mevani kiriting: ")
    fruits.append(fruit)

    print("Mevalar:", fruits)
