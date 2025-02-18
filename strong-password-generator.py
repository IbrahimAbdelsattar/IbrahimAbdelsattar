#strong password generator
'''
import string module
store all characters in list(upper\lower case, digits, punctuations)
take number of characters from user
make sure the number of chars is more that or equal 6
shuffle all lists 
calculate 30% and 20% of numbers of characters 
create password 60% letters and 40% digits and puctuations
'''

import string
import random
s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.digits)
s4=list(string.punctuation)

char_name=input("Please enter the number of characters (6 or more): \n")
while True:
    try:
        char_name=int(char_name)
        if char_name <6:
            print("You must enter more than or equal 6.\n")
            char_name=input("Please enter the number of characters (6 or more): \n")
        else:
            break
    except:
        print("Enter numbers only.\n")
        char_name=input("Please enter the number of characters (6 or more): \n")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1=round(char_name*(30/100))
part2=round(char_name*(20/100))

password=[]

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

password=''.join(password[:])

print(password)