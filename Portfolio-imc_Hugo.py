# CALCULADORA DE IMC
def calculadora_imc(peso, altura): #função que vou usar pra calcular o meu Imc
        seu_imc = peso / (altura * altura)
        return seu_imc

# Coleta os dados do usuário atraz do input() e armazena na variaveis  nome, peso e altura
nome = input("Digite seu nome ")
peso = float(input("Digite seu peso em quilos (sem as gramas) "))
altura = float(input("Informe sua altura (metro e cm, separados por ponto) ")) 

imc = calculadora_imc(peso, altura) # Chamando a função da linha 2 e armazenado na varialvel imc


# Classificação do Imc CONDIÇÕES ABAIXO
if imc >= 16.0 and imc <= 16.9 :
       print(f"{nome} você esta na magreza extrema! Isso indicar problemas graves de saúde seu IMC é {imc:.1f}")
elif imc >= 17.0 and imc <= 18.5 :
       print(f"{nome} você esta na magreza leve! esta na hora de comer mais seu IMC é {imc:.1f}") 
elif imc >= 18.5 and imc <= 24.9 :
       print(f"{nome} você esta no peso normal! Parabéns e seu IMC é {imc:.1f} ideal continue assim")       
elif imc >= 25.0 and imc <= 29.9 :
       print(f"{nome} você esta no sobrepeso! Esta na hora de uma saladinha, não acha? seu IMC é {imc:.1f}")       
elif imc >= 30.0 and imc <= 34.9 :
       print(f"{nome} você esta na obesidade grau I Procure seu medico e seu IMC é {imc:.1f}")
elif imc >= 35.0 and imc <= 39.9 :
       print(f"{nome} você esta na obesidade grau II ou severa sua saúde esta prejudicada e seu IMC é {imc:.1f}")
elif imc <= 40.0:
       print(f"{nome} você esta na obesidade grau III ou mórbida vá ao hospital com urgencia e seu IMC é {imc:.1f}")      
else:    #Pensando no Usuario se ele digitar algo errado fora da classificação.
 print(f"Houve um Erro em sistema {nome} ou seu IMC esta abaixo do 16.0 ou acima de 40.0 sendo ele {imc:.1f} aparentando estar quase morrendo")