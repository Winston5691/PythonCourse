# First test
name = input('What is your name? ')
Today_is_Sunday = True

if Today_is_Sunday:
    print(name.upper())
    print(f' today is a Sunday go to church')
else:
    print(name.upper())
    print(f' go to work')
   
#    Second test involving two conditions
has_high_income = True
has_good_credit = True

if has_high_income and  has_good_credit:
    print(f' You are eligible for a loan')
else:
    print(f' You are not eligible for a loan')

#  Third test involving either
is_a_student = False
is_young = True

if is_a_student or  is_young:
    print(f' Ticket granted')
else:
    print(f' Ticket not granted')
    
# Fourth test involving one condition but not the other
has_a_good_credit = False
has_a_criminal_record = True

if has_a_good_credit and not  has_a_criminal_record:
    print(f' You can enroll')
else:
    print(f' You cannot enroll')
    
# Fourth test involving comparison of two conditions
age = int(input('What is your age? '))

if age > 30:
    print(f' You are old')
else:
    print(f' Under age')

    
if len(name) < 3:
    print(f' name has to be more than 3 characters')
elif len(name) > 50:
    print(f' name has to be less than 50 characters')
else: 
    print(f' name is good')
    
weight = int(input('What is your weight? '))
deminations = input('Is your weight in (L) Lbs or (K) Kgs? ')

if deminations.upper() == "L":
    converted=weight*0.4
    print(f' Your weight is {converted}Kgs')
else:
    deminations.upper () == "K"
    converted=weight/0.4
    print(f' Your weight is {converted}Lbs')
    

