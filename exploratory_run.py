
class JobApplication:
    def __init__(self, name, email, experience):
        self.name = name
        self.email = email
        self.experience = experience
    
    def display_info(self):
        print("Name: ", self.name)
        print("Email: ", self.email)
        print("Experience: ", self.experience)

class JobApplicationSystem:
    def __init__(self):
        self.applications = []
    
    def apply_for_job(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        experience = input("Enter your experience: ")
        
        application = JobApplication(name, email, experience)
        self.applications.append(application)
        
        print("Thank you for applying!")
    
    def display_applications(self):
        for idx, app in enumerate(self.applications, 1):
            print("Application #", idx)
            app.display_info()

# Main program
job_system = JobApplicationSystem()

while True:
    print("\nJob Application System")
    print("1. Apply for job")
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
