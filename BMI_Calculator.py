def calculate_bmi(weight, height):

    BMI = 703*(weight/height**2)

    if BMI <= 18.5:
        print('You are underweight... eat more')
    
    elif BMI 18.5 > number <= 25:
        print('your basic, but normal')
    elif BMI 25 > number <=29.9:
        print('You heavy fam')
    else:
        print('You fat Bruv') 


weight = input('What is your weight in pounds?')
weight = float(weight)

height = input("How tall are you in inches?")
height = float(height)
calculate_bmi(weight, height)