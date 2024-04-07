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

# testing:
user1 = UserProfile("Anna", 19, "Female", "Statistics", [1,2,2,2,1,1,1,1,2,"yes"], ["raves", "anime", "books", "gym", "plants"] )

user2 = UserProfile("Pao", 19, "Female", "CS", [1,2,1,2,1,1,1,1,2,"no"], ["Yoga", "anime", "books", "Vinyls", "plants"] )
