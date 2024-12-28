
class JobApplication:
    def __init__(self, name, email, phone_number, experience, skills):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.experience = experience
        self.skills = skills
    
    def display_application(self):
        print("Job Application Details:")
        print("Name:", self.name)
        print("Email:", self.email)
        print("Phone Number:", self.phone_number)
        print("Experience:", self.experience)
        print("Skills:", self.skills)

def main():
    print("Welcome to the Job Application System")
    
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    phone_number = input("Enter your phone number: ")
    experience = input("Enter your work experience: ")
    skills = input("Enter your skills (comma separated): ")
    
    skills_list = skills.split(",")
    
    application = JobApplication(name, email, phone_number, experience, skills_list)
    application.display_application()
    
if __name__ == "__main__":
    main()
