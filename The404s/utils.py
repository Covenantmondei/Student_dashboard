# from django.core.mail import send_mail

# # def send_verification_email(email, access_code):
#     # verification_link = f"http://127.0.0.1:8000/the404s/verify-email/{access_code}"
#     # send_mail("Verify your email", f"Click the linkto verify your email: {verification_link}", "covenantmonday863@gmail.com", [email], fail_silently=False)
    
# def generate_otp(email, access_code):
#     """This function will randomly generate a 6-digit OTP"""
#     import random
#     generate_otp = random.randint(100000, 999999)
#     return generate_otp