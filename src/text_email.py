# Sending text-only emails
message = EmailMessage()
message["subject"] = "Test email!"
message["from"] = "<test@testmail.com>"
message["to"] = "midhunhk+test@gmail.com>"
message.set_content("Hello Universe!")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('<your_email@gmail.com>', '<generated_app_password>')
    smtp.send_message(message)
    print("Email sent!")