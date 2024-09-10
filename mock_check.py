
class Applicant:
    def __init__(self, name, email, phone_number, resume):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.resume = resume

class Job:
    def __init__(self, title, description, requirements):
        self.title = title
        self.description = description
        self.requirements = requirements

class JobApplicationSystem:
    def __init__(self):
        self.applicants = []
        self.jobs = []

    def add_applicant(self, applicant):
        self.applicants.append(applicant)

    def add_job(self, job):
        self.jobs.append(job)

    def display_jobs(self):
        print("Available Jobs:")
        for ind, job in enumerate(self.jobs):
            print(f"{ind+1}. {job.title}")
            print(f"Description: {job.description}")
            print(f"Requirements: {job.requirements}")
            print()

    def apply_for_job(self, applicant, job_index):
        job = self.jobs[job_index - 1]
        print(f"Applicant {applicant.name} has applied for the job: {job.title}")

# Sample usage
job_app_system = JobApplicationSystem()

job1 = Job("Software Engineer", "Develop software applications using Python", "Computer Science degree, Python programming skills")
job2 = Job("Marketing Coordinator", "Develop marketing strategies for company products", "Marketing degree, strong communication skills")

job_app_system.add_job(job1)
job_app_system.add_job(job2)

applicant1 = Applicant("John Doe", "johndoe@email.com", "123-456-7890", "Software Engineer with 3 years of experience")
applicant2 = Applicant("Jane Smith", "janesmith@email.com", "987-654-3210", "Marketing Coordinator with 5 years of experience")

job_app_system.add_applicant(applicant1)
job_app_system.add_applicant(applicant2)

job_app_system.display_jobs()

applicant_choice = int(input("Enter the job number you want to apply for: "))
applicant = job_app_system.applicants[0]  # Assuming we have only one applicant in this example
job_app_system.apply_for_job(applicant, applicant_choice)
