import re
import random
import string

def generate_random_string(length):
    r = ''.join(random.choice(string.ascii_letters) for _ in range(length))
    return r
length = 3


print('''
                                    HEY WELCOME TO THIS SECRET LANGUAGE INTERPRETER                                                 ''')
r = input("Do you want to CODE or DECODE: ")

if r == "CODE":
    a = input("Enter the string you want to code: ")
    word = re.findall(r"\w+|\d+|[!+@+#+$+%+^+&+*+()+{}+:+;+<+>+,+.+?+\\+/+~+]",a) 

    # print(word)
    print("Here is Your Encoded String: ")
    for i in word:
        if len(i)>=3:
            r1 = generate_random_string(length)
            r2 = generate_random_string(length)
            q = list(i)
            q1 = q.pop(0)
            r3 = ''.join(q)+q1
            print(f'''{r1+r3+r2}''',end=' ')
        elif len(i)<3:
            r4 = i[::-1]
            print(r4,end=" ")
        elif i in ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|','}', '~']:
            print(i,end="")

elif r == "DECODE":
    a = input("Enter the string you want to decode: ")
    word = re.findall(r"\w+|\d+|[!+@+#+$+%+^+&+*+()+{}+:+;+<+>+,+.+?+\\+/+~+]",a) 
    
    
    for i in word:
        if len(i)>2:
            q1 = list(i)
            for i in range(0,3):
                q1.pop(0)
                q1.pop(-1)
            q2 = q1.pop(-1)
            q3 = q2+''.join(q1)
            print(q3,end=" ")
        elif len(i)==2:
            q4 = i[::-1]
            print(q4,end=" ")
        elif i in ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|','}', '~']:
            print(i,end="")

# a = input("Enter the string you want to decode: ")
# word = re.findall(r"\w+|\d+|[!+@+#+$+%+^+&+*+()+{}+:+;+<+>+,+.+?+\\+/+~+]",a) 
# print(word)



