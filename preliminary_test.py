
class JobApplicationSystem:
    def __init__(self):
        self.applicants = []

    def apply_for_job(self, name, skills, experience):
        self.applicants.append({ 'name': name, 'skills': skills, 'experience': experience })

    def display_applicants(self):
        for app in self.applicants:
            print(f"Name: {app['name']}")
            print(f"Skills: {app['skills']}")
            print(f"Experience: {app['experience']}")
            print()

# Main program
job_system = JobApplicationSystem()

while True:
    print("Welcome to the Job Application System")
    print("1. Apply for a job")
    print("2. Display all applicants")
    print("3. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter your name: ")
        skills = input("Enter your skills (comma separated): ").split(',')
        experience = input("Enter your experience: ")
        job_system.apply_for_job(name, skills, experience)
        print("Application submitted successfully.")
    elif choice == 2:
        job_system.display_applicants()
    elif choice == 3:
        print("Thank you for using the Job Application System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
