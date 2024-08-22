
# Define a function for creating a new job application
def create_application():
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    resume = input("Enter a brief summary of your resume: ")
    
    return {
        "name": name,
        "email": email,
        "resume": resume
    }

# Main program loop
applications = []

while True:
    print("Welcome to the job application system")
    print("1. Create a new application")
    print("2. View applications")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        application = create_application()
        applications.append(application)
        print("Application created successfully")
    elif choice == "2":
        print("Current applications:")
        for idx, app in enumerate(applications):
            print(f"Application {idx+1}:")
            print(f"Name: {app['name']}")
            print(f"Email: {app['email']}")
            print(f"Resume: {app['resume']}")
    elif choice == "3":
        print("Exiting program")
        break
    else:
        print("Invalid choice. Please try again.")
