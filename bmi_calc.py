'''
This function should return 2 values: 
- the BMI category (ex. "underweight") 
- the actual BMI value (ex. 22.86)

Reminders: 
- calculate bmi before returning outputs 
- add error checking for invalid input and unrealistic information
'''


def bmi_check(weight, height):
    if not (isinstance(weight, float) and isinstance(height, float)):
        return "invalid input"
    
    if (weight > 635) and (height > 2.27):
        print("unrealistic information")
    else:
        bmi_calculate =  weight/(height**2)
        if bmi_calculate < 18.5:
            return "underweight by ", bmi_calculate 
        elif bmi_calculate <= 24.9:
            return  "normal by ", bmi_calculate
        elif bmi_calculate <= 29.9:
            return "overweight ", bmi_calculate
        elif bmi_calculate <= 39.9:
            return "obese by ", bmi_calculate
        elif bmi_calculate <= 40:
            return  "extrmely obese by ", bmi_calculate

