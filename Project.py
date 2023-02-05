birth_year= input('Birth year: ')
age = 2022 - int(birth_year)
name =  input('What is your name? ')
weight_lbs =  input('What is your weight pounds? ')
weight_kgs = int(weight_lbs) * 0.45
fav_color =  input('What is your favourite color? ')
print( weight_kgs)
msg= f'Hi {name} your age is {age} and your favourite color is {fav_color}'
print(msg)
