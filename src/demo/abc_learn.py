from abc import ABC, abstractmethod

class Course(ABC):
    @abstractmethod
    def enroll(self, student: str) -> None:
        print(f"{student} enrolled in Course")
        
class MathCourse(Course):
    def enroll(self, student: str):
        print(f"{student} enrolled in MathCourse")
    
class ScienceCourse(Course):
    def enroll(self, student: str):
        print(f"{student} enrolled in ScienceCourse")

courses: list[str] = [MathCourse(), ScienceCourse()]
for course in courses:
    course.enroll("John")