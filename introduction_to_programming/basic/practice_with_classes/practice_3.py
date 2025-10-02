class BaseURL:
    def get_absolute_url(self):
        return f"https://ivashev-education.com/"


class Course(BaseURL):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def get_absolute_url(self):
        base_url = super().get_absolute_url()
        return f"{base_url}/courses/{self.title}"

    def __str__(self):
        return f"Course {self.title}: {self.get_absolute_url()}\nCourse lasts {self.duration} weeks.\n"


class StudentProfile(BaseURL):
    def __init__(self, full_name, email):
        self.full_name = full_name
        self.email = email

    def get_absolute_url(self):
        base_url = super().get_absolute_url()
        return f"{base_url}/profiles/{self.full_name}"

    def __str__(self):
        return f"Student {self.full_name}: {self.get_absolute_url()}\nStudent`s email {self.email}\n"


def add_to_dict(any_dict, key, value):
    any_dict[key] = value


if __name__ == "__main__":
    course_student_dict = {}

    backend = Course("Python-Backend", 30)
    first_student = StudentProfile("Kirill-Pryiomyshev", "viliskrill322@gmail.com")
    add_to_dict(course_student_dict, backend, first_student)

    frontend = Course("Python-Frontend", 25)
    second_student = StudentProfile("Anna-Kovalskaia", "akov99@icloud.com")
    add_to_dict(course_student_dict, frontend, second_student)

    quality_assurance = Course("Quality-Assurance-Engineer", 15)
    third_student = StudentProfile("Anastasia-Kovalskaia", "anaskov21@icloud.com")
    add_to_dict(course_student_dict, quality_assurance, third_student)

    for course, student in course_student_dict.items():
        print(course)
        print(student)
