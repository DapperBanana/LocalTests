
class JobApplicationSystem:
    def __init__(self):
        self.applicants = []
    
    def create_application(self):
        name = input("Enter your name: ")
        email = input("Enter your email address: ")
        resume = input("Paste your resume here: ")
        
        applicant = {
            "name": name,
            "email": email,
            "resume": resume
        }
        
        self.applicants.append(applicant)
        print("Application submitted successfully!")
    
    def view_applications(self):
        if not self.applicants:
            print("No applications to display.")
        else:
            for idx, applicant in enumerate(self.applicants):
                print(f"Application {idx + 1}:")
                print(f"Name: {applicant['name']}")
                print(f"Email: {applicant['email']}")
                print(f"Resume: {applicant['resume']}")
                print()
    
    def run(self):
        while True:
            print("Job Application System")
            print("1. Create new application")
            print("2. View all applications")
            print("3. Quit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.create_application()
            elif choice == "2":
                self.view_applications()
            elif choice == "3":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")
        
        
job_app_system = JobApplicationSystem()
job_app_system.run()
