def Calculate_bmi(weight, height, measure_scale):
    if measure_scale == "kg/m":
        return weight / (height ** 2)
    elif measure_scale == "lb/in":
        return (weight / (height ** 2)) * 703
    else:
        return None

def Bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal Weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obesity"
