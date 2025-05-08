from django.contrib import admin
from .models import *

admin.site.site_header = "The404 Admin"
admin.site.site_title = "The404 Admin Portal"
admin.site.index_title = "Welcome to The404 Admin Portal"

# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'email', 'reg_no', 'access_code', 'is_verified')
    search_fields = ('first_name', 'surname', 'reg_no', 'email')
    list_filter = ('is_verified',)
    ordering = ('-id',)

admin.site.register(UserAccount)

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('student', 'other_name', 'phone_number', 'dob', 'guardian', 'guardian_contact', 'address', 'next_of_kin', 'n_o_k_contact')
    search_fields = ('student__first_name', 'student__surname', 'phone_number')
    list_filter = ('student__is_verified',)
    ordering = ('-id',)
admin.site.register(StudentProfile)

class UserFacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_name', 'description')
    search_fields = ('faculty_name',)
    ordering = ('-id',)
admin.site.register(UserFaculty)

class UserDeptAdmin(admin.ModelAdmin):
    list_display = ('dept_name', 'description', 'unique_key')
    search_fields = ('dept_name',)
    ordering = ('-id',)
admin.site.register(UserDept)


class UserCoursesAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_code', 'unique_key')
    search_fields = ('course_name',)
    ordering = ('-id',)
admin.site.register(UserCourses)


class StudentSchoolDetailsAdmin(admin.ModelAdmin):
    list_display = ('student', 'bio', 'faculty', 'department', 'programme_type', 'mode_of_study')
    search_fields = ('student__first_name', 'student__surname')
    list_filter = ('faculty', 'department')
    ordering = ('-id',)
admin.site.register(StudentSchoolDetails)

class LecturerAdmin(admin.ModelAdmin):
    list_display = ('lecturer_name', 'lecturer_email', 'lecturer_phone_number', 'lecturer_department')
    search_fields = ('lecturer_name', 'lecturer_email')
    ordering = ('-id',)
admin.site.register(Lecturer)

class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_code', 'course_lecturer', 'course_department')
    search_fields = ('course_name', 'course_code')
    ordering = ('-id',)
admin.site.register(CourseEnrollment)