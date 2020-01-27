import requests
import bs4
import re

found_drug_information = search_ndc_database('233215')
print(found_drug_information)

def search_ndc_database(NDC):
    url = 'https://ndclist.com/?s='
    search_url = url + NDC

    response = requests.get(search_url)
    soup = bs4.BeautifulSoup(response.text)
    
    response = []
    response.append(str(soup.findAll("td", {"data-title": "Proprietary Name"})[0]))
    response.append(str(soup.findAll("td", {"data-title": "Non-Proprietary Name"})[0]))
    response.append(str(soup.findAll("td", {"data-title": "Dosage Form"})[0]))
    response.append(str(soup.findAll("td", {"data-title": "Route Name"})[0]))
    response.append(str(soup.findAll("td", {"data-title": "Company Name"})[0]))
    response.append(str(soup.findAll("td", {"data-title": "Product Type"})[0]))
    
    clean_response = []
    for item in response:
        clean_response.append(re.findall(r"\>(.*?)\<",(str(item)))[0])
        
    return clean_response
