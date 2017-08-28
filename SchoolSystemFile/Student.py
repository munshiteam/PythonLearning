class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return ("{0} is a(n) {1} year old student.".format(self.name, self.age))
