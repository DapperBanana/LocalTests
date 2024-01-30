
class JobApplication:
    def __init__(self, name, age, experience_years, job_title):
        self.name = name
        self.age = age
        self.experience_years = experience_years
        self.job_title = job_title
    
    def display(self):
        print("Applicant Name:", self.name)
        print("Age:", self.age)
        print("Years of Experience:", self.experience_years)
        print("Job Title:", self.job_title)

def apply_job():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    experience_years = int(input("Enter years of experience: "))
    job_title = input("Enter the job title you are applying for: ")
    
    application = JobApplication(name, age, experience_years, job_title)
    return application

def main():
    # Simulated job application process
    print("Welcome to the Job Application System!")
    print("--------------------------------------")
    
    num_applications = int(input("Enter the number of applications: "))
    applications = []
    
    for i in range(num_applications):
        print("\nApplication", i + 1)
        print("--------------")
        application = apply_job()
        applications.append(application)
    
    print("\nJob Applications Summary")
    print("------------------------")
    
    for application in applications:
        application.display()
        print("")

if __name__ == "__main__":
    main()
