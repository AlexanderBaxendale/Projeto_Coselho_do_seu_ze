import requests
import time
from deep_translator import GoogleTranslator
from loguru import logger


def obter_conselho():

    r = requests.get('https://api.adviceslip.com/advice')
    if r.status_code == 200:
        return r.json()['slip']['advice'], r.json()['slip']['id']
    else:
        return "Erro ao obter conselho"    

def gerar_conselho():
        tradutor = GoogleTranslator(source="auto", target="pt")
        traducao = input('Gostaria de traduzir seu conselhos? - digite s/n: ')
        conselho, conselho_id = obter_conselho()
        if obter_conselho():
            conselhos.append((conselho, conselho_id))
            if traducao == 's':
                print(f' ID: {conselho_id}  -  conselho: {tradutor.translate(conselho)}')
                conselhos_traduzidos.append(tradutor.translate(conselho))
            elif traducao == 'n':
                print(f' ID: {conselho_id}  -  conselho: {(conselho)}')
            else:
                print('valor incorreto')

def abrir_conselho():
    try:
        if decicao == 's' :   
            with open('arquivo.txt', 'r', encoding='UTF-8') as arquivo:
                mostra_conselho = arquivo.read()
                print(mostra_conselho) 
        else:
            print('Você decidio não ver sua lista de conselho(s)')
    except FileNotFoundError:
            print('Ainda não há conselhos guardados')

    
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
    print('5 - Mostra conselhos traduzidos -')
    print('6 - Guarda conselhos Traduzidos -')
    print('7 - Sair do programa -')
    print('\n-------------------------------------------------\n')


print('\nX----------------------------------------------------------------X\n')
print('                 Bem-Vindo a Cachaçaria do Seu Zé!                  ')
print('                 A Melhor cachaçaria em dar conselhos               ')
print('\nX----------------------------------------------------------------X\n')

escolha = 1000

while escolha != 0:
    menu()
    try:
        escolha = int(input('Digite a opção desejavel:'))
    except ValueError:
        print('\n Digite uma valor valido \n')
        time.sleep(0.5)
    match escolha:
        case 1:
            print('\nX------------> QUANTIDADE DE CONSELHOS <------------X\n')
            try:
                quantidade_conselho = int(input('Quantos conselhos você quer ?: '))
                print('\nescolha a opção 2 para ver os seu conselhos\n')
            except ValueError :
                print('\ndigite um número valido!')
            time.sleep(0.5)
            conselhos = []
            
        case 2:
            print('\nX-------------> MOSTRA CONSELHO <-------------------X\n')
            conselhos_traduzidos = []
            try:
                for i in range(quantidade_conselho):
                    gerar_conselho()
                    time.sleep(1)
            except Exception as erro:
                print(f'Ocorreu um error: {erro} ! - Por favor digite a opção 1 antes dessa ')

           
        case 3 :
            print('\nX-------------> MOSTRA CONSELHO GUARDADO <-------------------X\n')
            try:
                salvar = input('Gostaria de salvar seu conselho(s) - Digite s/n :')
            except ValueError:
                print('\nDigite um valor valido!\n ')   
            try:  
                if salvar == 's':
                    guarda_conselho(conselhos)
                    print('Seu Conselho está salvo!')
                    time.sleep(0.5)
                elif salvar == 'n':
                    print('Você decidio não salvar seu conselho')
                    time.sleep(0.5)
                else:
                    print('digite um valor valido')
                    time.sleep(0.5)
            except Exception as erro :
                print(f'Ocorreu um error : {erro} - O conselho ainda não foi gerado')
            
        case 4:
            print('\nX-------------> ABRIR LISTA DE CONSELHOS <-------------------X\n')
            try:
                decicao = input('Gostaria de ver os sua lista de conselho(s) - Digite s/n :')
            except ValueError:
                print('\nDigite um valor valido\n')
                time.sleep(0.5)
            
            abrir_conselho()
            time.sleep(1)
              
        case 5:
            tradutor = GoogleTranslator(source='en', target='pt')
            
            try:
                mostra = input('\nGostaria de ver seus conselhos Traduzidos - Digite s/n :\n')    
            except ValueError:
                print('Digite uma valor valido')
            try:
                if mostra == 's':
                    print(conselhos_traduzidos)
                else:
                    print('você decidiu não ver seus conselhos traduzidos')
                    time.sleep(0.5)
            except Exception as erro:
                print(f'Ocorreu um error: {erro} -  Talvez os conselhos ainda não foram gerados')
        case 6:
            try:
                mostra_traducao = input('Aproveitando, você gostaria de salvar seus conselhos Traduzidos em um arquivo? - Digite s/n : ')
            except ValueError:
                print('\ndigite um valor valido\n')
                time.sleep(0.5)
            try:
                if mostra_traducao == 's':
                    with open('arquivo.txt', 'w', encoding='UTF-8') as arquivo:
                        for conselho, conselho_id in conselhos:
                            arquivo.write(f'ID: {conselho_id} - {tradutor.translate(conselho)}')
                    print('Seu conselho estar Salvo!')
                    time.sleep(0.5)
                else:
                    print('você decidiu não salvar seus conselhos traduzidos')
            except Exception as erro:
                    print(f'Ocorreu um error: {erro} -  Talvez os conselhos ainda não foram gerados') 
        case 7:
            sair = input('Deseja sair do Programa - Digite s/n :')
            time.sleep(0.5)
            if sair == 's':
                print('\nobrigado por passa na Cachaça do seu Zé - Até a próxima\n')
                break
            elif sair == 'n':
                print('\nVocê decidio fica para mais uma rodada\n')