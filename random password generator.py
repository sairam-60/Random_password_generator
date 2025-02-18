import random
import string 

passlen = int(input("enter length of password :- 10"))
char =string.ascii_letters +string.digits+string.punctuation
password = ""
for i in range(passlen):
    password += random.choice(char)
print("your password is : " ,password )


# import random
# import string 
# passlen = 8
# char =string.ascii_letters +string.digits+string.punctuation
# res ="".join(random.choice(char) for i in range(passlen))
# print(res)
