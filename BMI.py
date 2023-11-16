print('此BMI計算機僅供學術交流運用')
print('身高請進到小數第二位 例如:166-->1.66')
height = input('請輸入你的身高: ')
weight = input('請輸入你的體重: ')

height = float(height)
weight = float(weight)

bmi = weight / (height* height)
bmi = float(bmi)
print(round(bmi, 1))

if bmi < 18.5:
	print('體重過輕')
elif bmi >=18.5 and bmi < 24:
	print('體重正常')
elif bmi >= 24 and bmi < 27:
	print('體重過重')
elif bmi >= 27 and bmi < 30:
	print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('中度肥胖')
else:
	print('你超胖的')