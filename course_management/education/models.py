from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Student(models.Model):
    rut = models.CharField(max_length=9, primary_key=True, verbose_name=_("RUT"), null=False, blank=False)
    name = models.CharField(max_length=50, verbose_name=_("Name"), null=False, blank=False)
    last_name = models.CharField(max_length=50, verbose_name=_("Last Name"), null=False, blank=False)
    birth_date = models.DateField(verbose_name=_("Birth Date"), null=False, blank=False)
    active = models.BooleanField(default=False, verbose_name=_("Active"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    created_by = models.CharField(max_length=50, verbose_name=_("Created By"), null=False, blank=False)

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")
        
class Teacher(models.Model):
    rut = models.CharField(max_length=9, primary_key=True, verbose_name=_("RUT"), null=False, blank=False)
    name = models.CharField(max_length=50, verbose_name=_("Name"), null=False, blank=False)
    last_name = models.CharField(max_length=50, verbose_name=_("Last Name"), null=False, blank=False)
    active = models.BooleanField(default=False, verbose_name=_("Active"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    created_by = models.CharField(max_length=50, verbose_name=_("Created By"), null=False, blank=False)

    class Meta:
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")

class Course(models.Model):
    code = models.CharField(max_length=10, primary_key=True, verbose_name=_("Code"), null=False, blank=False, unique=True)
    name = models.CharField(max_length=50, verbose_name=_("Name"), null=False, blank=False)
    version = models.IntegerField(verbose_name=_("Version"))
    teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Teacher"), unique=True)
    students = models.ManyToManyField(Student, related_name='courses', verbose_name=_("Students"))

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")
        
class Address(models.Model):
    id = models.AutoField(primary_key=True, verbose_name=_("ID"))
    street = models.CharField(max_length=50, verbose_name=_("Street"), null=False, blank=False)
    number = models.CharField(max_length=10, verbose_name=_("Number"), null=False, blank=False)
    apt = models.CharField(max_length=10, blank=True, verbose_name=_("Apartment"))
    district = models.CharField(max_length=50, verbose_name=_("District"), null=False, blank=False)
    city = models.CharField(max_length=50, verbose_name=_("City"), null=False, blank=False)
    region = models.CharField(max_length=50, verbose_name=_("Region"), null=False, blank=False)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, unique=True, verbose_name=_("Student"), null=False, blank=False)

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")