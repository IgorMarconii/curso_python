nome = 'Igor Marconi'
altura = 1.85
peso = 87
formula_imc = peso / altura**2
peso_estaideal = formula_imc > 18.9 and formula_imc < 24.9  

print(f'{nome}, tem {altura} de altura e pesa {peso:.2f}')
print(f'e seu IMC é {formula_imc:.2f}')
print(f'O seu peso está ideal: {peso_estaideal}')