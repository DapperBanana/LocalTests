
class JobApplicationSystem:
    def __init__(self):
        self.applications = []

    def apply_job(self, name, email, resume):
        application = {
            'name': name,
            'email': email,
            'resume': resume
        }
        self.applications.append(application)
        print("Application submitted successfully!")

    def list_applications(self):
        if len(self.applications) == 0:
            print("No applications found.")
        else:
            for idx, application in enumerate(self.applications):
                print(f"Application {idx + 1}:")
                print(f"Name: {application['name']}")
                print(f"Email: {application['email']}")
                print(f"Resume: {application['resume']}")
                print()

# Main program loop
job_system = JobApplicationSystem()

while True:
    print("Job Application System")
    print("1. Apply for a job")
    print("2. List applications")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        resume = input("Enter your resume: ")
        job_system.apply_job(name, email, resume)
    elif choice == '2':
        job_system.list_applications()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Job Application System!")
