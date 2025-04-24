import pywhatkit as kit
import time

# Lista de contatos (números de telefone no formato internacional com código do país)
contatos = [
        "+5521980395021"
]
# Coleta números de telefone do usuário
while True:
    novo_numero = input("Digite um número de telefone para enviar o ZAP (ou 'sair' para terminar e manda zap somente para os da lista): ")
    if novo_numero.lower() == 'sair':
        break
    contatos.append(novo_numero)  # Adiciona o número à lista de contatos

# Mensagem a ser enviada
mensagem = "Olá, esta é uma mensagem automatizada do programador HUGO que esta criando essa API. Tenha um ótima dia e bora pra CIMA BRASIL !"

# Função para enviar mensagens
def enviar_mensagens(contatos, mensagem):
    for numero in contatos:
        try:
            # Verifica se o número tem exatamente 13 caracteres
            if len(numero) != 14:  # O número deve ter exatamente 14 caracteres se não resultar em erro
                raise ValueError("Número não encontrado")  # Simulando um erro
            
            # Horário de envio - define para um minuto à frente do atual
            hora_atual = time.localtime()
            hora = hora_atual.tm_hour
            minuto = hora_atual.tm_min + 1
                       
            # Envia a mensagem
            kit.sendwhatmsg(numero, mensagem, hora, minuto)
            
            print(f"Mensagem enviada para {numero}")
            time.sleep(30)  # Aguarda 30 segundos antes de enviar para o próximo contato
            
        except Exception as e:
            
            print(f"Falha ao enviar mensagem para {numero}: {str(e)}")
            

# Chama a função para enviar as mensagens
enviar_mensagens(contatos, mensagem)

