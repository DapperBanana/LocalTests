
class JobApplication:
    def __init__(self, name, age, experience, skills):
        self.name = name
        self.age = age
        self.experience = experience
        self.skills = skills

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Experience: {self.experience} years")
        print("Skills:")
        for skill in self.skills:
            print(f"- {skill}")

# Main code
print("Welcome to the job application system!")
print("Please enter your information below:")

name = input("Name: ")
age = int(input("Age: "))
experience = int(input("Years of experience: "))
skills = input("Enter your skills (separated by commas): ").split(",")

application = JobApplication(name, age, experience, skills)

print("\nYour job application has been submitted. Here is your information:")
application.display_info()
