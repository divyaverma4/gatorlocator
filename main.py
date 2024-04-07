import tkinter as tk
from pymongo import MongoClient
from user import UserProfile
from matching import interests_similarity


class GatorLocatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GatorLocator")

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Name entry
        self.label_name = tk.Label(self.root, text="Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        # Age entry
        self.label_age = tk.Label(self.root, text="Age:")
        self.label_age.grid(row=1, column=0, padx=10, pady=5)
        self.entry_age = tk.Entry(self.root)
        self.entry_age.grid(row=1, column=1, padx=10, pady=5)

        # Gender entry
        self.label_gender = tk.Label(self.root, text="Gender:")
        self.label_gender.grid(row=2, column=0, padx=10, pady=5)
        self.entry_gender = tk.Entry(self.root)
        self.entry_gender.grid(row=2, column=1, padx=10, pady=5)

        # Major entry
        self.label_major = tk.Label(self.root, text="Major:")
        self.label_major.grid(row=3, column=0, padx=10, pady=5)
        self.entry_major = tk.Entry(self.root)
        self.entry_major.grid(row=3, column=1, padx=10, pady=5)

        # Interests entry
        self.label_interests = tk.Label(self.root, text="Interests (comma-separated):")
        self.label_interests.grid(row=4, column=0, padx=10, pady=5)
        self.entry_interests = tk.Entry(self.root)
        self.entry_interests.grid(row=4, column=1, padx=10, pady=5)

        # Submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_profile)
        self.submit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Matching results display
        self.matching_results_text = tk.Text(self.root, height=10, width=50)
        self.matching_results_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def submit_profile(self):
        # Extract user input
        name = self.entry_name.get()
        age = int(self.entry_age.get())
        gender = self.entry_gender.get()
        major = self.entry_major.get()
        interests = self.entry_interests.get().split(",")

        # Create a UserProfile instance
        user_profile = UserProfile(name, age, gender, major, interests)

        # Save to MongoDB
        user_profile.save_to_database()

        # Display matching results
        self.display_matching_results(user_profile)

    def display_matching_results(self, user_profile):       # wont display matching results due to not having more variables (userprofile asks for more) and also because database is empty - so it wont match.
        # Connect to MongoDB and get user profiles collection
        client = MongoClient(
            'mongodb+srv://sailordawgggg:12345@cluster0.tjofgji.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        db = client['gatorlocator_database']
        collection = db['user_profiles']

        # Retrieve all user profiles from the database
        all_profiles = collection.find()

        # Perform matching and display results
        self.matching_results_text.delete(1.0, tk.END)  # Clear previous content
        for profile in all_profiles:
            other_profile = UserProfile(profile['name'], profile['age'], profile['gender'], profile['major'], None,
                                        profile['interests'])
            if user_profile != other_profile:  # Exclude the user's own profile from matching
                common_interests = interests_similarity(user_profile, other_profile)
                self.matching_results_text.insert(tk.END, f"Name: {other_profile.name}\n")
                self.matching_results_text.insert(tk.END, f"Common Interests: {', '.join(common_interests)}\n\n")


# Create the main application window
try:
    root = tk.Tk()
except Exception as e:
    print("An error occurred while creating the Tkinter window:", e)
else:
    # Instantiate the GatorLocatorApp class
    app = GatorLocatorApp(root)
    # Run the Tkinter event loop
    root.mainloop()
