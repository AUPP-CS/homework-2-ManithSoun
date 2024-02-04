from bmi_calc import bmi_check

# Call the bmi_calc function and add in a user interface for the bmi calculator (ex. welcome message, instructions, etc.)

# Add your code here
while True:
    name = input("What is your name? : ")
    weight = float(input("How much do you weight? (in kg): "))
    height = float(input("How tall are you? (in m): "))


    print(f"Hello {name} You are {bmi_check(weight, height)} BMI")

    con = input("Do you want to continue? Y/N: ")
    if con.lower() == "n":
        print("Thank you for using our app")
        print("Hope you have a great day, dear!! <3")
        exit()
    else:
        continue
    