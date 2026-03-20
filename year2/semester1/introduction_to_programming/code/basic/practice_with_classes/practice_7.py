from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int
    major: str
    gpa: float

    def __eq__(self, other):
        if isinstance(other, Student):
            return (
                self.name == other.name and
                self.age == other.age and
                self.major == other.major and
                self.gpa == other.gpa
            )
        return False

    def display_info(self):
        return f"Student`s name is {self.name}\nHis age is {self.age}\nHis major is {self.major}\nHis GPA is {self.gpa}\n"

    def calculate_grade(self):
        if self.gpa == 5:
            return "Great!"
        elif 4 < self.gpa < 5:
            return "Good!"
        elif 3 < self.gpa < 4:
            return "Satisfactory!"
        else:
            return "Unsatisfactory!"


def compare_of_students(student1, student2):
    if student1 == student2:
        return "They are the same students."
    else:
        return "They are not the same students."


students = [
    Student("Alice", 20, "Computer Science", 3.8),
    Student("Alice", 20, "Computer Science", 3.8),
    Student("Bob", 22, "Engineering", 3.2),
    Student("Charlie", 21, "Mathematics", 4.5),
    Student("David", 23, "Physics", 2.7),
    Student("Eve", 19, "Biology", 3.9),
]

sorted_students = sorted(students, key=lambda student: student.gpa, reverse=True)

if __name__ == "__main__":
    for student in sorted_students:
        print(student.display_info())

    for student in sorted_students:
        print(f"{student.name} - Grade: {student.calculate_grade()}")

    print(f"\nAre Alice and Alice the same student?\n{compare_of_students(students[0], students[1])}\n{students[0] == students[1]}")
    print(f"\nAre Alice and Eve the same student?\n{compare_of_students(students[0], students[5])}\n{students[0] == students[5]}")
