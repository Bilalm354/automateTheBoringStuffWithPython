Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> myCat = {'size':'fat', 'color
	 
SyntaxError: EOL while scanning string literal
>>> myCat = {'size':'fat', 'color':'gray', 'disposition':'loud'}
>>> myCat.size
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    myCat.size
AttributeError: 'dict' object has no attribute 'size'
>>> myCat['size']
'fat'
>>> 'My cat has ' + myCat['color'] + ' fur'
'My cat has gray fur'
>>> f"My cat has {myCat['color']} fur"
'My cat has gray fur'
>>> 
== RESTART: /Users/Bilal/automateTheBoringStuffWithPython/chapter-5/birthdays.py =
Enter a name: (blank to quit)
bilal
I do not have birthday information for bilal.
What is their birthday?
Jul 18
Birthday database updated.
Enter a name: (blank to quit)

>>> birthdyas
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    birthdyas
NameError: name 'birthdyas' is not defined
>>> birthdays
{'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4', 'bilal': 'Jul 18'}
>>> spam = {'color': 'red', 'age': 42}
>>> for v in spam.value():
	print(v)

	
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    for v in spam.value():
AttributeError: 'dict' object has no attribute 'value'
>>> for v in spam.values:
	print(v)

	
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    for v in spam.values:
TypeError: 'builtin_function_or_method' object is not iterable
>>> spam
{'color': 'red', 'age': 42}
>>> for v in spam.values():
	print(v)

	
red
42
>>> for k in spam.keys():
	print(k)

	
color
age
>>> for i in spam.items():
	print(i)

	
('color', 'red')

('age', 42)
>>> spam.keys()
dict_keys(['color', 'age'])
>>> list(spam.keys())
['color', 'age']
>>> spam = {'color': 'red', 'age': 42}
>>> for k, v in spam.items():
	print('key: ' + k + ' Value:' + str(v))

	
key: color Value:red
key: age Value:42
>>> 'name' in spam.keys()
False
>>> Zophie in spam.values()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    Zophie in spam.values()
NameError: name 'Zophie' is not defined
>>> 'Zophie' in spam.values()
False
>>> 'name' not in spam.keys()
True
>>> picnicItems = {'apples':: 5, 'cups':2}
SyntaxError: invalid syntax
>>> f"I am bringing {str(picnicItems.get('cups', 0))} cups."
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    f"I am bringing {str(picnicItems.get('cups', 0))} cups."
NameError: name 'picnicItems' is not defined
>>> picnicItems = {'apples': 5, 'cups':2}
>>> f"I am bringing {str(picnicItems.get('cups', 0))} cups."
'I am bringing 2 cups.'
>>> f"I am bringing {str(picnicItems.get('eggs', 0))} eggs."f"I am bringing {str(picnicItems.get('cups', 0))} cups."
'I am bringing 0 eggs.I am bringing 2 cups.'
>>> spam = {
	'name': 'Pooka',
	'Age': 5}
>>> spam.setDefault('color': 'black')
SyntaxError: invalid syntax
>>> spam.setDefault('color','black')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    spam.setDefault('color','black')
AttributeError: 'dict' object has no attribute 'setDefault'
>>> spam.setdefault('color','black')
'black'
>>> spam
{'name': 'Pooka', 'Age': 5, 'color': 'black'}
>>> spam.setdefault('color','white')
'black'
>>> spm
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    spm
NameError: name 'spm' is not defined
>>> spam
{'name': 'Pooka', 'Age': 5, 'color': 'black'}
>>> 
= RESTART: /Users/Bilal/automateTheBoringStuffWithPython/chapter-5/characterCount.py
{'I': 1, 't': 6, ' ': 13, 'w': 2, 'a': 4, 's': 3, 'b': 1, 'r': 5, 'i': 6, 'g': 2, 'h': 3, 'c': 3, 'o': 2, 'l': 3, 'd': 3, 'y': 1, 'n': 4, 'A': 1, 'p': 1, 'e': 5, 'k': 2}
>>> 
