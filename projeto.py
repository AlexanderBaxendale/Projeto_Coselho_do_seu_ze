import requests
from deep_translator import GoogleTranslator
from loguru import logger




def obter_conselho():

    r = requests.get('https://api.adviceslip.com/advice')
    if r.status_code == 200:
        return r.json()['slip']['advice']
    else:
        return "Erro ao obter conselho"

if __name__== '__main__':
    obter_conselho()



def numero_de_conselhos():

    tradutor = GoogleTranslator(source="en", target= "pt")
    try:
        quantidade = int(input('Quantos conselhos você quer?:'))
        if quantidade <= 0:
            print('Digite um número positivo')
            return
    except ValueError:
        print('Digite uma Número válido!')
        return
    
    for i in range(quantidade):
        print(f'conselho {i+1} : {tradutor.translate(obter_conselho())}')
if __name__ == '__main__':
    numero_de_conselhos()



def guarda_conselho():
    
    gera_conselho= requests.get('https://api.adviceslip.com/advice')      
    try:
        gera_conselho == 200
        return numero_de_conselhos()
    except ValueError as error:
        logger.exception(f'Error:{error}')
    
    with open('Conselhos.txt', 'w', encoding='UTF-8') as conselhos_salvo:
        conselhos_salvo.write(gera_conselho.text)

if __name__ == '__main__':
    guarda_conselho()