import random

destinations = ['Las Vegas', 'New York City', 'Orlando', 'Chicago', 'Nashville']

restaurants = ['Pizza Time', 'Taco Tuesday', 'Ramen Bowls', 'Wings Wing Wings', 'Homestyle Cookin']

entertainment = ['Music Concert', 'Sight Seeing', 'Watch a Play', 'Visit the Museum', 'Amusement Park']

transportation = ['Moped Scooter', 'Luxury Car', 'Helicopter', 'Horseback', 'Roller Skates']


# def generate_trip():
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

pick_a_place()



