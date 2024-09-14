
class JobApplicationSystem:
    def __init__(self):
        self.applications = []

    def apply_for_job(self, name, email, position):
        application = {
            'name': name,
            'email': email,
            'position': position
        }
        self.applications.append(application)
        print(f"Application for {position} submitted successfully.")

    def list_applications(self):
        for i, application in enumerate(self.applications):
            print(f"Application {i+1}:")
            print(f"Name: {application['name']}")
            print(f"Email: {application['email']}")
            print(f"Position: {application['position']}")
            print("------------------------")

# Main program
job_system = JobApplicationSystem()

while True:
    print("\nJob Application System")
    print("1. Apply for a Job")
    print("2. List Applications")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        position = input("Enter the position you are applying for: ")
        job_system.apply_for_job(name, email, position)
    elif choice == '2':
        job_system.list_applications()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
