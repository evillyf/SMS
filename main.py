# Instalações terminal:
#  - pip install selenium
#  - pip install twilio
#
#
# Instalação chromedriver:
#  - ver sua versão do Chrome em: Ajuda > Sobre o Google Chrome.
#  - fazer download em https://chromedriver.chromium.org/downloads de acordo com tua versão do Chrome (dois primeiros digítos).
#  - salvar o executável na mesma pasta do projeto.
#
#
# Agendador de Tarefas:
#  - instruções para rodar o código automaticamente em README-AGENDADOR.
#



############## BUSCANDO AS INFORMAÇÕES ##############

# Usando o selenium

import time
from selenium import webdriver

# remover as options de segundo plano se quiser ver o código rodando
chrome_options = webdriver.ChromeOptions() #faz o código rodar em segundo plano
chrome_options.add_argument('headless') #faz o código rodar em segundo plano

driver = webdriver.Chrome(options=chrome_options) #entre parênteses faz o código rodar em segundo plano

# selenium abre o navegador com o link especificado.
driver.get(
    'https://www.amazon.com.br/Becoming-Michelle-Obama/dp/1524763136/ref=sr_1_2?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=becoming&qid=1637448542&sr=8-2&ufe=app_do%3Aamzn1.fos.db68964d-7c0e-4bb2-a95c-e5cb9e32eb12')
time.sleep(1) # apesar do selenium aguardar a página carregar automaticamente, as vezes é necessário o sleep caso apareçam pop-outs na página ou garantir que não haverá nenhum bug.

# selenium busca a informação que contém a id "price" no código html da página. (inspecionar página > ctrl + shift + c > selecionar elemento desejado > ver sua parte do código destacado em azul)
valor = driver.find_element_by_id("price")
# converte o valor buscado em texto
valor = valor.text
# mostra o valor requerido no output.
print(valor)



############## ENVIANDO SMS ##############

# Usando a API Twilio. Necessário cadastro (https://www.twilio.com/)


from twilio.rest import Client

# informações que o site disponibiliza na home quando faz login
account_sid = 'ACc90e91d305a4d31f5e2ca81e715087b7'
token = '4161008cc46e634a4f3786dc741f95ff'

Client = Client(account_sid, token)

remetente = '+17406933961' #número que o twilio disponibiliza para o user
destino = '+5521912345678' #seu número de telefone aqui (necessário verificação. Caso queira add outro núm: ir em > Phone Numbers > Manage > Verified Caller ID's)


# mensagem que será enviada para o celular
message = Client.messages.create(
    to=destino, # variavél destino com os seus números verificados
    from_=remetente, # variavél remetente com o número que o twilio disponibiliza para cada user
    # mensagem que será enviada
    body=f''' - \n\nAtualização do livro Becoming de Michele Obama!\n 
    Valor atual: {valor},
    ''')

# mostrar o output para verificar se o sms foi enviado
print(message.sid)
