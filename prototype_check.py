
class JobApplication:
    def __init__(self):
        self.applicant_name = ""
        self.job_title = ""
        self.experience = ""
        self.skills = []

    def apply_for_job(self):
        print("Welcome to the job application system")
        self.applicant_name = input("Enter your name: ")
        self.job_title = input("Enter the job title you are applying for: ")
        self.experience = input("Enter your experience: ")
        skills_str = input("Enter your skills, separated by commas: ")
        self.skills = skills_str.split(",")

    def display_application(self):
        print("\nJob Application Summary:")
        print(f"Applicant Name: {self.applicant_name}")
        print(f"Job Title: {self.job_title}")
        print(f"Experience: {self.experience}")
        print("Skills:")
        for skill in self.skills:
            print(f"- {skill}")

# Main program
job_application = JobApplication()
job_application.apply_for_job()
job_application.display_application()
