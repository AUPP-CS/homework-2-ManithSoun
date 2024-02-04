'''
This function should return 2 values: 
- the BMI category (ex. "underweight") 
- the actual BMI value (ex. 22.86)

Reminders: 
- calculate bmi before returning outputs 
- add error checking for invalid input and unrealistic information
'''


def bmi_check(weight, height):
   
        if not isinstance(weight, (int, float)) or not isinstance(height, (int, float)):
                return "invalid input", 1

        if weight <= 635 and height <= 2.72:
                result = round(weight/height ** 2, 2)
                if result < 18.5:
                        return "underweight", result
                elif result >= 18.5 and result <= 24.9:
                        return "normal", result
                elif result >= 25 and result <= 29.9:
                        return "overweight", result
                elif result >= 30 and result <= 34.9:
                        return "obese", result
                else:
                        return "extremely obese", result
        else:
                return "unrealistic information", 2