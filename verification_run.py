
class JobApplicationSystem:
    def __init__(self):
        self.applications = []

    def apply_for_job(self, name, desired_position):
        application = {
            'name': name,
            'desired_position': desired_position
        }
        self.applications.append(application)
        print(f"Thank you, {name}! Your application for the position of {desired_position} has been received.")

    def list_applications(self):
        for index, application in enumerate(self.applications):
            print(f"Application {index + 1}:")
            print(f"Name: {application['name']}")
            print(f"Desired Position: {application['desired_position']}")
            print()

def main():
    job_system = JobApplicationSystem()

    while True:
        print("\nJob Application System")
        print("1. Apply for a job")
        print("2. List applications")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            desired_position = input("Enter the desired position: ")
            job_system.apply_for_job(name, desired_position)

        elif choice == "2":
            job_system.list_applications()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
