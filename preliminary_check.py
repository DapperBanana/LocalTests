
class JobApplicationSystem:
    def __init__(self):
        self.applications = []

    def apply_for_job(self, name, position, experience):
        application = {
            'name': name,
            'position': position,
            'experience': experience
        }
        self.applications.append(application)
        print(f"Application for {name} for the position of {position} submitted.")

    def display_applications(self):
        for idx, app in enumerate(self.applications):
            print(f"Application {idx+1} - Name: {app['name']}, Position: {app['position']}, Experience: {app['experience']}")

# Main program
job_system = JobApplicationSystem()

while True:
    print("Welcome to the Job Application System!")
    print("1. Apply for a job")
    print("2. Display all applications")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter your name: ")
        position = input("Enter the position you are applying for: ")
        experience = input("Enter your experience: ")
        job_system.apply_for_job(name, position, experience)
    elif choice == 2:
        job_system.display_applications()
    elif choice == 3:
        print("Exiting the Job Application System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
