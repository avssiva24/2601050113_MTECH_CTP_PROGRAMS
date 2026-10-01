from dataclasses import dataclass


class Student:
    def __init__(self, name: str, roll_no: int):
        self.name = name
        self.roll_no = roll_no


@dataclass
class StudentData:
    name: str
    roll_no: int


student1 = Student("Ravi", 101)
student2 = StudentData("Ravi", 101)

print("Traditional class:")
print("Name:", student1.name)
print("Roll No:", student1.roll_no)

print("\nDataclass:")
print(student2)
