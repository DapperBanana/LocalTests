
import time

def apply_for_job():
    print("Welcome to the job application system!")
    time.sleep(1)
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    experience = input("Enter your years of experience: ")
    
    print("\nThank you for applying for the job!")
    print("Here is your application details:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Experience: {experience} years")
    
apply_for_job()
