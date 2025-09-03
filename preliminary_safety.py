
class JobApplication:
    def __init__(self, name, email, phone_number, resume):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.resume = resume
        
    def display_info(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Phone Number:", self.phone_number)

# Sample job application system
job_applications = []

while True:
    print("Job Application System")
    print("1. Submit job application")
    print("2. View all job applications")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone_number = input("Enter your phone number: ")
        resume = input("Enter a link to your resume: ")
        
        new_application = JobApplication(name, email, phone_number, resume)
        job_applications.append(new_application)
        print("Job application submitted successfully!")
        
    elif choice == '2':
        if len(job_applications) == 0:
            print("No job applications submitted yet.")
        else:
            for i, application in enumerate(job_applications, 1):
                print("Job Application #", i)
                application.display_info()
                print()
    elif choice == '3':
        print("Exiting job application system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
