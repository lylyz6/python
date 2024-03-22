#8.1
def display_message():
    print("this paragraph explains what is function")
display_message()

#8.2
def favorite_book(title):
    print(f"One of my favorite books is {title}.")
favorite_book("Jouney to the West")

#8.3
def make_shirt(size, logo):
    print(f"The size of this shirt is {size}, logo is {logo}")
make_shirt("medium", "hello")

#8.4
def make_shirt(size, logo="I love Python"):
    print(f"The size of this shirt is {size}, logo is {logo}")
make_shirt("large")
make_shirt("small")
make_shirt("small", "hello")

def describe_city(city, country="China"):
    print(f"{city} is in {country}")
describe_city("shanghai")
describe_city("sanya")
describe_city("London", "UK")

#10.1
from pathlib import Path
guestlist = Path("guest.txt")
guestlist.write_text(input("what's your name?"))

#10.2
guests = ""
going = True
while going:
    guests += f"{input("what's your name?")}\n"
    request = input("continue writing? (y/n)")
    if request == "n":
        going = False
guestlist.write_text(guests)
