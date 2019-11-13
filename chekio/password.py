def checkio(data):
	upper_flag =False
	Lower_flag = False
	number_flag = False

	if len(data)<10:
		return False

	else:
		for character in data:
			if character.isupper():
				upper_flag=True
			if character.islower():
				Lower_flag= True
			if character.isdigit():
				number_flag=True
		return upper_flag and Lower_flag and number_flag


#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")