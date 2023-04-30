print()
print('** UNIT CONVERTER **')
print()

conversions_available =	[(1, 'km', 'mi'),
                         (2, 'mi', 'km'),
                         (3, 'kg', 'lbs'),
                         (4, 'lbs', 'kg'),
                         (5, '°F', '°C'),
                         (6, '°C', '°F'),
                         (7, 'Gal', 'Ft³'),
                         (8, 'Ft³', 'Gal'),
                         (9, 'pressure head in ft', 'psi'),
                         (10, 'psi', 'pressure head in ft'),
                         (11, '°C', '°F'),
                         (12, '°C', '°F'),
                         (13, '°C', '°F'),
                         (14, '°C', '°F'),
                         (15, '°C', '°F'),
                         (16, '°C', '°F'),
                         (17, '°C', '°F'),
                         (18, '°C', '°F'),
                         (19, '°C', '°F'),
                         (20, '°C', '°F'),
                         ]

print('Conversions available:')
print()

for converson_number, from_unit, to_unit in conversions_available:
  print(f'{converson_number}) {from_unit} -> {to_unit}')

print()
conversion = input('Enter the number of the conversion to use --> ')
conversion_index = int(conversion) - 1

converson_number, from_unit, to_unit, = conversions_available[conversion_index]
print()
from_value = float(input(f'Enter{from_unit}--> '))
print()

if converson_number == 1:
    to_value = from_value * .62
    print(f'{from_value} {from_unit} -> {to_value} { to_unit}')

elif converson_number == 2:
   to_value = from_value / .62
   print(f'{from_value} {from_unit} -> {to_value} { to_unit}')

elif converson_number == 3:
   to_value = from_value * .45
   print(f'{from_value} {from_unit} -> {to_value} { to_unit}')

elif converson_number == 4:
   to_value = from_value / .45
   print(f'{from_value} {from_unit} -> {to_value} { to_unit}')

elif converson_number == 5:
   to_value = (from_value - 32) / 1.8
   print(f'{from_value} {from_unit} -> {to_value} { to_unit}')

elif converson_number == 6:
   to_value = from_value * 1.8 + 32
   print(f'{from_value} {from_unit} -> {to_value} { to_unit}')

elif converson_number == 7:
   to_value = from_value / 7.48051949
   print(f'{from_value} {from_unit} -> {to_value} { to_unit}')

elif converson_number == 8:
   to_value = from_value * 7.48051949
   print(f'{from_value} {from_unit} -> {to_value} { to_unit}')
   
elif converson_number == 9:
   to_value = from_value * 62.4 / 144
   print(f'{from_value} {from_unit} -> {to_value} { to_unit}')

elif converson_number == 10:
   to_value = from_value / (62.4 / 144)
   print(f'{from_value} {from_unit} -> {to_value} { to_unit}')

elif converson_number == 11:
   to_value = from_value * 7.48051949
   print(f'{from_value} {from_unit} -> {to_value} { to_unit}')

elif converson_number == 12:
   to_value = from_value * 7.48051949
   print(f'{from_value} {from_unit} -> {to_value} { to_unit}')

elif converson_number == 13:
   to_value = from_value * 7.48051949
   print(f'{from_value} {from_unit} -> {to_value} { to_unit}')

elif converson_number == 14:
   to_value = from_value * 7.48051949
   print(f'{from_value} {from_unit} -> {to_value} { to_unit}')

elif converson_number == 15:
   to_value = from_value * 7.48051949
   print(f'{from_value} {from_unit} -> {to_value} { to_unit}')



