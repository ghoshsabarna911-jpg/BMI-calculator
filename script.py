a = float(input('Enter your weight in kgs or lbs: '))
b = float(input('Enter your height in inches or cms: '))
y = input('Was your weight in kgs or lbs? ').strip().upper()
z = input('Was your height in inches or cms? ').strip().upper()

# Convert weight to kg
if y == 'KGS':
    pass
elif y == 'LBS':
    a = a * 0.453592

# Convert height to meters
if z == 'CMS':
    b = b * 0.01
elif z == 'INCHES':
    b = b * 0.0254

# Calculate BMI
BMI = a / (b**2)

print(f'Your BMI is: {BMI:.2f}')

# BMI Categories
if BMI < 18.5:
    print('You are underweight, need to gain some weight.')
elif 18.5 <= BMI < 25:
    print('You are normal, don’t listen to others.')
elif 25 <= BMI < 30:
    print('You are overweight, not obese but still need to lose some weight.')
elif 30 <= BMI < 40:
    print('You are obese and need to lose some weight.')
else:
    print('You are severely obese, it is serious and possibly harmful.')

print('Results are for adults only and do not apply to teenagers or kids. THANK YOU!')
