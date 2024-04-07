import tkinter as tk

class DatingAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dating App")

        # Define colors
        background_color = "#f0f0f0"
        label_color = "#333333"
        button_color = "#4CAF50"

        # Create and pack widgets with color settings
        self.label_name = tk.Label(root, text="Name:", fg=label_color, bg=background_color)
        self.label_name.pack()

        self.entry_name = tk.Entry(root)
        self.entry_name.pack()

        self.label_age = tk.Label(root, text="Age:", fg=label_color, bg=background_color)
        self.label_age.pack()

        self.entry_age = tk.Entry(root)
        self.entry_age.pack()

        self.label_interests = tk.Label(root, text="Interests:", fg=label_color, bg=background_color)
        self.label_interests.pack()

        self.listbox_interests = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.listbox_interests.insert(1, "Hiking")
        self.listbox_interests.insert(2, "Reading")
        self.listbox_interests.insert(3, "Cooking")
        self.listbox_interests.pack()

        self.button_submit = tk.Button(root, text="Submit", command=self.match_profiles, fg=label_color, bg=button_color)
        self.button_submit.pack()

        # Matched profiles display
        self.matched_profiles_label = tk.Label(root, text="Matched Profiles:", fg=label_color, bg=background_color)
        self.matched_profiles_label.pack()

        self.matched_profiles_text = tk.Text(root, height=10, width=50)
        self.matched_profiles_text.pack()

    def match_profiles(self):
        # Dummy logic for matching profiles (replace with actual matchmaking algorithm)
        name = self.entry_name.get()
        age = self.entry_age.get()
        selected_interests = [self.listbox_interests.get(idx) for idx in self.listbox_interests.curselection()]

        # Dummy matched profiles (replace with actual matching logic)
        matched_profiles = [
            {"name": "Alice", "age": 25, "interests": ["Hiking", "Reading"]},
            {"name": "Bob", "age": 30, "interests": ["Reading", "Cooking"]}
        ]

        # Display matched profiles
        self.matched_profiles_text.delete(1.0, tk.END)  # Clear previous content
        for profile in matched_profiles:
            self.matched_profiles_text.insert(tk.END, f"Name: {profile['name']}, Age: {profile['age']}, Interests: {', '.join(profile['interests'])}\n")

# Create the main application window
root = tk.Tk()

# Instantiate the DatingAppGUI class
app = DatingAppGUI(root)

# Run the Tkinter event loop
root.mainloop()