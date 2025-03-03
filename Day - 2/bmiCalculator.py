# ==========================
# SIMPLE BMI CALCULATOR
# ==========================

# Get user input for weight (kg) and height (m)
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display the result
print(f"Your BMI is: {bmi:.2f}")

# Categorize BMI
if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 24.9:
    print("Category: Normal weight")
elif 25 <= bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")
