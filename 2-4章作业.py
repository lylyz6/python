#2.3
name = "eric"
sentence1 = "Hello "
sentence2 = ", would you like to learn some Python today?"
print(f"{sentence1}{name}{sentence2}")

#2.4
name_of_god = "slay_conceit"
print("",name_of_god.upper(),"\n",name_of_god.lower(),"\n",name_of_god.title())

#2.5 & 2.6
Famous_player = "Pager"
sentence = '"How to play one map? Just play this map more."'
print(Famous_player,"once said,",sentence)

#3.1 & 3.2
player_list = ["Piggice", "Tomoe", "Bochi the osu", "Slay_conceit", "Eveliya", "NaimuTongzi", "iz6"]
a=0
while a < 6:
    print(f"hello,{player_list[a]}")
    a = a + 1

#3.4
Guests = ["mom", "dad", "sister", "brother"]
b = 0
while b < 4:
    print(f"hello, {Guests[b]}. Welcome to my house!")
    b = b + 1
can_not_come_Guest=Guests.pop(3)
print(can_not_come_Guest)
Guests.append("grandfather")
b = 0
while b < 4:
    print(f"hello, {Guests[b]}. Welcome to my house!")
    b = b + 1
Guests.insert(0,"aunt")
Guests.insert(2,"uncle")
Guests.append("grandmother")
print(f"I found a bigger table, so I invite {Guests[0]}, {Guests[2]},{Guests[-1]}, too.")
b = 0
while b < 7:
    print(f"hello, {Guests[b]}. Welcome to my house!")
    b = b + 1
b = 0
while b < 5:
    print(f"Sorry, {Guests[0]}. I can't invite you to have dinner.")
    Guests.pop(0)
    b = b+1
b = 0
while b < 2:
    print(f"Hi, {Guests[b]}. You can also come to have dinner with me, I will appreciate if you can come!")
    b = b + 1
b = 0
while b < 2:
    del Guests[0]
    b = b + 1
print(Guests)

#3.8
Place = ["England", "Japan", "France", "Australia", "Canada" ]
print(Place)
Sorted_Place = sorted(Place)
print(Place)
reSorted_Place = sorted(Place, reverse = True)
print(Place)
Place.reverse()
print(Place)
Place.reverse()
print(Place)
Place.sort()
print(Place)
Place.sort(reverse = True)
print(Place)

#3.9
print(f"I will invite {len(Guests) + 2} people to have lunch. ")

#4.1
Fruits = ["apple", "orange", "banana"]
for fruit in Fruits:
    print(f"I like {fruit}")
print(f"I like {Fruits[0]}, {Fruits[1]},{Fruits[2]}. So I love fruit! ")

#4.2
animals = ["cat", "dog", "fox"]
for animal in animals:
    print(animal)
for animal in animals:
    print(f"A {animal} would make a great pet")
print("Any of these animals would make a great pet!")

#4.3 to 4.5
for number in range(1, 21):
    print(number)
list100w = list(range(1, 1000001))
print(min(list100w),max(list100w),sum(list100w))

#4.6
singles = [i for i in range(1, 21, 2)]
for single in singles:
    print(single)

#4.7
triples = [i for i in range(3, 31, 3)]
for triple in triples:
    print(triple)

#4.8
cubes = [i ** 3 for i in range(1, 11)]
for cube in cubes:
    print(cube)

#4.10
print(f"The first three items in the list are {Place[:3]}")
print(f"Three items from the middle of the list are {Place[1:4]}")
print(f"The last three items in the list are {Place[2:]}")

#4.11
Friend_Fruits = Fruits[:]
Fruits.append("appear")
Friend_Fruits.append("watermelon")
print("My favorite fruits are")
for fruit in Fruits:
    print(fruit)
print("My friend's favorite fruits are")
for fruit in Friend_Fruits:
    print(fruit)

#4.13
menu = ("rice", "noodle", "egg", "water", "juice")
for food in menu:
    print(food)
menu = ("milk", "beef", "egg", "water", "juice")
for food in menu:
    print(food)