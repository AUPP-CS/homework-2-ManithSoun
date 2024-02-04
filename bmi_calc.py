'''
This function should return 2 values: 
- the BMI category (ex. "underweight") 
- the actual BMI value (ex. 22.86)

Reminders: 
- calculate bmi before returning outputs 
- add error checking for invalid input and unrealistic information
'''


def bmi_check(weight, height):
    try:
        # Attempt to convert weight and height to float
        weight = float(weight)
        height = float(height)

        if (weight < 636) and (height < 2.27):
            bmi_score = round(weight / (height ** 2), 2)

            if bmi_score < 18.5:
                return "underweight", bmi_score 
            elif 18.5 <= bmi_score <= 24.9:
                return "normal", bmi_score
            elif 25 <= bmi_score <= 29.9:
                return "overweight", bmi_score
            elif 30 <= bmi_score <= 39.9:
                return "obese", bmi_score
            elif bmi_score >= 40:
                return "extremely obese", bmi_score
        else:
            return "unrealistic information"

    except ValueError:
        # Handle the case where conversion to float fails
        return "invalid input"


