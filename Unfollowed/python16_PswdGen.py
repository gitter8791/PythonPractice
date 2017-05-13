#Function generates random password from ASCII pool
import random
import string

def gen8pdw():
	passwd_what = str(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(8)))
	return (passwd_what)

print ('Your password is: ', gen8pdw())


'''
import string
import random

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input('How many characters in your password?'))))
'''