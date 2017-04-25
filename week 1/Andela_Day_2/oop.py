#this is the parent class for all students

class Student():
    # these are inherited by every student
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def register(self):
        pass


#science students inherits from the Student class and over rides the register method
class Science_Student(Student):
    def __init__(self, department, class_name, lab_number):
        self.department = department
        self.class_name = class_name
        self.lab_number = lab_number
    def register(self, num):
        self.lab_number = num

#Arts students inherits from the Student class and over rides the register method
class Arts_Student(Student):
    def __init__(self, lecture_room_number):
        self.lecture_room_number = lecture_room_number
    def register(self, lecture_room_number):
        self.lecture_room_number = lecture_room_number



