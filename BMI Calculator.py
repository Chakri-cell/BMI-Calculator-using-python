# BMI Calculator
def calculate_bmi(weight, height):

    bmi = weight / (height ** 2)
    return bmi
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
def main():
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            if weight <= 0:
                print("Error: Weight must be a positive number.")
                continue
            
            height = float(input("Enter your height in meters: "))
            if height <= 0:
                print("Error: Height must be a positive number.")
                continue
            
            bmi = calculate_bmi(weight, height)
            bmi_category = classify_bmi(bmi)
            
            print(f"Your BMI is: {bmi:.2f}")
            print(f"BMI Category: {bmi_category}")
            break
        
        except ValueError:
            print("Error: Please enter a valid number.")
if __name__ == "__main__":
    main()