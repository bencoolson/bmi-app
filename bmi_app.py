w=input("What is your weight\n")
w = float(w)
h = input("what is your height\n")
h = float(h)

def BMI_calc(w,h):
    BMI=(w/(h**2))
    BMI=round(BMI,1)
    
    if BMI<18.5:
        print(f"Your BMI Is :{BMI}\nUnderweight")
    elif 18.4< BMI<25:
        print(f"Your BMI IS : {BMI}\nNormal")
    elif 24.9<BMI<30:
        print(f"Your BMI IS :{BMI}\nOverweight")
    elif 29.9<BMI < 35:
        print(f"Your BMI IS : {BMI}\nClass 2 Obesity")
    elif 34.9<BMI < 40:
        print(f"Your BMI IS :{BMI}\nClass 2 obesity")
    else:
        print(f"Your BMI IS : {BMI}\nExtreme Obesity")
        
BMI_calc(w,h)
        
