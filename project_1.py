import random

# Features:

# (5 points): As a developer, I want to make at least three commits with descriptive messages.

# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainments in their own separate lists.

def the_list_we_want():
    what_user_wants = input('What do you want to choose next? (Type one of these options: Destination, Transportation, or Entertainment) ')
    if what_user_wants == 'Destination':
        return ['Colorado', 'Arizona', 'South Dakota', 'California']
    if what_user_wants == 'Transportation':
        return ['Plane', 'Bus', 'Car', 'Train', 'RV']
    if what_user_wants == 'Entertainment':
        return ['Biking', 'Skiing', 'Rafting', 'Sky Diving', 'Scuba Diving', 'Underwater Basket Weaving']

# (5 points): As a user, I want a destination to be randomly selected for my day trip.

def random_choice():
    our_list = the_list_we_want()
    random.choice(our_list)
    user_y_or_n = input('Are you happy with this selection? Yes or No ')
    if user_y_or_n == 'Yes':
        return our_list
    else:
        random_choice()
        
print(random_choice())








# destinations =[....]
# restaurants = [...]

# def randomChoice(someList):
#     # return a choice

# def genAllChoices():
#     # for store in variables
    # chosenDest = randomChoice(destinations)

# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.

# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.

# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

# (10 points): As a user, I want to display my completed trip in the console.

# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!