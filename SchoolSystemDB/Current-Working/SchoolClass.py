class SchoolClass():
    def __init__(self, teacher, grade, students):
        self.teacher = teacher
        self.grade = grade
        self.students = students

    def __repr__(self):
        return ("This is a Grade {0} class with {1} students, Taught by {2}".format(self.grade, self.students, self.teacher))
