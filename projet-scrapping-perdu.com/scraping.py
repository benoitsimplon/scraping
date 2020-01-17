import requests
from bs4 import BeautifulSoup

perdu_response = requests.get("https://www.perdu.com")
#print(perdu_response.content)
soup = BeautifulSoup(perdu_response.content, 'html.parser')
print(f'BSoup has found :{soup.title.text}')
'''
.content => récupe une liste de contenu
.contents => récup ce qui se trouve entre les balises
.text => récup le texte
'''