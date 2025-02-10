
class JobApplication:
    def __init__(self, name, age, experience, skills):
        self.name = name
        self.age = age
        self.experience = experience
        self.skills = skills
    
    def display_application(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Experience:", self.experience)
        print("Skills:", self.skills)
        
def main():
    print("--- Job Application System ---")
    
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    experience = input("Enter your experience: ")
    skills = input("Enter your skills separated by commas: ").split(",")
    
    application = JobApplication(name, age, experience, skills)
    
    print("\n--- Job Application Summary ---")
    application.display_application()
    
if __name__ == "__main__":
    main()
