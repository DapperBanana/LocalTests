
class JobApplication:
    def __init__(self, name, email, phone_number, skills, experience):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.skills = skills
        self.experience = experience

    def display_info(self):
        print("Name: ", self.name)
        print("Email: ", self.email)
        print("Phone Number: ", self.phone_number)
        print("Skills: ", self.skills)
        print("Experience: ", self.experience)


def main():
    print("Welcome to the job application system!")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone_number = input("Enter your phone number: ")
    skills = input("Enter your skills (separated by comma): ").split(',')
    experience = input("Enter your experience: ")

    job_application = JobApplication(name, email, phone_number, skills, experience)

    print("\nThank you for submitting your job application!")
    job_application.display_info()


if __name__ == "__main__":
    main()
