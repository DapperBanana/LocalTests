
class JobApplication:
    def __init__(self, name, email, phone, resume):
        self.name = name
        self.email = email
        self.phone = phone
        self.resume = resume

    def display_application(self):
        print("Name: " + self.name)
        print("Email: " + self.email)
        print("Phone: " + self.phone)
        print("Resume: " + self.resume)

# Main program
print("Welcome to the Job Application System")

name = input("Enter your name: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
resume = input("Attach your resume: ")

new_application = JobApplication(name, email, phone, resume)

print("\nJob application submitted successfully.")
print("\nApplication Details:")
new_application.display_application()
