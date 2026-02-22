#Program that takes marks of 5 subjects as input and calculates total marks, percentage and grade and result

def grade_calculator():
    try:
        marks1=float(input("Enter marks for subject 1: "))
        marks2=float(input("Enter marks for subject 2: "))
        marks3=float(input("Enter marks for subject 3: "))
        marks4=float(input("Enter marks for subject 4: "))
        marks5=float(input("Enter marks for subject 5: "))

        if(marks1<0 or marks1>100 or marks2<0 or marks2>100 or marks3<0 or marks3>100 or marks4<0 or marks4>100 or marks5<0 or marks5>100):
            print("Please enter valid marks between 0 and 100.")
            return

        total_marks = marks1 + marks2 + marks3 + marks4 + marks5 # Calculate total marks
        percentage = (total_marks / 500) * 100 # Calculate percentage

        if percentage >= 90:
            grade = 'A+'
        elif percentage >= 80:
            grade = 'A'
        elif percentage >= 70:  
            grade = 'B'
        elif percentage >= 60:
            grade = 'C'
        elif percentage >= 50:
            grade = 'D'
        else:
            grade = 'F'

        result = "Pass" if percentage >= 50 else "Fail"
        print(f"Marks in subject 1: {marks1}")
        print(f"Marks in subject 2: {marks2}")
        print(f"Marks in subject 3: {marks3}")
        print(f"Marks in subject 4: {marks4}")
        print(f"Marks in subject 5: {marks5}")

        print(f"Total Marks: {total_marks}")

        print(f"Percentage: {percentage:.2f}%")

        print(f"Grade: {grade}")
        
        print(f"Result: {result}")
    except ValueError:
        print("Please enter valid numbers for marks.")

# Function call
grade_calculator()