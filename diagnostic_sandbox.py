
class JobApplicationSystem:
    def __init__(self):
        self.applicants = []

    def apply_for_job(self, name, position, experience):
        applicant_info = {
            'name': name,
            'position': position,
            'experience': experience
        }
        self.applicants.append(applicant_info)
        print(f"Application submitted for {name} for the position of {position}")

    def list_applicants(self):
        for idx, applicant in enumerate(self.applicants):
            print(f"{idx+1}. Name: {applicant['name']}, Position: {applicant['position']}, Experience: {applicant['experience']}")

# Main program
job_app_system = JobApplicationSystem()

while True:
    print("\nMenu:")
    print("1. Apply for a job")
    print("2. List applicants")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter your name: ")
        position = input("Enter the position you are applying for: ")
        experience = input("Enter your years of experience: ")
        job_app_system.apply_for_job(name, position, experience)
    
    elif choice == '2':
        job_app_system.list_applicants()

    elif choice == '3':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
