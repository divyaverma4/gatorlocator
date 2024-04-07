from user import UserProfile

# a function that counts similar preferences(personality, minimum 5 out of 10)
def personality_similarity(user1, user2):
    common_personality = sum(1 for a, b in zip(user1.personality_answers, user2.personality_answers) if a == b)
    return common_personality
    # for this function to work, we MUST have our answers for the 10 personality questions to be integers
    # example: user1_answers = [1, 2, 1, 2, 1, 1, 2, 1, 2, 'yes']
    # user2_answers = [2, 1, 2, 1, 2, 2, 1, 2, 1, 'no']


# a second functions that seeks an overlap between interests using sets()
def interests_similarity(user1, user2):
    common_interests = set(user1.interest_answers) & set(user2.interest_answers)
    return common_interests

#activity doesn't run unless called by match function
# basically just spits out possible activities based on similar interests
def activity(similarities_list):
    match_activity = []
    for item in similarities_list:
        if (item == "books"):
            match_activity.append("visit the local bookstore!")
        elif (item == "plants"):
            match_activity.append("visit the local greenhouse!")
        elif (item == "anime"):
            match_activity.append("have an anime watch night!")
    return match_activity

# takes 2 users, assesses their compatibility
# if compatible, returns their activity list
def match(user1, user2):
    if (personality_similarity(user1, user2) >= 5):
        similarities_list = interests_similarity(user1, user2)
        if similarities_list >= 3:
            return activity(similarities_list)
        else:
            return 0


# testing:
user1 = UserProfile("Anna", 19, "Female", "Statistics", [1,2,2,2,1,1,1,1,2,"yes"], ["raves", "anime", "books", "gym", "plants"] )
user1.save_to_database()
user2 = UserProfile("Pao", 19, "Female", "CS", [1,2,1,2,1,1,1,1,2,"no"], ["Yoga", "anime", "books", "Vinyls", "plants"] )
user2.save_to_database()

print(personality_similarity(user1, user2))
print(interests_similarity(user1, user2))

user1and2 = match(user1, user2)
if (user1and2 != 0):
    print("Congratulations, you've been matched! Together you should: \n")
    for item in user1and2:
        print(item + "\n")
