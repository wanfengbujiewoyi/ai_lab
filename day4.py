bmi=input("How number of your BMI?")
bmi=float(bmi)
if bmi<18.5:
   print("你的bmi属于偏瘦范围")
elif bmi<24:
   print("你的bmi属于正常范围")
elif bmi<28:
   print("超重")
else:
   print("肥胖")
            