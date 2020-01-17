import requests
import pyexcel as pe
from bs4 import BeautifulSoup

liste_scraping =[]

def scraper(browserpage,liste_scraping):
    webscraper_response = requests.get(browserpage)
    soup = BeautifulSoup(webscraper_response.content, 'html.parser')
    caption_info = soup.find_all('div',{'class': 'caption'})
    for i in range(len(caption_info)):
        dico ={}
        prix = caption_info[i].find_all('h4', {'class': 'pull-right price'})
        item = caption_info[i].find_all('a', {'class': 'title'})
        px = prix[0].text
        dico[item[0].text] = px[1:]
        liste_scraping.append(dico)
    return liste_scraping



def browser_adress(webPageName,webCategory,webItemsComputers, i_cat, i_item):
    browserpage = f"{webPageName}{webCategory[i_cat]}{webItemsComputers[i_item]}"
    return browserpage


def main_programm(liste_scraping):
    liste_scraper=[]
    webPageName = "https://www.webscraper.io/test-sites/e-commerce/allinone"
    webCategory = ("/computers","/phones")
    webItemsComputers = ("/laptops","/tablets")
    for i_cat in range(len(webCategory)):
        dico ={}
        for i_item in range(len(webItemsComputers)):
            if i_cat == 1:
                ad = "https://www.webscraper.io/test-sites/e-commerce/allinone/phones"
                liste = scraper(ad,liste_scraping)
                break
            else:
                ad = browser_adress(webPageName,webCategory,webItemsComputers, i_cat, i_item)
                liste = scraper(ad,liste_scraping)
                dico[webItemsComputers[i_item]] = liste
        dico[webCategory[i_cat]] = liste
        liste_scraper.append(liste)
    return dico_scraper


x = main_programm(liste_scraping)

print(x)
 