# etapa 2 - Determinar o tipo de elemento
print(type('Hello world'))
print(type(7))

print(type(True))
print(type(False))

print(type('True'))
print(type('False'))
## etapa 3 - Análise booleana de string
print(bool('True'))
print(bool('False'))
print(bool(''))
print(bool(' '))
print(bool('Hello world'))
## etapa 4 - Análise booleana de números
print(bool(7))
print(bool(1))
print(bool(0))
print(bool(-1))
## etapa 5 - Análise booleana de comparação
print(1 + 1 == 3)
print(1 + 1 == 2)
## etapa 6 - Análise booleana de operadores lógicos
print(3 == 4)
print(3 != 4)
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
## etapa 7 - Análise de expressões booleanas
first_number = 5
second_number = 0
true_value = True
false_value = False

if first_number > 1 and first_number < 10:
    print('The value is between 1 and 10.')

if first_number > 1 or second_number > 1:
    print('At least one value is greater than 1')

print(not true_value)
print(not false_value)

if not first_number > 1 and second_number < 10:
    print('Both values pass the test')
else:
    print('Both values do NOT pass the test')