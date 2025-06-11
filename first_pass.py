
class JobApplication:
    def __init__(self, name, age, experience):
        self.name = name
        self.age = age
        self.experience = experience

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Experience:", self.experience)

def main():
    print("Welcome to the job application system!")
    print("Please enter your information below:")

    name = input("Name: ")
    age = input("Age: ")
    experience = input("Years of experience: ")

    applicant = JobApplication(name, age, experience)

    print("\nThank you for submitting your application. Here is your information:")
    applicant.display_info()

if __name__ == "__main__":
    main()
