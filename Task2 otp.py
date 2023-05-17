
import random
import smtplib

def generate_otp():
    return random.randint(1000, 9999)

def send_otp(email, otp):
    smtp_server = "smtp.gmail/com"
    smtp_port = 587  
    sender_email = "devashiskapte6@gmail.com"   
    message = f"Subject: OTP Verification\n\nYour OTP: {otp}"

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message)
        print("OTP sent successfully!")
    except smtplib.SMTPException as e:
        print("Failed to send OTP.")
        print(e)

def verify_otp(entered_otp, expected_otp):
    return entered_otp == expected_otp


email = "bajiiisan69@gmail.com"  
otp = generate_otp()
send_otp(email, otp)

entered_otp = int(input("Enter the OTP you received: "))
if verify_otp(entered_otp, otp):
    print("OTP verification successful!")
else:
    print("OTP verification failed!")











