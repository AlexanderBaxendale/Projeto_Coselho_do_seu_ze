import requests
from deep_translator import GoogleTranslator
from loguru import logger


def obter_conselho():

    r = requests.get('https://api.adviceslip.com/advice')
    if r.status_code == 200:
        return r.json()['slip']['advice'], r.json()['slip']['id']
    else:
        return "Erro ao obter conselho"    

def gerar_conselho():
     
        conselho, conselho_id = obter_conselho()
        if obter_conselho():
            conselhos.append((conselho, conselho_id))
            print(f' ID: {conselho_id}  -  conselho: {conselho}')  
    
    
def guarda_conselho(conselhos):
    with open('arquivo.txt', 'w', encoding='UTF-8') as arquivo:
        for conselho, conselho_id in conselhos:
            arquivo.write(f'ID: {conselho_id} - {conselho}')

def menu():
    print('\n-------Escolha entre uma das opções abaixo-------\n')
    print('1 - Ouvir o Seu Zé -')
    print('2 - Mostra Conselho -')
    print('3 - Guardar a Sabedoria -')
    print('4 - Mostra conselhos guardados -')
    print('5 - Traduzir conselhos -')
    print('6 - Traduzir conselhos salvos -')
    print('7 - Sair do programa -')
    print('\n-------------------------------------------------\n')


print('\n----------------------------------------------------------------\n')
print('                 Bem-Vindo a Cachaçaria do Seu Zé!                  ')
print('                 A Melhor cachaçaria em dar conselhos               ')
print('\n----------------------------------------------------------------\n')

escolha = 1000

while escolha != 0:
    menu()
    try:
        escolha = int(input('Digite a opção desejavel:'))
    except ValueError:
        print('\n Digite uma valor valido \n')

    match escolha:
        case 1:
            print('\n------------> QUANTIDADE DE CONSELHOS <------------\n')
            try:
                quantidade_conselho = int(input('Quantos conselhos você quer ?: '))
            except ValueError :
                print('digite um número valido!')
            
            conselhos = []
            print('\nescolha a opção 2 para ver os seu conselhos\n')
        case 2:
            print('\n-------------> MOSTRA CONSELHO <-------------------\n')
            try:
                for i in range(quantidade_conselho):
                    gerar_conselho()
            except Exception as erro:
                print(f'\nOcorreu um error: {erro} ! - Por favor digite a primeiro  opção 1 antes dessa \n')

           
        case 3 :
            print('\n-------------> MOSTRA CONSELHO GUARDADO <-------------------\n')
            try:
                salvar = input('Gostaria de salvar seu conselho(s) - Digite s/n :')
            except ValueError:
                print('\nDigite um valor valido - Porfavor segua a ordem! \n')   
              
            if salvar == 's':
                guarda_conselho(conselhos)
                print('Seu Conselho está salvo!')
            elif salvar == 'n':
                print('Você decidio não salvar seu conselho')
            else:
                print('digite um valor valido')
            
            
        case 4:
            print('\n-------------> ABRIR LISTA DE CONSELHOS <-------------------\n')
            try:
                decicao = input('Gostaria de ver os sua lista de conselho(s) - Digite s/n :')
            except ValueError:
                print('Digite um valor valido')
            
            try:
                if decicao == 's' :   
                    with open('arquivo.txt', 'r', encoding='UTF-8') as arquivo:
                        mostra_conselho = arquivo.read()
                        print(mostra_conselho) 
                else:
                    print('Você decidio não ver sua lista de conselho(s)')
            except FileNotFoundError:
                print('O arquivo não foi encontrado')
            
        case 5:
            
            tradutor = GoogleTranslator(source="auto", target="pt")
            print(tradutor.translate(conselhos))
        case 7:
            sair = input('Deseja sair do Programa - Digite s/n :')
            if sair == 's':
                print('\nobrigado por passa na Cachaça do seu Zé - Até a próxima\n')
                break
            elif sair == 'n':
                print('\nVocê decidio fica para mais uma rodada\n')