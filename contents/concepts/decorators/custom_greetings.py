#Functions returns functions

def greeting(lang):
	def custom_greetings(name):
		if lang.lower() == 'english':
			greet = 'Hello '
		elif lang.lower() == 'german':
			greet = 'Hallo '
		elif lang.lower() == 'marathi':
			greet = 'Namaskar '
		else:
			greet = 'Hi '

		return greet + name + '!!'
	return custom_greetings


lang = input('Language: ')
name = input('Name: ')
greet = greeting(lang)
print(greet(name))

