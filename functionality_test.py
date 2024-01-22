
class JobApplication:
    def __init__(self, name, age, qualifications, experience):
        self.name = name
        self.age = age
        self.qualifications = qualifications
        self.experience = experience
    
    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nQualifications: {self.qualifications}\nExperience: {self.experience}\n'

class JobApplicationSystem:
    def __init__(self):
        self.applications = []
    
    def add_application(self, application):
        self.applications.append(application)
    
    def view_applications(self):
        for application in self.applications:
            print(application)

    def search_applications(self, qualification):
        found_applications = []
        for application in self.applications:
            if qualification.lower() in application.qualifications.lower():
                found_applications.append(application)
        
        if found_applications:
            for application in found_applications:
                print(application)
        else:
            print("No matching applications found.")

# Sample usage of the program
system = JobApplicationSystem()

# Create job applications
application1 = JobApplication("John Doe", 25, "Bachelor's degree in Computer Science", "3 years of software development experience")
application2 = JobApplication("Jane Smith", 30, "Master's degree in Business Administration", "5 years of marketing experience")
application3 = JobApplication("Bob Johnson", 22, "High school diploma", "1 year of customer service experience")

# Add job applications to the system
system.add_application(application1)
system.add_application(application2)
system.add_application(application3)

# View all applications
system.view_applications()

# Search applications by qualification
print("\nSearching applications with 'degree' qualification:")
system.search_applications("degree")

print("\nSearching applications with 'marketing' qualification:")
system.search_applications("marketing")
