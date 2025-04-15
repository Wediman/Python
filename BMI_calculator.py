height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

h_height = float(height)
w_weight = float(weight)
bmi_result = int(w_weight / (h_height * h_height))

if int(bmi_result) <= 18.5:
    print(f"Your BMi is {bmi_result}, you are slightly underweight.")
elif bmi_result <=25:
    print(f"Your BMi is {bmi_result}, you have a normal weight.")
elif bmi_result <=30:
    print(f"Your BMi is {bmi_result}, you are obese.")
else:
    print(f"Your BMi is {bmi_result}, you are clinically obese.")