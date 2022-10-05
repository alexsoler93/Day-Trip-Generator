import random

destinations = ['Las Vegas', 'New York City', 'Orlando', 'Chicago', 'Nashville']

restaurants = ['Pizza', 'Tacos', 'Ramen', 'Wings', 'Homestyle Cookin']

entertainment = ['Music Concert', 'Sight Seeing', 'Watch a Play', 'Visit the Museum', 'Amusement Park']

transportation = ['Moped Scooter', 'Luxury Car', 'Helicopter', 'Horseback', 'Roller Skates']


# random functions key, so that i don't forget.

#     ran_destination = print(random.choice(destinations))

#     ran_restaurants = print(random.choice(restaurants))

#     ran_entertainment = print(random.choice(entertainment))

#     ran_transportation = print(random.choice(transportation))

def pick_a_place():
    ran_dest = random.choice(destinations)
    if ran_dest == "Las Vegas":
        print("Las Vegas: Viva Las Vegas")
    elif ran_dest == "New York City":
        print("New York City: Hello Big Apple!")
    elif ran_dest == "Orlando":
        print("Orlando: Fun in the sun")
    elif ran_dest == "Chicago":
        print("Chicago: The Windy City!")
    elif ran_dest == "Nashville":
        print("Nashville: There's nothing a trip here can't solve!")
    else:
        print()

def pick_a_food():
    ran_rest = random.choice(restaurants)
    if ran_rest == "Pizza":
        print("It's pizza time!")
    elif ran_rest == "Tacos":
        print("Everyday is Taco Tuesday!")
    elif ran_rest == "Ramen":
        print("Grab a bowl of ramen.")
    elif ran_rest == "Wings":
        print("Can't go wrong with wings!")
    elif ran_rest == "Homestyle Cookin":
        print("Soothe your soul with some homestyle cookin'")
    else:
        print()

pick_a_place()
pick_a_food()



