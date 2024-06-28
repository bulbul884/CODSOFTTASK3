import random
def genetrate_password(length=14):
    character=string.ascii_letters+string_digits+string_punctuations
    password=('random.choice(characters)for_ in range(length')
    return password
if __name__=="__main__":
     password_length=14
try:


 password_length=int(input("enter desired password length(default is 14)"))
except ValueError:
  
  print("invalid input using default password length")
if password_length<=0:
 
  print("password length should be greater than zero.using default password length")
  password_length=8
  
  generated_password=generate_password(password_length)

print("Generated password:",genetrate_password)



    