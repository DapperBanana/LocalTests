
def get_personal_info():
    print("Please enter your personal information:")
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    return name, age, email

def get_education_info():
    print("Please enter your education information:")
    degree = input("Degree: ")
    school = input("School: ")
    graduation_year = input("Graduation Year: ")
    return degree, school, graduation_year

def get_experience_info():
    print("Please enter your work experience information:")
    company = input("Company: ")
    position = input("Position: ")
    start_date = input("Start Date: ")
    end_date = input("End Date: ")
    return company, position, start_date, end_date

def submit_application(name, age, email, degree, school, graduation_year, company, position, start_date, end_date):
    print("Thank you for submitting your application!")
    print("Name:", name)
    print("Age:", age)
    print("Email:", email)
    print("Education: ", degree, "from", school, "Graduation year:", graduation_year)
    print("Work Experience: ", position, "at", company, "from", start_date, "to", end_date)

def main():
    print("Welcome to the job application system!")
    
    name, age, email = get_personal_info()
    
    degree, school, graduation_year = get_education_info()
    
    company, position, start_date, end_date = get_experience_info()
    
    submit_application(name, age, email, degree, school, graduation_year, company, position, start_date, end_date)

if __name__ == "__main__":
    main()
