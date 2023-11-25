class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def find_student_info(student_list, name):
    for student in student_list:
        if student.name.lower() == name.lower():
            return student.roll_number, student.cgpa
    return None, None  # Return None if the student is not found

# Collect student data until the user decides to stop
students_list = []
while True:
    name = input("Enter student name (or 'exit' to stop): ")
    if name.lower() == 'exit':
        break  # Exit the loop if the user chooses to stop
    roll_number = input("Enter roll number: ")
    cgpa = float(input("Enter CGPA: "))
    student = Student(name, roll_number, cgpa)
    students_list.append(student)

# Ask for a student name to search
while True:
    search_name = input("Enter a student name to get roll number and CGPA (or 'exit' to stop): ")
    if search_name.lower() == 'exit':
        break  # Exit the loop if the user chooses to stop
    roll_number, cgpa = find_student_info(students_list, search_name)
    
    if roll_number is not None:
        print(f"Student found - Roll Number: {roll_number}, CGPA: {cgpa}")
    else:
        print("Student not found.")