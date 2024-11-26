import requests
from deep_translator import GoogleTranslator
from loguru import logger
r = requests.get('https://api.adviceslip.com/advice')


print(r.json()['slip']['id'])
print("-------------------------------")
print(r.json()['slip']['advice'])
print("-------------------------------")

def conselhos_do_zé():

    tradutor = GoogleTranslator(source="en", target= "pt")
    conselho = (r.json()['slip']['advice'])

    traducao_conselho = tradutor.translate(conselho)
    print(traducao_conselho)

if __name__ == '__main__':
    conselhos_do_zé()

print('\n--------Tela de quantidades-------\n')

numeros_conselho = int(input('Quantos conselhos você quer?'))


def quantidade_conselhos():
    while numeros_conselho:
        if numeros_conselho >= 1:
            break
if __name__ == "__main__":
    quantidade_conselhos()


    
