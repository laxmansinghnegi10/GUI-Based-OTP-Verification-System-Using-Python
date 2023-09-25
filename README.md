# GUI-Based-OTP-Verification-System-Using-Python
This Python project creates a simple OTP (One-Time Password) verification system with a graphical user interface (GUI) using the tkinter library.

Here's an explanation of the code:


1-Import necessary modules:

* random: Used for generating random OTPs.

* smtplib: Used for sending emails.

* ssl: Used for secure email communication.

* tkinter: Used for creating the GUI.

* messagebox: A submodule of tkinter used for displaying message boxes.



2- Define the send_otp(email) function:


* This function generates a 6-digit random OTP and sends it to the provided email address.

* It uses Gmail's SMTP server for sending the email.

* The OTP, email content, and email sending are handled here.


3- Define the verify_otp() function:

* This function is the main function for OTP verification.

* It creates the main GUI window where the user can input their email address.

* When the user clicks the "Send OTP" button, it calls send_otp_and_open_verify_window().


4- Define send_otp_and_open_verify_window():


* This function is called when the user clicks the "Send OTP" button.

* It retrieves the user's email address from the input field, sends the OTP, and opens a new window * for OTP verification.


5- In the send_otp_and_open_verify_window() function:


* A new window (verify_window) is created for OTP verification.

* The user is prompted to enter the OTP they received via email.

* When the user clicks the "Submit" button, it checks if the entered OTP matches the one sent via email.


6- If the OTP matches, a success message is shown in a message box.


* If the OTP is incorrect, an error message is shown in a message box.


7- The main window (window) prompts the user to enter their email address.


* When the user clicks the "Send OTP" button, it triggers the OTP sending process.


8- Finally, the __name__ block ensures that the verify_otp() function is called when the script is run directly.

Overall, this code provides a simple GUI for OTP verification where users can enter their email address, receive an OTP, and verify it through the GUI.




