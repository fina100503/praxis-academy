>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
tel['jack']
4098
del tel['sape']
tel['irv'] = 4127
tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
list(tel)
['jack', 'guido', 'irv']
sorted(tel)
['guido', 'irv', 'jack']
'guido' in tel
True
'jack' not in tel
False
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
 {x: x**2 for x in (2, 4, 6)}
 print( {x: x**2 for x in (2, 4, 6)})
dict(sape=4139, guido=4127, jack=4098)
print(dict(sape=4139, guido=4127, jack=4098))dict(sape=4139, guido=4127, jack=4098)