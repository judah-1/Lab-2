def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / height / height
    print(bmi)
    if bmi > 25.0:
        print("Weight classification: Overweight")
    else:
        if bmi < 18.5:
            print("Weight classification: Underweight")
        else:
            print("Weight classification: Normal Weight")


calculate_bmi(1.57,20)