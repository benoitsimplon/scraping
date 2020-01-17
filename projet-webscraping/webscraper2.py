import requests
from bs4 import BeautifulSoup
from pyexcel_ods3 import save_data


def scraper(browserpage,cat,sscat,liste_scraper):
    webscraper_response = requests.get(browserpage)
    soup = BeautifulSoup(webscraper_response.content, 'html.parser')
    caption_info = soup.find_all('div',{'class': 'caption'})
    for i in range(len(caption_info)):
        liste =[]
        prix = caption_info[i].find_all('h4', {'class': 'pull-right price'})
        item = caption_info[i].find_all('a', {'class': 'title'})
        px = prix[0].text
        it = item[0].text
        liste.append(cat[1:])
        liste.append(sscat[1:])
        liste.append(it)
        liste.append(px[1:])
        liste_scraper.append(liste)




def browser_adress(webPageName,webCategory,webItemsComputers, i_cat, i_item):
    browserpage = f"{webPageName}{webCategory[i_cat]}{webItemsComputers[i_item]}"
    return browserpage


def main_programm():
    liste_scraper=[]
    webPageName = "https://www.webscraper.io/test-sites/e-commerce/allinone"
    webCategory = ("/computers","/phones")
    webItemsComputers = ("/laptops","/tablets")
    for i_cat in range(len(webCategory)):
        cat = webCategory[i_cat]
        for i_item in range(len(webItemsComputers)):
            sscat = webItemsComputers[i_item]
            if i_cat == 1:
                sscat = cat
                ad = "https://www.webscraper.io/test-sites/e-commerce/allinone/phones"
                scraper(ad,cat,sscat,liste_scraper)
                break
            else:
                ad = browser_adress(webPageName,webCategory,webItemsComputers, i_cat, i_item)
                scraper(ad,cat,sscat,liste_scraper)
    return liste_scraper


x = main_programm()

print(x)

def export_excel(x):
    data = OrderedDict
    save_data("doc_excel_ods.ods", x)

export_excel(x)