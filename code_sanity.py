
class JobApplication:
    def __init__(self, name, age, experience, skills):
        self.name = name
        self.age = age
        self.experience = experience
        self.skills = skills

    def submit_application(self):
        print("Application submitted for", self.name)

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Experience:", self.experience)
        print("Skills:", self.skills)


def main():
    print("Welcome to the Job Application System")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    experience = input("Enter your experience: ")
    skills = input("Enter your skills (separated by commas): ").split(",")

    application = JobApplication(name, age, experience, skills)

    print("\nJob Application Details:")
    application.display_details()

    submit = input("\nSubmit application? (yes/no): ")
    if submit.lower() == "yes":
        application.submit_application()
        print("Thank you for applying!")
    else:
        print("Application not submitted. Goodbye!")


if __name__ == "__main__":
    main()
