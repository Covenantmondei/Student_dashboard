from django.urls import path
from . import views

urlpatterns = [
    path('createaccount/', views.create_account, name='createaccount'),
    path('login/', views.login, name="login"),
    path('verify-email/<str:access_code>/', views.verify_email, name="verifyemail"),
    path('dashboard/<str:reg_no>/', views.dashboard, name="dashboard"),
    path('register-courses/', views.register_courses, name="registercourses"),
    path('update-profile/<str:reg_no>/', views.update_profile, name="updateprofile"), 
    path('check-profile/', views.check_profile, name="checkprofile"),
    path('logout/', views.user_logout, name="logout"),

]