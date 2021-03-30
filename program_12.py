# Program 12:

"""
- Generate OTP of 4 digits
- Generate a Captcha of length as per requirement
- Check the validity of an email id
"""

# Main Program:

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

# OUTPUT#
'''
        ---------------------------------------------------
       |                       MENU                        |
        ---------------------------------------------------
       | 1. Generate a 4 digit OTP                         |
       | 2. Generate a Captcha of length as per requirement|
       | 3. Check the validity of an email id              |
       | 4. Exit                                           |
        ---------------------------------------------------
        
Enter Choice: 1
4400
Enter Choice: 2
Enter the size for the Captcha: 10
P3xlNsOiqE
Enter Choice: 3
Enter an Email ID: nandan@gmail.com
Valid Email
Enter Choice: 3
Enter an Email ID: nandan.com
Invalid Email
Enter Choice: 4
>>> '''
