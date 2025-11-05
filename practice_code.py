
class JobApplication:
    def __init__(self, name, age, experience, skills):
        self.name = name
        self.age = age
        self.experience = experience
        self.skills = skills
    
    def submit_application(self):
        print("Application submitted for {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Experience: {}".format(self.experience))
        print("Skills: {}".format(", ".join(self.skills)))

def main():
    print("Welcome to the job application system!")
    
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    experience = input("Enter your experience: ")
    skills = input("Enter your skills (separated by commas): ").split(",")
    
    application = JobApplication(name, age, experience, skills)
    application.submit_application()

if __name__ == "__main__":
    main()
