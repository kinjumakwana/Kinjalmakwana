import random
import string

plen=int(input("Enter pwd len: "))
# if(type(plen)==str):
#     print("enter valid number")
# if plen.isdigit():
#         break
#     else:
#         print("invalid input")
#         continue

# if type(plen)!=int:
#     raise ValueError/TypeError("Enter Valid Integer")

# while type(plen)!=int:
#     print("Input must be a positive integer")
#     plen=int(input("Enter pwd len: "))

s1= string.ascii_lowercase
s2= string.ascii_uppercase
s3= string.digits
s4=string.punctuation
s=[]   
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
print(random.shuffle(s))
# print(s)
# random.sample(s,5)
print("your pwd is: ", end="")
print("".join(s[0:plen]))

