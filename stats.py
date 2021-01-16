from country_list import countries_for_language
import os
import requests
from shutil import copyfileobj
from strings import *

def countrylist(q):
    countries = dict(countries_for_language('en'))
    if q in countries.values():
        return api_response(q) 
    else:
        return False

def api_response(q):
    URL = os.environ.get("CURL","").format(q)
    data = requests.get(URL).json()
    flag_img(data['countryInfo']['flag'])
    return COUNTRY_DATA.format(data['country'],data['countryInfo']['iso2'],data['cases'],data['todayCases'],data['deaths'],data['todayDeaths'],data['recovered'],data['active'],data['critical'],data['casesPerOneMillion'],data['deathsPerOneMillion'],data['tests'],data['testsPerOneMillion'])


def flag_img(flag_img_url):
    img_r = requests.get(flag_img_url)
    if img_r.status_code == 200:
        with open('img.png', 'wb') as img:
            img.write(img_r.content)
    del img_r

def global_stats():
    URL = os.environ.get("GURL","")
    data = requests.get(URL).json()
    return GLOBAL_DATA.format(data['cases'],data['todayCases'],data['deaths'],data['todayDeaths'],data['recovered'],data['active'],data['critical'],data['casesPerOneMillion'],data['deathsPerOneMillion'],data['tests'],data['testsPerOneMillion'],data['affectedCountries'])
