#texty
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#definování pole uživatelů a řádkového oddělovače.
users = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
separator = '-' * 63

#Přivítání uživatele
print(separator)
print('Welcome to the app. Please log in: ')

#Přihlášení uživatele s kontrolou vstupních dat.
username = input('USERNAME: ').lower()
pasword = str(input('PASSWORD: ')).lower()
if users.get(username) == pasword:
	print(separator)
else:
	print('udaje incorected')
	exit()

#Výběr textu uživatelem zadáním čísel od jedné do tří. Kontrola zadaného čísla.
print('We have 3 texts to be analyzed.')
number = input('Enter a number btw. 1 and 3 to select: ')
if number in ['1', '2', '3']:
	number = int(number)
else:
	print('wrong asignment, repeat !!!')
	exit()
print(separator)
#vytvoření proměnné "text" v které bude text podle výběru uživatele.
text = TEXTS[number - 1]
print(f'You choose this text:\n {text}' )
print(separator)

#Rozsekání textu na slova a očištění od mezer, čárek a teček.
clear_list = []
for word in text.split():
	clear_word = word.strip(" ,.")
	clear_list.append(clear_word)

#Vytvoření proměnných a cyklu pro výpis počtu slov dle zadání.
sumOfWords = len(clear_list)
capitalLetter = 0
capitalLetters = 0
smallLeters = 0
numberCount = 0
sumOfNumbers = 0
for char in clear_list:
	if char.istitle():
		capitalLetter += 1
	elif char.isupper():
		capitalLetters += 1
	elif char.islower():
		smallLeters += 1
	elif char.isnumeric():
		numberCount += 1
		sumOfNumbers = sumOfNumbers + int(char)

#Výpis výše definovaných proměnných.
print(f'There are {sumOfWords} words in the selected text.')
print(f'There are {capitalLetter} titlecase words.')
print(f'There are {capitalLetters} uppercase words.')
print(f'There are {smallLeters} lowercase words.')
print(f'There are {numberCount} numeric strings.')
print(separator)

#Vytvoření slovníku pro graf, který zobrazí pomocí znaku "*" počet opakujících se délek slov.
chart = {}
for chart_word in clear_list:
	if len(chart_word) not in chart:
		chart[len(chart_word)] = 1
	else:
		chart[len(chart_word)] += 1

cetnost = sorted(chart, key=chart.get)
for slovo in cetnost:
    print(f'{slovo}{chart.get(slovo) * "*"}{chart.get(slovo)}')

#Součet všech čísel ve vybraném textu.
print(separator)
print(f'If we summed all the numbers in this text we would get: {sumOfNumbers}.')
print(separator)


