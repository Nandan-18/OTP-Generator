

# Main Program

import validate

print("""
        ---------------------------------------------------
       |                       MENU                        |
        ---------------------------------------------------
       | 1. Generate a 4 digit OTP                         |
       | 2. Generate a Captcha of length as per requirement|
       | 3. Check the validity of an email id              |
       | 4. Exit                                           |
        ---------------------------------------------------
        """)
while True:
    ch = int(input("Enter Choice: "))
    if ch == 1:
        a = validate.generateOTP()
        print(a)
    elif ch == 2:
        size = int(input("Enter the size for the Captcha: "))
        print(validate.rand_captcha(size))
    elif ch == 3:
        email = input("Enter an Email ID: ")
        validate.check(email)
    elif ch == 4:
        break
    else:
        print("INVALID INPUT!")

################################################################################
