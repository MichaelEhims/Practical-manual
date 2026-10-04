#Exercise 1
num = int(input('Enter a whole number:\n'))
if num > 0 :
    print ('It is a positive number')
elif num < 0 :
    print ('It is a negative number')
else : 
    print ('The number is zero')
    
#Exercise 2
password = input('Enter your desired password: \n')

has_digits = False
has_uppercase = False
has_special = False

for character in password:
     if character.isdigit():
         has_digits = True
     if character.isupper():
         has_uppercase = True
     if not character.isalnum():
         has_special = True
         
if len(password) >= 8 and has_digits and has_uppercase and has_special :
    print ('strong password')
else :
    print ('weak password')
    
#Exercise 3
score = int(input("Enter your score: "))

if score >= 70:
    print("Grade: A")
elif score >= 60:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
elif score >= 45:
    print("Grade: D")
elif score >= 40:
    print("Grade: E")
else:
    print("Grade: F")
