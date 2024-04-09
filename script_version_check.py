
class JobApplication:
    def __init__(self, name, email, phone, resume):
        self.name = name
        self.email = email
        self.phone = phone
        self.resume = resume

    def display_info(self):
        print("Name: ", self.name)
        print("Email: ", self.email)
        print("Phone: ", self.phone)
        print("Resume: ", self.resume)

def main():
    print("Welcome to the job application system!")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    resume = input("Enter your resume: ")

    application = JobApplication(name, email, phone, resume)

    print("\nYour job application details:")
    application.display_info()

if __name__ == "__main__":
    main()
