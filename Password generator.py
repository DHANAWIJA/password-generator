#PASSWORD GENERATOR

import string
import random

password_count=int(input("enter no of pwd wish to generated:"))

def generate_password(length):
   char_lower=string.ascii_lowercase
   char_upper=string.ascii_uppercase
   numeric=string.digits
   spacial_char=string.punctuation

characters=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
print(characters)

while True:
    length=int(input("enter length of password between 8 and 15:"))

    if length<8:
        print("enter length greater than or equal to 8")
        break
    if length>15:
        print("enter length less than or equal to 15")
        break

    password="".join(random.choice(characters)for x in range(length))
    print(password)

    print("random password generated:",password)
    break




















