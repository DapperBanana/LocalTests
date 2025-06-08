
class JobApplicationSystem:
    
    def __init__(self):
        self.applications = []
    
    def display_menu(self):
        print("Job Application System Menu")
        print("1. Apply for a job")
        print("2. View all applications")
        print("3. Exit")
    
    def apply_for_job(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        position = input("Enter the position you are applying for: ")
        
        application = {
            "name": name,
            "email": email,
            "position": position
        }
        
        self.applications.append(application)
        print("Application submitted successfully!")
    
    def view_applications(self):
        if len(self.applications) == 0:
            print("No applications submitted yet.")
        else:
            for index, application in enumerate(self.applications, 1):
                print(f"Application {index}:")
                print(f"Name: {application['name']}")
                print(f"Email: {application['email']}")
                print(f"Position: {application['position']}")
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.apply_for_job()
            elif choice == '2':
                self.view_applications()
            elif choice == '3':
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    job_application_system = JobApplicationSystem()
    job_application_system.run()
