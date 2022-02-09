weight = str(input("Enter your weight : "))
height = str(input("Enter your height :"))

height2 = float(height) * float(height)

BMI = int(weight) / height2


if BMI < 18.5:
    print("Underweight")
else:
    if (BMI >= 18.5) and (BMI<25):
        print("Normal")
    elif (BMI >= 25) and (BMI<30):
        print("Overweight")
    elif BMI > 30:
        print("Obesity")

