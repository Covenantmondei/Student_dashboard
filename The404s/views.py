from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.tokens import default_token_generator
from .utils import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import random
from django.http import JsonResponse
import time
from decouple import config
from django.templatetags.static import static

REGNO = None
ACCESSCODE = None

# def get_departments(request):
#     faculty_name = request.GET.get('faculty')
#     try:
#         faculty = UserFaculty.objects.get(faculty_name=faculty_name)
#         departments = faculty.departments.all()
#         department_list = [dept.department_name for dept in departments]
#         return JsonResponse({'departments': department_list})
#     except UserFaculty.DoesNotExist:
#         return JsonResponse({'departments': []})

def regno():
    """This function will randomly generate"""
    global REGNO
    no = "0123456789"
    return "".join(random.choices(no, k=10))
    # return student_reg_no

def accesscode():
    global ACCESSCODE
    letters = "ABC0123456789"
    return "".join(random.choices(letters, k=5))

# Create your views here.
def create_account(request):
    user = UserAccount.objects.filter() # filter through the database
    print(request.POST)
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        sur_name = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if UserAccount.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('createaccount')

        # generate the reg_no and access_code
        reg_no = regno()
        access_code = accesscode()
        
        # create an object to save to the database
        print("Account created success")
        
        user = UserAccount.objects.create(first_name=firstname, surname=sur_name, email=email, reg_no=reg_no, access_code=access_code)
        # request.session['user_email'] = email
        # generate_otp(email, access_code)
        # send_verification_email(email, access_code)
        
        
        # messages.success(request, "Enter OTP sent to your email")
        user.save()
        print("Redirecting to dashboard with reg_no:", reg_no)
        return redirect('dashboard', reg_no=reg_no)
    
        
    return render(request, 'createaccount.html')


# def verify_email(request, access_code):
#     try:
#         user = UserAccount.objects.get(access_code=access_code)
#         user.is_verified = True
#         print(access_code)
#         user.save()
#         messages.success(request, "Email verified successfully! Now complete your registration")
#         return redirect('login')
#     except UserAccount.DoesNotExist:
#         print("invalid access code!")
#         messages.error(request, 'Invali d Verification Link')
#         return redirect('create_account')
    
# def send_otp(request):
#     email = request.session.get('user_email')
#     otp = generate_otp()
#     request.session['otp'] = otp
#     request.session['otp_expiry'] = str(time.time() + 300)  # Set session expiry to 5 minutes
    
#     send_mail(
#         subject='Your OTP Code',
#         message=f'Your OTP code is: {otp}',
#         from_email=config('EMAIL_HOST_USER'),
#         recipient_list=[email],
#         fail_silently=False,
#     )
    
# def verify_otp(request):
#     if request.method == 'POST':
#         entered_otp = request.POST.get('otp')
#         otp = request.session.get('otp')
#         otp_expiry = request.session.get('otp_expiry')
        
#         if not otp or not otp_expiry:
#             messages.error(request, "No OTP entered. Please request a new OTP.")
#             return redirect('createaccount')
        
#         if time.time() > float(otp_expiry):
#             messages.error(request, "OTP has expired. Please request a new one.")
#             return redirect('createaccount')
        
#         otp_expiry = float(otp_expiry)
        
#         if entered_otp == otp:
#             user = UserAccount.objects.get(email=request.session['user_email'])
#             user.is_verified = True
#             user.save()
#             messages.success(request, "Email verified successfully! Now complete your registration")
#             return redirect('dashboard')
#         else:
#             messages.error(request, "Invalid OTP. Please try again.")
    
#     return render(request, 'otp_page.html')

def login_view(request):
    
    if request.method == 'POST':
        reg_num = request.POST['reg_num']
        access_code = request.POST['accesscode']
        
        
        if UserAccount.objects.filter(reg_no=reg_num).exists(): #filter through the database to check if the user exists
            # check if the user is verified
            try:
                user = UserAccount.objects.get(reg_no=reg_num)
                if user.access_code == access_code:
                    messages.success(request, "Login Successful. Continue to you dashboard")
                    return redirect('dashboard', reg_no=user.reg_no)
                
            except UserAccount.DoesNotExist:
                messages.error(request, "Invalid Student Details")
                return redirect('login')
                
    return render(request, 'login.html')

# make it necessary for user login to access the dashboard

def get_departments(request):
    user_faculty = request.GET.get('faculty')
    dept = UserDept.objects.filter(unique_key__faculty_name=user_faculty).values_list('dept_name', flat=True)
    return JsonResponse({'departments': list(dept)})


# @login_required(login_url='login')
def dashboard(request, reg_no):
    user = get_object_or_404(UserAccount, reg_no=reg_no)
    student = StudentSchoolDetails.objects.filter(student=user).first() # filter through the model
    profile = StudentProfile.objects.filter(student=user).first() # filter through the model
    # user = UserAccount.objects.filter() # filter through the database
    
    context = {
        "full_name": f"{user.first_name} {user.surname}",
        "reg_no": user.reg_no,
        "date_of_birth": profile.dob if profile else None,
        "faculty": student.faculty if profile else None,
        "course_of_study": student.department if profile else None,
        "Email": user.email if profile else None,
        "programme": student.programme_type if profile else None,
        "entry_mode": student.entry_mode if profile else None,
        "session": student.session if profile else None,
        "entry_year": student.entry_year if profile else None,
        "semester": student.semester if profile else None,
        # "profile_image": profile.image.url if profile and profile.image else None

    }
    return render(request, 'dashboard.html', context)

def register_courses(request):
    return render(request, 'registercourses.html')

def update_profile(request, reg_no):
    user = get_object_or_404(UserAccount, reg_no=reg_no)
    student = StudentProfile.objects.filter(student=user).first() # filter through the model
    all_faculty = UserFaculty.objects.all()
    all_departments = UserDept.objects.all()
    
    
    if request.method == 'POST':
        dob = request.POST.get('dob')
        faculty_name = request.POST.get('faculty')
        course_of_study = request.POST.get('course_of_study')
        email = request.POST.get('email')
        programme = request.POST.get('programme')
        entry_mode = request.POST.get('entry_mode')
        session = request.POST.get('session')
        entry_year = request.POST.get('entry_year')
        semester = request.POST.get('semester')
       
        
        if StudentSchoolDetails.objects.filter(student=user).exists():
            student_profile = StudentProfile.objects.get(student=user)
            student_details = StudentSchoolDetails.objects.get(student=user)
            student_profile.dob = dob
            student_details.faculty = faculty_name
            student_details.department = course_of_study
            student_details.programme_type = programme
            student_details.entry_mode = entry_mode
            student_details.session = session
            student_details.entry_year = entry_year
            student_details.semester = semester
            
            if 'image' in request.FILES:
                student_profile.passport = request.FILES['image']
            student_details.objects.update_or_create(student=user, defaults={
                'faculty': faculty_name,
                'department': course_of_study,
                'programme_type': programme,
                'entry_mode': entry_mode,
                'session': session,
                'entry_year': entry_year,
                'semester': semester
            })
            
            student_profile.objects.update_or_create(student=user, defaults={
                'dob': dob,
                'passport': student_profile.passport
            })
            student_details.save()
            student_profile.save()
            print("POST DATA:", request.POST)

            
            messages.success(request, "Profile updated successfully")
            return redirect('dashboard', reg_no=user.reg_no)
            
    context = {
    "reg_no": user.reg_no,
    "name": f"{user.first_name} {user.surname}",
    "email": f"{user.email}",
    "faculties": all_faculty,
    "departments": all_departments,
    "image": student.passport.url if student and student.passport else "/static/default_profile.jpg",
    }
    return render(request, 'updateprofile.html', context)

def check_profile(request):
    return render(request, 'checkprofile.html')

def terms_conditions(request):
    return render(request, 'terms_conditions.html')

def error(request):
    return render(request, 'error.html')

def success(request):
    return render(request, 'success.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect('login')