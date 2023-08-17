
#### informacoes do usuario ####
nome = input('Digite seu nome: ')
idade = int(input('digite sua idade: '))
altura = float(input('digite sua altura (em metros): '))
hobby = str(input('digite algo que você gosta de fazer: '))

###calculo do IMC####
peso = float(input('Qual seu peso? '))
imc = (peso/(altura ** 2))

#dica do imc

if imc < 18.5:
    tipo_imc = 'abaixo do peso'
elif imc < 25:
    tipo_imc = 'com peso saudavel'
elif imc < 30:
    tipo_imc = 'acima do peso'
else:
    tipo_imc = "obessidade"

#imprimir perfil do usuario
print('Ola {}, vi que você tem {} e mede {} e vi tambem que gosta de {}'.format(nome,idade,altura,hobby))
print('seu IMC deu {} e isso indica que você esta {}'.format(imc,tipo_imc))



