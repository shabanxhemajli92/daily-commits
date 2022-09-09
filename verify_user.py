import re
 
pattern="[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"#uppercase letters([A-Z]) lowercase letters[a-z] numbers[0-9]
user_input=input("input the email you want to search:")
if re.search(pattern,user_input):
  print("valid email")
else:
  print("invalid email")  