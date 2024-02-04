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
    
    if (weight > 635) or (height > 2.27):
        print("unrealistic information")
    else:
        bmi_calculate =  (weight/(height**2), 2)

        if bmi_calculate < 18.5:
            return "underweight", bmi_calculate 
        elif 18.5 <= bmi_calculate <= 24.9:
            return  "normal", bmi_calculate
        elif 25 <= bmi_calculate <= 29.9:
            return "overweight", bmi_calculate
        elif 30 <= bmi_calculate < 34.9:
            return "obese", bmi_calculate
        elif bmi_calculate >= 35:
            return  "extrmely obese", bmi_calculate
