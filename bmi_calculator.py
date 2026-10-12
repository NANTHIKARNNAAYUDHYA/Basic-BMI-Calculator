def calculate_bmi(weight, height):
    # คำนวณ BMI จากน้ำหนัก (kg) และส่วนสูง (m)
    bmi = weight / (height ** 2)
    return bmi

# ตัวอย่างการคำนวณ
weight_kg = 55.0
height_m = 1.65

result = calculate_bmi(weight_kg, height_m)
print("ค่า BMI ของคุณคือ:", round(result, 2))
