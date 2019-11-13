from collections import Counter

def checkio(text):
	text=text.lower()
	lista=[]
	letra=[]

	for character in text:
		if (character.isalpha()):
			lista.extend(character)
	#print(lista)
	#h=sorted(lista)
	#print(h)
	c=Counter(lista)
	for letter, value in c.items():
		if value == max(c.values()):
			letra.extend(letter)
	d=sorted(letra)

	#print(d[0])
	return d[0]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

#Another way to do it 
# import string
#
# def checkio(text):
#     """
#     We iterate through latyn alphabet and count each letter in the text.
#     Then 'max' selects the most frequent letter.
#     For the case when we have several equal letter,
#     'max' selects the first from they.
#     """
#     text = text.lower()
#     return max(string.ascii_lowercase, key=text.count)