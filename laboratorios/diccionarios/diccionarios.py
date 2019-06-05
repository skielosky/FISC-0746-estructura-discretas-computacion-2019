# Section 6.2.1 snippets
country_codes = {'Finland': 'fi', 'South Africa': 'za',
                 'Nepal': 'np'}

country_codes

# Determining if a Dictionary Is Empty
len(country_codes)

if country_codes:
    print('country_codes is not empty')
else:
    print('country_codes is empty')

country_codes.clear()

if country_codes:
    print('country_codes is not empty')

# Section 6.2.2 snippets
days_per_month = {'January': 31, 'February': 28, 'March': 31}

days_per_month

for month, days in days_per_month.items():
    print(f'{month} has {days} days')


# Section 6.2.3 snippets

# 6.2.3 Basic Dictionary Operations
roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}

roman_numerals

# Accessing the Value Associated with a Key
roman_numerals['V']

# Updating the Value of an Existing Key–Value Pair
roman_numerals['X'] = 10

roman_numerals

# Adding a New Key–Value Pair
roman_numerals['L'] = 50

roman_numerals

# Removing a Key–Value Pair
del roman_numerals['III']

roman_numerals

roman_numerals.pop('X')

roman_numerals

# Attempting to Access a Nonexistent Key
roman_numerals['III']

roman_numerals.get('III')

roman_numerals.get('III', 'III not in dictionary')

roman_numerals.get('V')

# Testing Whether a Dictionary Contains a Specified Key
'V' in roman_numerals

'III' in roman_numerals

'III' not in roman_numerals

# Section 6.2.4 snippets

months = {'January': 1, 'February': 2, 'March': 3}

for month_name in months.keys():
    print(month_name, end='  ')

for month_number in months.values():
    print(month_number, end='  ')

# Dictionary Views
months_view = months.keys()

for key in months_view:
    print(key, end='  ')

months['December'] = 12

months

for key in months_view:
    print(key, end='  ')

# Converting Dictionary Keys, Values and Key–Value Pairs to Lists
list(months.keys())

list(months.values())

list(months.items())

# Processing Keys in Sorted Order

for month_name in sorted(months.keys()):
    print(month_name, end='  ')

# Section 6.2.5 snippets
country_capitals1 = {'Belgium': 'Brussels',
                     'Haiti': 'Port-au-Prince'}

country_capitals2 = {'Nepal': 'Kathmandu',
                     'Uruguay': 'Montevideo'}

country_capitals3 = {'Haiti': 'Port-au-Prince',
                     'Belgium': 'Brussels'}

country_capitals1 == country_capitals2

country_capitals1 == country_capitals3

country_capitals1 != country_capitals2

# Section 6.2.7 snippets
# Python Standard Library Module ‘collections‘
from collections import Counter

text = ('this is sample text with several words '
        'this is more sample text with some different words')

counter = Counter(text.split())

for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')

print('Number of unique keys:', len(counter.keys()))

# Section 6.2.8 snippets
country_codes = {}

country_codes.update({'South Africa': 'za'})

country_codes

country_codes.update(Australia='ar')

country_codes

country_codes.update(Australia='au')

country_codes