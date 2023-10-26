class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the student_list based on CGPA in descending order
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


# Example usage:

# Create a list of student objects
students = [
    Student("Alice", "001", 3.8),
    Student("Bob", "002", 3.6),
    Student("Charlie", "003", 4.0),
    Student("David", "004", 3.9),
]

# Sort the students based on CGPA
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print(
      f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}"
  )
