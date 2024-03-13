
class JobApplicationSystem:
    def __init__(self):
        self.applications = []

    def apply_for_job(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        resume = input("Attach your resume (file name): ")
        cover_letter = input("Enter your cover letter: ")

        application = {
            "name": name,
            "email": email,
            "resume": resume,
            "cover_letter": cover_letter
        }

        self.applications.append(application)
        print("Application submitted successfully!")

    def display_applications(self):
        if not self.applications:
            print("No applications found.")
        else:
            print("List of applications:")
            for index, application in enumerate(self.applications):
                print(f"Application {index + 1}:")
                print(f"Name: {application['name']}")
                print(f"Email: {application['email']}")
                print(f"Resume: {application['resume']}")
                print(f"Cover Letter: {application['cover_letter']}")
                print("")

# Main program
job_system = JobApplicationSystem()

while True:
    print("1. Apply for a job")
    print("2. Display applications")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        job_system.apply_for_job()
    elif choice == '2':
        job_system.display_applications()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
