
jobs = {
    "Software Developer": ["Python", "Java", "C++", "Web Development"],
    "Data Scientist": ["Python", "R", "Machine Learning", "Statistics"],
    "Marketing Specialist": ["Social Media", "SEO", "Content Creation"]
}

def apply_for_job(job):
    print(f"Applying for {job} position.")
    skills_required = jobs[job]
    
    applicant_skills = input("Enter your skills separated by commas: ").split(", ")
    
    if all(skill in applicant_skills for skill in skills_required):
        print("Congratulations! You meet the requirements for this job.")
    else:
        print("Sorry, you do not have the required skills for this job.")

def main():
    print("Welcome to the job application system.")
    
    while True:
        print("\nAvailable jobs:")
        for job in jobs:
            print(job)
        
        selected_job = input("\nEnter the job you'd like to apply for (or type 'quit' to exit): ")
        
        if selected_job.lower() == "quit":
            break
        
        if selected_job in jobs:
            apply_for_job(selected_job)
        else:
            print("Invalid job position. Please try again.")

if __name__ == "__main__":
    main()
