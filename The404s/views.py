from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.tokens import default_token_generator
from .utils import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import random

REGNO = None
ACCESSCODE = None

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
        firstname = request.POST.get('first_name')
        sur_name = request.POST.get('surname')
        email = request.POST.get('email')
        password =request.POST.get('password')
        
        if UserAccount.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('createaccount')

        global reg_no
        global access_code
        reg_no = regno()
        access_code = accesscode()
        
        # create an object to save to the database
        print("Account created success")
        
        user = UserAccount.objects.create(first_name=firstname, surname=sur_name, email=email, reg_no=reg_no, access_code=access_code)
        send_verification_email(email, access_code)
        
        messages.success(request, "Check your email and click the link to verify your email")
        return redirect('login')
        
        
    return render(request, 'createaccount.html', {'messages': messages.get_messages(request)})


def verify_email(request, access_code):
    try:
        user = UserAccount.objects.get(access_code=access_code)
        user.is_verified = True
        print(access_code)
        user.save()
        messages.success(request, "Email verified successfully! Now complete your registration")
        return redirect('login')
    except UserAccount.DoesNotExist:
        print("invalid access code!")
        messages.error(request, 'Invalid Verification Link')
        return redirect('create_account')

def login(request):
    
    if request.method == 'POST':
        reg_num = request.POST['reg_num']
        access_code = request.POST['accesscode']
        
        
        if UserAccount.objects.filter(reg_no=reg_num).exists(): #filter through the database to check if the user exists
            # check if the user is verified
            user = UserAccount.objects.get(reg_no=reg_num)
            if user.is_verified:
                if user.access_code == access_code:
                    messages.success(request, "Login Successful. Continue to you dashboard")
                    return redirect('dashboard', reg_no=user.reg_no)
                try:
                    user = UserAccount.objects.get(reg_no=reg_num)
                except user.DoesNotExist:
                    messages.error(request, "Invalid Student Details")
                    return redirect('login')
                
    return render(request, 'login.html')

# make it necessary for user login to access the dashboard

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
        "profile_image": profile.image.url if profile and profile.image else "/static/default_profile.jpg"
    }
    return render(request, 'dashboard.html', context)

def register_courses(request):
    return render(request, 'registercourses.html')

def update_profile(request, reg_no):
    user = get_object_or_404(UserAccount, reg_no=reg_no)
    student = StudentProfile.objects.filter(student=user).first() # filter through the model
    
    context = {
        "reg.no": user.reg_no,
    }
    
    if request.method == 'POST':
        dob = request.POST.get('dob')
        faculty = request.POST.get('faculty')
        course_of_study = request.POST.get('course_of_study')
        email = request.POST.get('email')
        programme = request.POST.get('programme')
        entry_mode = request.POST.get('entry_mode')
        session = request.POST.get('session')
        entry_year = request.POST.get('entry_year')
        semester = request.POST.get('semester')
        
        if StudentProfile.objects.filter(student=user).exists():
            profile = StudentProfile.objects.get(student=user)
            profile.dob = dob
            profile.faculty = faculty
            profile.course_of_study = course_of_study
            profile.email = email
            profile.programme_type = programme
            profile.entry_mode = entry_mode
            profile.session = session
            profile.entry_year = entry_year
            profile.semester = semester
            
            if 'image' in request.FILES:
                profile.image = request.FILES['image']
            
            profile.save()
            
            messages.success(request, "Profile updated successfully")
            return redirect('dashboard', reg_no=user.reg_no)
    return render(request, 'updateprofile.html', context)

def check_profile(request):
    return render(request, 'checkprofile.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect('login')