
class JobApplicationSystem:
    def __init__(self):
        self.applications = []

    def submit_application(self, name, email, resume):
        application = {
            'name': name,
            'email': email,
            'resume': resume
        }
        self.applications.append(application)
        print("Application submitted successfully!")

    def view_applications(self):
        for i, application in enumerate(self.applications):
            print(f"Application {i+1}:")
            print(f"Name: {application['name']}")
            print(f"Email: {application['email']}")
            print(f"Resume: {application['resume']}")
            print()

job_application_system = JobApplicationSystem()

while True:
    print("1. Submit Application")
    print("2. View Applications")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        resume = input("Enter your resume: ")
        job_application_system.submit_application(name, email, resume)
    elif choice == '2':
        job_application_system.view_applications()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the job application system.")
