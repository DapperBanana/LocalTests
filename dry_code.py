
# Define the Job Application class
class JobApplication:
    def __init__(self):
        self.name = ''
        self.age = ''
        self.email = ''
        self.qualifications = []

    def submit_application(self):
        # Get personal information from the user
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.email = input("Enter your email address: ")
        
        # Get qualifications from the user
        num_of_qualifications = int(input("Enter the number of qualifications: "))
        for i in range(num_of_qualifications):
            qualification = input(f"Enter qualification {i+1}: ")
            self.qualifications.append(qualification)
        
        # Display summary of the job application
        print("\nJob Application Summary:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print("Qualifications: ")
        for qualification in self.qualifications:
            print("- " + qualification)

# Create a new job application
job_application = JobApplication()

# Start the application process
print("Welcome to the Job Application System")
print("-------------------------------------")

job_application.submit_application()
