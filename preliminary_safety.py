
def job_application_system():
    print("Welcome to the Job Application System!")
    
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    experience = input("Enter your previous work experience: ")
    
    print("\nThank you for submitting your application!")
    print("Here is a summary of the information you provided:")
    print("Name: " + name)
    print("Age: " + str(age))
    print("Experience: " + experience)
    
    print("\nYour application will now be reviewed. We will contact you if you are selected for an interview.")
    
job_application_system()
