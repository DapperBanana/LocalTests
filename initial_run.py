
class Job:
    def __init__(self, title, description, requirements):
        self.title = title
        self.description = description
        self.requirements = requirements

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nRequirements: {self.requirements}"


class JobApplicationSystem:
    def __init__(self):
        self.jobs = []

    def add_job(self, title, description, requirements):
        job = Job(title, description, requirements)
        self.jobs.append(job)

    def display_jobs(self):
        for i, job in enumerate(self.jobs):
            print(f"Job {i+1}:")
            print(job)
            print("\n")

    def apply_for_job(self):
        job_number = int(input("Enter the job number you want to apply for: "))
        if job_number <= len(self.jobs):
            print("You have successfully applied for the job!")
        else:
            print("Invalid job number. Please try again.")

# Creating a job application system
job_system = JobApplicationSystem()

# Adding jobs to the system
job_system.add_job("Software Engineer", "Developing software applications", "Bachelor's degree in Computer Science")
job_system.add_job("Marketing Manager", "Creating and implementing marketing strategies", "Bachelor's degree in Marketing")

# Displaying available jobs
job_system.display_jobs()

# Applying for a job
job_system.apply_for_job()
