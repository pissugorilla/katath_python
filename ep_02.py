def feet_to_meters(feet):
    """Converts feet to meters."""
    meters = feet * 0.3048
    return meters

def calculate_bmi(weight,height):
    """Calculates BMI."""
    bmi = weight / (height ** 2)
    return bmi

# 0 - 18.5 : "Underweight"
# 18.5 - 25: "Normal weight"
# 25 - 30: "Overweight"
# 30 + : "Obese"

def interpret_bmi(bmi):
    """Interprets BMI."""
    if bmi < 18.5:
       return "Underweight"
    elif 18.5 <= bmi < 25:
      return "Normal weight"
    elif 25 <= bmi < 30:
      return "Overweight"
    else:
      return "Obesity"
    
#BMI calculation
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enetr your height in feets: "))

#convert feet value to meter
height_in_meter = feet_to_meters(height)
# calculate the BMI value
bmi_vaule = calculate_bmi(weight,height_in_meter)
# interpret the BMI value
bmi_interpretation = interpret_bmi(bmi_vaule)

print(f"Your BMI is {bmi_vaule:.2f} which means you are {bmi_interpretation}.")
