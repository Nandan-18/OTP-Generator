
# Supporting Module:
import math
import random
import re
import string


# function to generate an OTP using random module
def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


# function to generate a Captcha     
def rand_captcha(size):
    generate_pass = ''.join([random.choice(string.ascii_uppercase +
                                           string.ascii_lowercase +
                                           string.digits)
                             for n in range(size)])
    return generate_pass


# function to validate an email ID using regex
regex = '^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$'


def check(email):
    if re.search(regex, email):
        print("Valid Email")
    else:
        print("Invalid Email")
