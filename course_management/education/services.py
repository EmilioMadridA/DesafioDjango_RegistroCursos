from .models import Student, Teacher, Course, Address
from django.core.exceptions import ObjectDoesNotExist

def create_student(rut, name, last_name, birth_date, created_by):
    student = Student(
        rut=rut,
        name=name,
        last_name=last_name,
        birth_date=birth_date,
        created_by=created_by,
    )
    student.save()
    return student

def create_teacher(rut, name, last_name, created_by):
    teacher = Teacher(
        rut=rut,
        name=name,
        last_name=last_name,
        created_by=created_by
    )
    teacher.save()
    return teacher

def create_course(code, name, version):
    course = Course(
        code=code,
        name=name,
        version=version
    )
    course.save()
    return course

def create_address(street, number, apt, district, city, region, student):
    address= Address(
        street=street,
        number=number,
        apt=apt,
        district=district,
        city=city,
        region=region,
        student=student
    )
    address.save()
    return address

def get_student(rut):
    return Student.objects.get(rut=rut)

def get_teacher(rut):
    return Teacher.objects.get(rut=rut)

def get_course(code):
    return Course.objects.get(code=code)

def add_teacher_to_course(teacher, course):
    try:
        teacher = Teacher.objects.get(rut=teacher.rut)
        course = Course.objects.get(code=course.code)
    except Teacher.DoesNotExist:
        print("No se ha encontrado el profesor")
        return
    except Course.DoesNotExist:
        print("No se ha encontrado el curso")
        return
        
    course.teacher = teacher
    course.save()

def add_courses_to_student(student, courses):
    try:
        student = Student.objects.get(rut=student.rut)
        for course in courses:
            Course.objects.get(code=course.code)
        student.courses.set(courses)
    except Student.DoesNotExist:
        print("No se ha encontrado el estudiante")
    except Course.DoesNotExist:
        print("No se ha encontrado el curso")

def print_student_courses(student):
    try:
        student = Student.objects.get(rut=student.rut)
    except Student.DoesNotExist:
        print("No se ha encontrado el estudiante")
        return
    courses = student.courses.all()
    if courses:
        for course in courses:
            print(f"Course: {course.name}, Code: {course.code}")
    else:
        print("El estudiante no esta inscrito en ningún curso")