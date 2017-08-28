from abc import ABCMeta, abstractmethod
import pickle
import os
import pyodbc
from Teacher import *
from Student import *
class IDataInterface:
    __metaclass__ = ABCMeta

    @classmethod
    def version(self): return "1.0"
    @abstractmethod
    def loadTeachers(self): raise NotImplementedError
    @abstractmethod
    def loadStudents(self): raise NotImplementedError
    @abstractmethod
    def loadSchoolClass(self): raise NotImplementedError
    @abstractmethod
    def saveTeachers(self, teachers): raise NotImplementedError
    @abstractmethod
    def saveStudents(self, students): raise NotImplementedError
    @abstractmethod
    def saveSchoolClass(self, schoolClass): raise NotImplementedError


class FileDataProvider(IDataInterface):
    def loadTeachers(self):
        try:
            if os.path.exists("teacher_dict.pickle"):
                with open("teacher_dict.pickle", "rb") as f:
                    teachers = pickle.load(f)
                    print(teachers, " \n")
                    return teachers
        except EOFError:
            print("Sorry you have no Teachers saved")
    def loadStudents(self):
        try:
            if os.path.exists("student_dict.pickle"):
                with open("student_dict.pickle", "rb") as f:
                    students = pickle.load(f)
                    print(students, " \n")
                    return students
        except EOFError:
            print("Sorry you have no Student saved")



class DBDataProvider(IDataInterface):
    def __init__(self):
        self.cnxn = pyodbc.connect("DSN=SchoolSystem")
        self.cursor = self.cnxn.cursor()

    def loadTeachers(self):
        teachers = []
        self.cursor.execute("Select * from teacher")
        rows = self.cursor.fetchall()
        for row in rows:
            teachers.append(Teacher(row.FName+" "+row.LName,
                    row.Age,
                    row.Qualification))
        return teachers

    def loadStudents(self):
        students = []
        self.cursor.execute("Select * from student")
        rows = self.cursor.fetchall()
        for row in rows:
            students.append(Student(row.FullName,
                    row.Age,
                    row.SchoolClass_ID))
        return students