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

#3.4 to 3.7
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

