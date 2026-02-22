#Personal Bio Card

# Function to print the bio card
def print_bio_card(name, age, course, college, email):
    width = 32  # inner width

    print("╔════════════════════════════════╗")
    print("║        STUDENT BIO CARD        ║")
    print("╠════════════════════════════════╣")

    line = f" Name    : {name}"
    print("║" + line + " " * (width - len(line)) + "║")

    line = f" Age     : {age} years"
    print("║" + line + " " * (width - len(line)) + "║")

    line = f" Course  : {course}"
    print("║" + line + " " * (width - len(line)) + "║")

    line = f" College : {college}"
    print("║" + line + " " * (width - len(line)) + "║")

    line = f" Email   : {email}"
    print("║" + line + " " * (width - len(line)) + "║")

    print("╚════════════════════════════════╝")

#try and except block to handle errors like invalid age input in user input
try:
    student_name = input("Enter your name: ")
    student_age = int(input("Enter your age: "))
    course_name = input("Enter your course: ")
    college_name = input("Enter your college: ")
    email_address = input("Enter your email: ")

    # Function call
    print_bio_card(
        student_name,
        student_age,
        course_name,
        college_name,
        email_address
    )

except ValueError:
    print("Please enter a valid age.")