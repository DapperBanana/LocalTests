
class JobApplication:
    def __init__(self, name, age, experience, skills):
        self.name = name
        self.age = age
        self.experience = experience
        self.skills = skills

def print_application(application):
    print("Name: ", application.name)
    print("Age: ", application.age)
    print("Experience: ", application.experience)
    print("Skills: ", application.skills)

def main():
    applications = []

    while True:
        print("Job Application System")
        print("1. Submit Application")
        print("2. View Applications")
        print("3. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            experience = input("Enter experience: ")
            skills = input("Enter skills (comma separated): ").split(",")

            application = JobApplication(name, age, experience, skills)
            applications.append(application)
            print("Application submitted successfully!")

        elif choice == "2":
            if len(applications) == 0:
                print("No applications submitted yet.")
            else:
                print("Applications:")
                for application in applications:
                    print_application(application)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
