from bmi_calc import bmi_check

# Call the bmi_calc function and add in a user interface for the bmi calculator (ex. welcome message, instructions, etc.)

# Add your code here

print("""

         .----------------.  .----------------.  .----------------. 
        | .--------------. || .--------------. || .--------------. |
        | |   ______     | || | ____    ____ | || |     _____    | |
        | |  |_   _ \    | || ||_   \  /   _|| || |    |_   _|   | |
        | |    | |_) |   | || |  |   \/   |  | || |      | |     | |
        | |    |  __'.   | || |  | |\  /| |  | || |      | |     | |
        | |   _| |__) |  | || | _| |_\/_| |_ | || |     _| |_    | |
        | |  |_______/   | || ||_____||_____|| || |    |_____|   | |
        | |              | || |              | || |              | |
        | '--------------' || '--------------' || '--------------' |
        '----------------'  '----------------'  '----------------'      
      """)
 
print("""
          ┓ ┏  ┓          ┏┳┓    ┳┓┳┳┓┳  ┏┓  ┓   ┓   •            
          ┃┃┃┏┓┃┏┏┓┏┳┓┏┓   ┃ ┏┓  ┣┫┃┃┃┃  ┃ ┏┓┃┏┓┏┃┏┓╋┓┏┓┏┓  ┏┓┏┓┏┓
          ┗┻┛┗ ┗┗┗┛┛┗┗┗    ┻ ┗┛  ┻┛┛ ┗┻  ┗┛┗┻┗┗┗┻┗┗┻┗┗┗┛┛┗  ┗┻┣┛┣┛
                                                              ┛ ┛ 
                      ~~ WHERE HEALTH IS MATTER ~~
      """)


while True:
    name = input("      1️⃣  What is your name? : ")
    weight = float(input("      2️⃣  How much do you weight? (in kg): "))
    height = float(input("      3️⃣  How tall are you? (in m): "))
    result = bmi_check(weight, height)
    upperName = name.upper()
    
    print(f"""\n                    
                              _______📄_RESULT_📄______
                              |                       |
            /\ ,____/\           You are {result[0]}                               
           | | @    @'|              by {result[1]}
           | |    3    )      |_______________________|
            /          __       
           /           __)       
          (          /__               
      ( ( |         ___)                   
            \   ,,_,,)                                    
             \_)
          
        \n""")
    print("======================================================")
    con = input(      "Do you want to continue? Y/N: ")
    print("======================================================")

    if con.lower() == "n":
        print(f"""  
             ____________________
            (    Don't Forget    )                
             \      To Do       /                 |----------------|
              \    Exercise    /                  |     Goodbye    |
               \    Daily     /    /\_____/\            {name}
                \______   ___/    (  •   •  )     |--   -----------|
                        \_\      ___   3    __       /_/
                                (__   \/    __) 
                                __    BMI    ;;
                               (__          )
                                   ,,,     /
                `                     (___/ ,,
        """)
        exit()
    else:
        continue










