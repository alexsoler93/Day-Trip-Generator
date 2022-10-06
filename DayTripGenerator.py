import random

destinations = ['Las Vegas', 'New York City', 'Orlando', 'Chicago', 'Nashville']

restaurants = ['Pizza', 'Tacos', 'Ramen', 'Wings', 'Homestyle Cookin']

entertainment = ['Concert', 'Sight Seeing', 'Watch a Play', 'Visit the Museum', 'Amusement Park']

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

def pick_a_ent():
    ran_ent = random.choice(entertainment)
    if ran_ent == "Concert":
        print("Vibe out at a concert.")
    elif ran_ent == "Sight Seeing":
        print("Check out the sights!")
    elif ran_ent == "Watch a Play":
        print("Look! It's a marquee, enjoy a play!")
    elif ran_ent == "Visit a Museum":
        print("Expand your mind at the museum!")
    elif ran_ent == "Amusement Park":
        print("Get your thrills at the amusement park!")
    else:
        print()

def pick_a_tran():
    ran_tran = random.choice(transportation)
    if ran_tran == "Moped Scooter":
        print("Feel the breeze on a moped!")
    elif ran_tran == "Luxury Car":
        print("Get flashy in a luxury car!")
    elif ran_tran == "Helicopter":
        print("Take to the sky in a helicopter!")
    elif ran_tran == "Horseback":
        print("Giddy up! Go on horseback!")
    elif ran_tran == "Roller Skates":
        print("Glide on by on some roller skates!")
    else:
        print()

pick_a_place()
pick_a_food()
pick_a_ent()
pick_a_tran()

