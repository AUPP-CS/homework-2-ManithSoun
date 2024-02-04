'''
This function should return 2 values: 
- the BMI category (ex. "underweight") 
- the actual BMI value (ex. 22.86)

Reminders: 
- calculate bmi before returning outputs 
- add error checking for invalid input and unrealistic information
'''


def bmi_check(weight, height):
    if isinstance(weight, (int, float)) and isinstance(height, (int, float)):
        if height < 2.72 and weight < 636:
            bmi_score = weight / (height ** 2)
            bmi = round(bmi_score, 2)
            if bmi < 18.5:
                return ("underweight", bmi)
            elif bmi >= 18.5 and bmi <= 24.9:
                return ("normal", bmi)
            elif bmi >= 25 and bmi <= 29.9:
                return ("overweight", bmi)
            elif bmi >= 30 and bmi <= 39.9:
                return ("obese", bmi)
            elif bmi > 40:
                return ("extremely obese", bmi)
        else:
            return ("unrealistic information", 2)
    else:
        return ("invalid input", 1) 
