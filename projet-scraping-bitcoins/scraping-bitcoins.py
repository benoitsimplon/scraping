import requests
from bs4 import BeautifulSoup

cours_bitcoin_response = requests.get("https://www.boursorama.com/bourse/devises/cryptomonnaies-bitcoin-euro-BTC-EUR/")
#print(cours_bitcoin_response.content)
soup = BeautifulSoup(cours_bitcoin_response.content, 'html.parser')
print(f'BSoup has found :{soup.title.text}')
'''
.content => récupe une liste de contenu
.contents => récup ce qui se trouve entre les balises
.text => récup le texte
'''
#apres inspection de l'élément de la page boursorama on soupconne que l'info est dans
#le div facepalte_info

faceplate_info = soup.find_all('div',{'class': 'c-faceplate__info'})

# On veux savoir cb y en a

print(len(faceplate_info))

#dans faceplate_info je cherche le bon objet c-instrument

cours_eur_btc = faceplate_info[0].find_all('span', {'class': 'c-instrument'})
print(cours_eur_btc)

prix_eur_btc = cours_eur_btc[0].text
variation_eur_btc = cours_eur_btc[1].text

print(f'Le bitcoins vaut :{prix_eur_btc} euros.')
print(f'Il a varié de  :{variation_eur_btc} depuis ce matin.')
