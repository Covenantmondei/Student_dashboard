from django.urls import path
from . import views

urlpatterns = [
    path('createaccount/', views.create_account, name='createaccount'),
    path('login/', views.login_view, name="login"),
    # path('verify-otp/<str:access_code>/', views.verify_otp, name="verifyemail"),
    path('dashboard/<str:reg_no>/', views.dashboard, name="dashboard"),
    path('register-courses/', views.register_courses, name="registercourses"),
    path('update-profile/<str:reg_no>/', views.update_profile, name="updateprofile"), 
    path('check-profile/', views.check_profile, name="checkprofile"),
    path('get-departments/', views.get_departments, name='get_departments'),
    path('terms_conditions/', views.terms_conditions, name="terms&conditions"),
    path('error/', views.error, name="error"),
    path('success', views.success, name="success"),
    path('logout/', views.user_logout, name="logout"),
    
]