num= int(input("Enter a number: "))

if num%2==0:
    print(f"{num} is Even number")
else:
    print(f'{num} is a odd number')    \
    


# check if someone can vote or not by age


Age = int(input("Enter your age: "))

if Age>=18:
    print("you are eligible to vote")

else:
    print("You're not eligible to vote")    



# create a grading system for student marks rank from A to fail

Marks = int(input("Enter Marks: "))

if Marks <= 100 and Marks >= 80:
    print("You have an A")
elif Marks <= 79 and Marks >= 60:
    print("You have a B")
elif Marks <= 59 and Marks >= 40:
    print("You have a C")
elif Marks <= 39 and Marks >= 0:
    print("You have an F")
else:
    print("You have a missing or invalid mark")




# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Get user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Display result with classification
print(f"Your BMI is: {bmi:.2f}")

# BMI classification based on WHO standards
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
