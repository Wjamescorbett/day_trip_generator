import random

destinations = ['Colorado', 'Arizona', 'South Dakota', 'California']
restaurants = ['Applebees', 'Silver Diner', 'Golden Corral', 'TGI Fridays', 'Bar Louie']
transportation = ['Plane', 'Bus', 'Car', 'Train', 'RV']
entertainment = ['Biking', 'Skiing', 'Rafting', 'Sky Diving', 'Scuba Diving', 'Underwater Basket Weaving']

def greeting_message():
    name = input("Let's start with your name. Who are you? ")
    print(f"Hello {name}, let's generate your trip! ")

def random_choice(some_list):
    random_output = random.choice(some_list)
    return random_output

def choose_destination():
    destination_selected = random_choice(destinations)
    return destination_selected

def choose_restaurant():
    restaurant_selected = random_choice(restaurants)
    return restaurant_selected

def choose_transportation():
    transpo_selected = random.choice(transportation)
    return transpo_selected

def choose_entertainment():
    ent_selected = random.choice(entertainment)
    return ent_selected

def meat_and_potatoes():
    temp_des = choose_destination()
    real_des = temp_des
    print(f"Great! You got {real_des}. Now Let's get a Restaurant. ")
    temp_res = choose_restaurant()
    real_res = temp_res
    print(f"You're restaurant is {real_res}! Transportation is next. ")
    temp_transpo = choose_transportation()
    real_transpo = temp_transpo
    print(f"You're going to get to {real_des} in a {real_transpo}! ")
    temp_ent = choose_entertainment()
    real_ent = temp_ent
    print(f"After eating, your entertainment is {real_ent}! What fun. ")
    happy = input('Do you want to re-generate this trip? ')
    if happy == 'Yes':
        meat_and_potatoes()
    else:
        print(f"Wonderful! Your trip is complete. You will be traveling to {real_des} in a {real_transpo}. You will eat at {real_res} and then go {real_ent}.")

greeting_message()
meat_and_potatoes()


# Features:

# (5 points): As a developer, I want to make at least three commits with descriptive messages.

# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainments in their own separate lists.

# (5 points): As a user, I want a destination to be randomly selected for my day trip.

# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.

# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.

# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

# (10 points): As a user, I want to display my completed trip in the console.

# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

