driving = input('have ever drive a car, yes or no?')
if driving != 'yes' and driving != 'no':
	print('please type yes or no')
	raise SystemExit

age = input('how old are you?')
age = int(age)
if driving == 'yes':
    if age >= 18:
    	print('you can drive legally')
    else:
    	print('how come you can drive?you have no driving license')
elif driving == 'no':
	if age >=18:
		print('you can go for lisense test')
	else:
		print('you are too young to drive')

