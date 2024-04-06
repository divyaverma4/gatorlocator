class User:

    #constructor
    #takes 2 parameters: an array of preferences and an array of interests
    #array of preferences in order: 0 for no option, 1 for yes option (or however we want to do it)
    #same for interests

    def __init__(self, preference, interest):
        self.preference = preference
        self.interest = interest

    def getPreference(self):
        return self.preference

    def getInterest(self):
        return self.interest
