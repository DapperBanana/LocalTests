
class JobApplication:
    def __init__(self, name, email, phone, resume):
        self.name = name
        self.email = email
        self.phone = phone
        self.resume = resume
    
    def display_application(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print("Resume:")
        print(self.resume)

def main():
    print("Welcome to the job application system!")
    
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    resume = input("Enter your resume: ")
    
    new_application = JobApplication(name, email, phone, resume)
    
    print("\nYour job application details:")
    new_application.display_application()
    
if __name__ == "__main__":
    main()
