print("="*30)
print('CALCULADORA IMC')
print("="*30)
nome = input('Olá, como se chamar ?')
print("-"*30)
peso = float(input(f'{nome} digite seu peso: '))
print("_"*30)
altura = float(input(f'{nome} digite sua altura'))
print("="*30)
print('CALCULO SENDO FEITO.....')
imc = peso / (altura * 2)
if imc <= 18.5:
    print(f'{nome}, seu IMC é {imc:.1f} \n MAGREZA')
elif imc >= 18.5 and imc <= 24.9:
    print(f'{nome}, seu IMC é {imc:.1f} \n NORMAL')
elif imc >= 25.0 and imc <=29.9:
    print(f'{nome}, seu IMC é {imc:.1f} \n SOBREPESO')
elif imc >= 30.0 and imc <= 39.9:
    print(f'{nome}, seu IMC é {imc:.1f} \n OBESIDADE')
else:
    print(f'{nome}, seu IMC é {imc:.1f} \n OBESIDADE GRAVE')
