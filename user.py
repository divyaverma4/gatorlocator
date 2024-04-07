from pymongo import MongoClient
class UserProfile:
    def __init__(self, name, age, gender, major, personality_answers, interest_answers):
        self.name = name
        self.age = age
        self.gender = gender
        self.major = major
        self.personality_answers = personality_answers
        self.interest_answers = interest_answers

    @staticmethod
    def connect_to_database():
        # Connect to MongoDB (assuming it's running locally on the default port)
        client = MongoClient('mongodb+srv://sailordawgggg:12345@cluster0.tjofgji.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        # Access the database and collection
        db = client['gatorlocator_database']
        collection = db['user_profiles']
        return collection

    def save_to_database(self):
        # Connect to MongoDB and get the collection
        collection = self.connect_to_database()
        # Convert UserProfile instance to a dictionary
        user_data = {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'personality_answers': self.personality_answers,
            'interests': self.interest_answers
        }
        # Insert the user data into the collection
        collection.insert_one(user_data)




