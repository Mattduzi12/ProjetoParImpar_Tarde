#Projeto par ou impar

#Apresentação
print('\n\t\t\t -- Verificador de Número \n\n')

#Entradas
num = int(input('Informe um número: '))

# Processamento e saida
if (num % 2) == 0:
    print(f'\n{num} é par!')
else:
    print(f'\n{num} é impar!')
