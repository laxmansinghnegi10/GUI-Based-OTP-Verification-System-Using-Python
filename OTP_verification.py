import random
import smtplib
import ssl
from tkinter import Tk, Label, Entry, Button, messagebox

def send_otp(email):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "laxmansinghnegi10@gmail.com"
    password = "ztxm bxlv ygfw qmtg"

    otp = ''.join([str(random.randint(0, 9)) for i in range(6)])

    message = f"""\
    Subject: OTP Verification

    Your OTP is {otp}.

    This OTP is valid for 5 minutes. Do not share it with anyone.
    """

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, email, message)

    return otp

def verify_otp():
    def send_otp_and_open_verify_window():
        email = email_entry.get()
        user_otp = send_otp(email)

        def submit_otp():
            entered_otp = otp_entry.get()
            if entered_otp == user_otp:
                messagebox.showinfo("OTP Verification", "OTP verification successful.")
                verify_window.destroy()
            else:
                messagebox.showerror("OTP Verification", "Invalid OTP, please try again.")
        
        verify_window = Tk()
        verify_window.title("Verify OTP")
        verify_window.geometry("500x200")

        Label(verify_window, text="Enter OTP sent to your email:").pack(pady=10)
        otp_entry = Entry(verify_window, show="*")
        otp_entry.pack(pady=5)

        Button(verify_window, text="Submit", command=submit_otp).pack(pady=10)

        verify_window.mainloop()
    
    window = Tk()
    window.title("OTP Verification-Developed By Laxman Singh Negi")
    window.geometry("720x200")

    Label(window, text="Enter your email address:").pack(pady=10)
    email_entry = Entry(window)
    email_entry.pack(pady=5)

    Button(window, text="Send OTP", command=send_otp_and_open_verify_window).pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    verify_otp()
