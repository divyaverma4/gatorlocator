# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from user import User

def preferenceCompatibility(user1, user2):
    user1pref = user1.getPreference
    user2pref = user2.getPreference
    count = 0
    match = False

    for x in len(user1pref):
        if user1pref[x] == user2pref[x]:
            count+= 1

    if count >= 3:
        match = True

    return match

def interestCompatibility(user1, user2):
    user1interest = user1.getInterest
    user2interest = user2.getInterest
    count = 0
    match = False
    sameinterests = []

    for x in len(user1interest):
        if user1interest[x] == user2interest[x]:
            count+= 1
            sameinterests.append(user1interest[x])

    if len(sameinterests) >= 3:
        match = True

    if match:
        return sameinterests
    else:
        return match


if __name__ == '__main__':



