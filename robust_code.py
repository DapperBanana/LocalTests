
class JobApplicationSystem:
    def __init__(self):
        self.applicants = []

    def display_menu(self):
        print("Welcome to the Job Application System")
        print("1. Apply for a job")
        print("2. View all applicants")
        print("3. Exit")

    def apply_for_job(self):
        name = input("Enter your name: ")
        job_title = input("Enter the job title you are applying for: ")
        resume = input("Enter your resume: ")
        self.applicants.append({"name": name, "job_title": job_title, "resume": resume})
        print("Application submitted successfully!")

    def view_applicants(self):
        if len(self.applicants) == 0:
            print("No applicants yet.")
        else:
            for applicant in self.applicants:
                print("Name: {}, Job Title: {}".format(applicant['name'], applicant['job_title']))
                print("Resume: {}".format(applicant['resume']))

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.apply_for_job()
            elif choice == '2':
                self.view_applicants()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    job_app_system = JobApplicationSystem()
    job_app_system.run()
