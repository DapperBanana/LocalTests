
class JobApplicationSystem:
    def __init__(self):
        self.applicants = []

    def apply_for_job(self, name, resume):
        self.applicants.append({"name": name, "resume": resume})
        print(f"Thank you {name} for applying for the job. Your application has been received.")

    def review_applications(self):
        print("List of applicants:")
        for idx, applicant in enumerate(self.applicants, 1):
            print(f"{idx}. {applicant['name']}")

    def select_candidate(self, idx):
        if idx < 1 or idx > len(self.applicants):
            print("Invalid candidate selection")
        else:
            selected_candidate = self.applicants[idx - 1]
            print(f"{selected_candidate['name']} has been selected for the job.")
            del self.applicants[idx - 1]

# Sample usage
job_app_system = JobApplicationSystem()

job_app_system.apply_for_job("Alice", "Experienced software engineer")
job_app_system.apply_for_job("Bob", "Fresh graduate with strong programming skills")

job_app_system.review_applications()

job_app_system.select_candidate(1)

job_app_system.review_applications()
