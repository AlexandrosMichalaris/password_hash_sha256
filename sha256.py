import hashlib #library that contains the sha hash functions
import string
import random

#Generates random string for __salt
def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#Main Class
class safe_manager:
    __salt = random_string_generator()
    __password = hashlib.pbkdf2_hmac('sha256', str(input("Please, wait a few seconds after you insert the password\nPlease enter password: ")).encode('ascii'), str(__salt).encode('ascii'), 3799999)
    #6.3sec

    #Reads the password from the user, it hashes the given password and returns it
    def pass_get(self):
        print("Please, wait a few seconds after you insert the password")
        passholder = hashlib.pbkdf2_hmac('sha256', str(input("Password: ")).encode('ascii'), str(safe_manager.__salt).encode('ascii'), 3799999)
        return passholder

    #It compares the given password with the stored one
    def pass_checker(self):
        if(safe_manager.__password == safe_manager.pass_get(self)):
            print("ACCESS GRANTED")
        else:
            print("CALL ALERT")

    #This function is used for testing purposes
    def print_pass(self):
        print(safe_manager.__password)



al = safe_manager()

al.pass_checker()
al.print_pass()
