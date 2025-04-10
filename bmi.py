def bmiRechner():
    gewicht = float(input("Gib dein Gewicht in kg an"))
    groesse = float(input("Gib deine groesse in Metern an"))
    bmi = gewicht / (groesse ** 2)
    bmi = bmi * 10000
    print("Dein BMI beträgt: + (bmi:f)")