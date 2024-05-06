from django.contrib import admin
from .models import Student, Teacher, Course, Address
from django.http import HttpResponse
import csv

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    actions = ["export_to_csv"]

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="students.csv"'
        writer = csv.writer(response)
        writer.writerow(["RUT", "Name", "Last Name", "Birth Date", "Active", "Created At", "Created By"])
        for student in queryset:
            writer.writerow(
                [
                    student.rut,
                    student.name,
                    student.last_name,
                    student.birth_date,
                    student.active,
                    student.created_at,
                    student.created_by,
                ]
            )
        return response

    export_to_csv.short_description = "Export selected student(s) to CSV"
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    exclude = ('created_at', 'updated_at',)
    actions = ["export_to_csv"]

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="teachers.csv"'
        writer = csv.writer(response)
        writer.writerow(["RUT", "Name", "Last Name", "Active", "Created At", "Created By"])
        for teacher in queryset:
            writer.writerow(
                [
                    teacher.rut,
                    teacher.name,
                    teacher.last_name,
                    teacher.active,
                    teacher.created_at,
                    teacher.created_by,
                ]
            )
        return response

    export_to_csv.short_description = "Export selected teacher(s) to CSV"

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    actions = ["export_to_csv"]

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="courses.csv"'
        writer = csv.writer(response)
        writer.writerow(["Code", "Name", "Version", "Teacher"])
        for course in queryset:
            writer.writerow(
                [
                    course.code,
                    course.name,
                    course.version,
                    course.teacher.name if course.teacher else "N/A",
                ]
            )
        return response

    export_to_csv.short_description = "Export selected course(s) to CSV"

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    actions = ["export_to_csv"]

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="addresses.csv"'
        writer = csv.writer(response)
        writer.writerow(["ID", "Street", "Number", "Apartment", "District", "City", "Region", "Student RUT"])
        for address in queryset:
            writer.writerow(
                [
                    address.id,
                    address.street,
                    address.number,
                    address.apt,
                    address.district,
                    address.city,
                    address.region,
                    address.student.rut,
                ]
            )
        return response

    export_to_csv.short_description = "Export selected address(es) to CSV"