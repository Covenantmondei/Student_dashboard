from django.db import models

# Create your models here
class UserAccount(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255)
    email = models.EmailField(unique=True) # to store user email
    reg_no = models.CharField(max_length=25)
    access_code = models.CharField(max_length=10, unique=True) # to store randomly generated accesscode
    is_verified = models.BooleanField(default=False) #to check if email is verified
    
    def __str__(self):
        return f"{self.first_name}, {self.surname} -- {self.reg_no}"
    
class StudentProfile(models.Model):
    other_name = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=11, unique=True)
    dob = models.DateField()
    guardian = models.CharField(max_length=255, null=True, blank=True)
    guardian_contact = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True)
    next_of_kin = models.CharField(max_length=255)
    n_o_k_contact = models.CharField(max_length=15, null=True)
    passport = models.ImageField(upload_to="passport/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    student = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name="studentdetails")
    
    def __str__(self):
        return self.student

class UserFaculty(models.Model):
    faculty_name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.faculty_name
    
class UserDept(models.Model):
    dept_name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    unique_key = models.ForeignKey(UserFaculty, on_delete=models.CASCADE, related_name="department", null=True, blank=True)
    
    def __str__(self):
        return self.dept_name
    
class UserCourses(models.Model):
    course_name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=10)
    unique_key = models.ForeignKey(UserFaculty, on_delete=models.CASCADE, related_name="courses", null=True, blank=True)
    
    def __str__(self):
        return f"{self.course_name} ({self.course_code})"
    
class StudentSchoolDetails(models.Model):
    student = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    faculty = models.ForeignKey(UserFaculty, on_delete=models.CASCADE, related_name="student_faculty", null=True, blank=True)
    department = models.ForeignKey(UserDept, on_delete=models.CASCADE, related_name="student_department", null=True, blank=True)
    programme_type = models.CharField(max_length=255, choices=[('Undergraduate', 'Undergraduate'), ('Postgraduate', 'Postgraduate')], null=True, blank=True)
    mode_of_study = models.CharField(max_length=255, choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time')], null=True, blank=True)
    entry_mode = models.CharField(max_length=255, choices=[('UTME', 'UTME'), ('Direct Entry', 'Direct Entry')], null=True, blank=True)
    semester = models.CharField(max_length=255, choices=[('First Semester', 'First Semester'), ('Second Semester', 'Second Semester')], null=True, blank=True)
    session = models.CharField(max_length=255, choices=[('2020/2021', '2020/2021'), ('2021/2022', '2021/2022')], null=True, blank=True)
    entry_year = models.CharField(max_length=4, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student} \n{self.faculty} \n{self.department}"
    
class Lecturer(models.Model):
    name = models.CharField(max_length=255)
    student = models.ManyToManyField(UserAccount)
    
    def __str__(self):
        return self.name
    
class CourseEnrollment(models.Model):
    student = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="students", null=True, blank=True)
    course = models.ManyToManyField(UserCourses, related_name="courses", null=True, blank=True)
    enrolled_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student}, {self.course}"