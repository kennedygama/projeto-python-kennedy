# ============================================
#        CÁLCULO DE GANHOS POR HORA
# ============================================

print('\n' + '=' * 45)
print('          GANHOS POR HORA ')
print('=' * 45 + '\n')

# --- Entrada de dados ---
nome = input("Olá! Qual é o seu nome? ")

# Validação simples para salário
while True:
    try:
        salario = float(input(f"{nome}, digite seu salário mensal (R$): "))
        break
    except ValueError:
        print(" Digite um número válido! Ex: 2500.00")

# Validação simples para horas
while True:
    try:
        horas_mes = int(input("Digite o total de horas trabalhadas por mês: "))
        if horas_mes > 0:
            break
        print(" As horas devem ser maior que 0.")
    except ValueError:
        print(" Digite um número inteiro válido! Ex: 160")

# --- Processamento ---
print('\n' + '-' * 45)
print(" PROCESSANDO INFORMAÇÕES...")
print('-' * 45 + '\n')

salario_horas = salario / horas_mes

# --- Resultado ---
print(f" {nome}, aqui está o resultado:")
print(f" Salário mensal: R$ {salario:,.2f}")
print(f" Horas por mês: {horas_mes} horas")
print(f" Ganho por hora: R$ {salario_horas:,.2f}")

print('\n' + '=' * 45)
print("          CÁLCULO FINALIZADO")
print('=' * 45)
