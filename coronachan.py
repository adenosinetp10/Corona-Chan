from telegram.ext import Updater,CommandHandler,MessageHandler
import requests
import os

default_url = 'https://api.covid19api.com/'
summary_url = 'https://api.covid19api.com/summary'


default=requests.get(default_url).json()
summary=requests.get(summary_url).json()

def start(update, context):
    fname=update.message.from_user.first_name
    update.message.reply_text('Konnichiwa! '+str(fname)+' san !\nDo /help to see How to use me and commands.')
    update.message.reply_text('😄')

def global1(update,context):
    new_confirmed=(summary["Global"]["NewConfirmed"])
    total_confirmed=(summary["Global"]["TotalConfirmed"])
    new_deaths=(summary["Global"]["NewDeaths"])
    total_deaths=(summary["Global"]["TotalDeaths"])
    new_recovered=(summary["Global"]["NewRecovered"])
    total_recovered=(summary["Global"]["TotalRecovered"])
    update.message.reply_text('Corona Global Statistics\n'
                                '\nNew Confirmed : '+str(new_confirmed)+
                                '\nTotal Confirmed : '+str(total_confirmed)+
                                '\nNew Deaths : '+str(new_deaths)+
                                '\nTotal Deaths : '+str(total_deaths)+
                                '\nNew Recovered : '+str(new_recovered)+
                                '\nTotal Recovered : '+str(total_recovered))

def countrycode(update,context):
    update.message.reply_text('Available Country Codes : '
                                '\nAF-Afghanistan'
                                '\nAL-Albania'
                                '\nDZ-Algeria'
                                '\nAD-Andorra'
                                '\nAO-Angola'
                                '\nAG-Antigua and Barbuda'
                                '\nAR-Argentina'
                                '\nAM-Armenia'
                                '\nAU-Australia'
                                '\nAT-Austria'
                                '\nAZ-Azerbaijan'
                                '\nBS-Bahamas'
                                '\nBH-Bahrain'
                                '\nBD-Bangladesh'
                                '\nBB-Barbados'
                                '\nBY-Belarus'
                                '\nBE-Belgium'
                                '\nBZ-Belize'
                                '\nBJ-Benin'
                                '\nBT-Bhutan'
                                '\nBO-Bolivia'
                                '\nBA-Bosnia and Herzegovina'
                                '\nBW-Botswana'
                                '\nBR-Brazil'
                                '\nBN-Brunei Darussalam'
                                '\nBG-Bulgaria'
                                '\nBF-Burkina Faso'
                                '\nBI-Burundi'
                                '\nKH-Cambodia'
                                '\nCM-Cameroon'
                                '\nCA-Canada'
                                '\nCV-Cape Verde'
                                '\nCF-Central African Republic'
                                '\nTD-Chad'
                                '\nCL-Chile'
                                '\nCN-China'
                                '\nCO-Colombia'
                                '\nKM-Comoros'
                                '\nCG-Congo (Brazzaville)'
                                '\nCD-Congo (Kinshasa)'
                                '\nCR-Costa Rica'
                                '\nHR-Croatia'
                                '\nCU-Cuba'
                                '\nCY-Cyprus'
                                '\nCZ-Czech Republic'
                                '\nCI-Côte d\'Ivoire'
                                '\nDK-Denmark'
                                '\nDJ-Djibouti'
                                '\nDM-Dominica'
                                '\nDO-Dominican Republic'
                                '\nEC-Ecuador'
                                '\nEG-Egypt'
                                '\nSV-El Salvador'
                                '\nGQ-Equatorial Guinea'
                                '\nER-Eritrea'
                                '\nEE-Estonia'
                                '\nET-Ethiopia'
                                '\nFJ-Fiji'
                                '\nFI-Finland'
                                '\nFR-France'
                                '\nGA-Gabon'
                                '\nGM-Gambia'
                                '\nGE-Georgia'
                                '\nDE-Germany'
                                '\nGH-Ghana'
                                '\nGR-Greece'
                                '\nGD-Grenada'
                                '\nGT-Guatemala'
                                '\nGN-Guinea'
                                '\nGW-Guinea-Bissau'
                                '\nGY-Guyana'
                                '\nHT-Haiti'
                                '\nVA-Holy See (Vatican City State)'
                                '\nHN-Honduras'
                                '\nHU-Hungary'
                                '\nIS-Iceland'
                                '\nIN-India'
                                '\nID-Indonesia'
                                '\nIR-Iran, Islamic Republic of'
                                '\nIQ-Iraq'
                                '\nIE-Ireland'
                                '\nIL-Israel'
                                '\nIT-Italy'
                                '\nJM-Jamaica'
                                '\nJP-Japan'
                                '\nJO-Jordan'
                                '\nKZ-Kazakhstan'
                                '\nKE-Kenya'
                                '\nKR-Korea (South)'
                                '\nKW-Kuwait'
                                '\nKG-Kyrgyzstan'
                                '\nLA-Lao PDR'
                                '\nLV-Latvia'
                                '\nLB-Lebanon'
                                '\nLS-Lesotho'
                                '\nLR-Liberia'
                                '\nLY-Libya'
                                '\nLI-Liechtenstein'
                                '\nLT-Lithuania'
                                '\nLU-Luxembourg'
                                '\nMK-Macedonia, Republic of'
                                '\nMG-Madagascar'
                                '\nMW-Malawi'
                                '\nMY-Malaysia'
                                '\nMV-Maldives'
                                '\nML-Mali'
                                '\nMT-Malta'
                                '\nMR-Mauritania'
                                '\nMU-Mauritius'
                                '\nMX-Mexico'
                                '\nMD-Moldova'
                                '\nMC-Monaco'
                                '\nMN-Mongolia'
                                '\nME-Montenegro'
                                '\nMA-Morocco'
                                '\nMZ-Mozambique'
                                '\nMM-Myanmar'
                                '\nNA-Namibia'
                                '\nNP-Nepal'
                                '\nNL-Netherlands'
                                '\nNZ-New Zealand'
                                '\nNI-Nicaragua'
                                '\nNE-Niger'
                                '\nNG-Nigeria'
                                '\nNO-Norway'
                                '\nOM-Oman'
                                '\nPK-Pakistan'
                                '\nPS-Palestinian Territory'
                                '\nPA-Panama'
                                '\nPG-Papua New Guinea'
                                '\nPY-Paraguay'
                                '\nPE-Peru'
                                '\nPH-Philippines'
                                '\nPL-Poland'
                                '\nPT-Portugal'
                                '\nQA-Qatar'
                                '\nXK-Republic of Kosovo'
                                '\nRO-Romania'
                                '\nRU-Russian Federation'
                                '\nRW-Rwanda'
                                '\nKN-Saint Kitts and Nevis'
                                '\nLC-Saint Lucia'
                                '\nVC-Saint Vincent and Grenadines'
                                '\nSM-San Marino'
                                '\nST-Sao Tome and Principe'
                                '\nSA-Saudi Arabia'
                                '\nSN-Senegal'
                                '\nRS-Serbia'
                                '\nSC-Seychelles'
                                '\nSL-Sierra Leone'
                                '\nSG-Singapore'
                                '\nSK-Slovakia'
                                '\nSI-Slovenia'
                                '\nSO-Somalia'
                                '\nZA-South Africa'
                                '\nSS-South Sudan'
                                '\nES-Spain'
                                '\nLK-Sri Lanka'
                                '\nSD-Sudan'
                                '\nSR-Suriname'
                                '\nSZ-Swaziland'
                                '\nSE-Sweden'
                                '\nCH-Switzerland'
                                '\nSY-Syrian Arab Republic (Syria)'
                                '\nTW-Taiwan, Republic of China'
                                '\nTJ-Tajikistan'
                                '\nTZ-Tanzania, United Republic of'
                                '\nTH-Thailand'
                                '\nTL-Timor-Leste'
                                '\nTG-Togo'
                                '\nTT-Trinidad and Tobago'
                                '\nTN-Tunisia'
                                '\nTR-Turkey'
                                '\nUG-Uganda'
                                '\nUA-Ukraine'
                                '\nAE-United Arab Emirates'
                                '\nGB-United Kingdom'
                                '\nUS-United States of America'
                                '\nUY-Uruguay'
                                '\nUZ-Uzbekistan'
                                '\nVE-Venezuela (Bolivarian Republic)'
                                '\nVN-Viet Nam'
                                '\nEH-Western Sahara'
                                '\nYE-Yemen'
                                '\nZM-Zambia'
                                '\nZW-Zimbabwe')
    
def AF(update, context):
    new_confirmed_AF=(summary["Countries"][0]["NewConfirmed"])    
    total_confirmed_AF=(summary["Countries"][0]["TotalConfirmed"])
    new_deaths_AF=(summary["Countries"][0]["NewDeaths"])
    total_deaths_AF=(summary["Countries"][0]["TotalDeaths"])      
    new_recovered_AF=(summary["Countries"][0]["NewRecovered"])    
    total_recovered_AF=(summary["Countries"][0]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Afghanistan'
   '\nNew Confirmed : '+str(new_confirmed_AF)+
   '\nTotal Confirmed : '+str(total_confirmed_AF)+
   '\nNew Deaths : '+str(new_deaths_AF)+
   '\nTotal Deaths : '+str(total_deaths_AF)+
   '\nNew Recovered : '+str(new_recovered_AF)+
   '\nTotal Recovered : '+str(total_recovered_AF))

def AL(update, context):
    new_confirmed_AL=(summary["Countries"][1]["NewConfirmed"])
    total_confirmed_AL=(summary["Countries"][1]["TotalConfirmed"])
    new_deaths_AL=(summary["Countries"][1]["NewDeaths"])
    total_deaths_AL=(summary["Countries"][1]["TotalDeaths"])
    new_recovered_AL=(summary["Countries"][1]["NewRecovered"])
    total_recovered_AL=(summary["Countries"][1]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Albania'
   '\nNew Confirmed : '+str(new_confirmed_AL)+
   '\nTotal Confirmed : '+str(total_confirmed_AL)+
   '\nNew Deaths : '+str(new_deaths_AL)+
   '\nTotal Deaths : '+str(total_deaths_AL)+
   '\nNew Recovered : '+str(new_recovered_AL)+
   '\nTotal Recovered : '+str(total_recovered_AL))

def DZ(update, context):
    new_confirmed_DZ=(summary["Countries"][2]["NewConfirmed"])
    total_confirmed_DZ=(summary["Countries"][2]["TotalConfirmed"])
    new_deaths_DZ=(summary["Countries"][2]["NewDeaths"])
    total_deaths_DZ=(summary["Countries"][2]["TotalDeaths"])
    new_recovered_DZ=(summary["Countries"][2]["NewRecovered"])
    total_recovered_DZ=(summary["Countries"][2]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Algeria'
   '\nNew Confirmed : '+str(new_confirmed_DZ)+
   '\nTotal Confirmed : '+str(total_confirmed_DZ)+
   '\nNew Deaths : '+str(new_deaths_DZ)+
   '\nTotal Deaths : '+str(total_deaths_DZ)+
   '\nNew Recovered : '+str(new_recovered_DZ)+
   '\nTotal Recovered : '+str(total_recovered_DZ))

def AD(update, context):
    new_confirmed_AD=(summary["Countries"][3]["NewConfirmed"])
    total_confirmed_AD=(summary["Countries"][3]["TotalConfirmed"])
    new_deaths_AD=(summary["Countries"][3]["NewDeaths"])
    total_deaths_AD=(summary["Countries"][3]["TotalDeaths"])
    new_recovered_AD=(summary["Countries"][3]["NewRecovered"])
    total_recovered_AD=(summary["Countries"][3]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Andorra'
   '\nNew Confirmed : '+str(new_confirmed_AD)+
   '\nTotal Confirmed : '+str(total_confirmed_AD)+
   '\nNew Deaths : '+str(new_deaths_AD)+
   '\nTotal Deaths : '+str(total_deaths_AD)+
   '\nNew Recovered : '+str(new_recovered_AD)+
   '\nTotal Recovered : '+str(total_recovered_AD))

def AO(update, context):
    new_confirmed_AO=(summary["Countries"][4]["NewConfirmed"])
    total_confirmed_AO=(summary["Countries"][4]["TotalConfirmed"])
    new_deaths_AO=(summary["Countries"][4]["NewDeaths"])
    total_deaths_AO=(summary["Countries"][4]["TotalDeaths"])
    new_recovered_AO=(summary["Countries"][4]["NewRecovered"])
    total_recovered_AO=(summary["Countries"][4]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Angola'
   '\nNew Confirmed : '+str(new_confirmed_AO)+
   '\nTotal Confirmed : '+str(total_confirmed_AO)+
   '\nNew Deaths : '+str(new_deaths_AO)+
   '\nTotal Deaths : '+str(total_deaths_AO)+
   '\nNew Recovered : '+str(new_recovered_AO)+
   '\nTotal Recovered : '+str(total_recovered_AO))

def AG(update, context):
    new_confirmed_AG=(summary["Countries"][5]["NewConfirmed"])
    total_confirmed_AG=(summary["Countries"][5]["TotalConfirmed"])
    new_deaths_AG=(summary["Countries"][5]["NewDeaths"])
    total_deaths_AG=(summary["Countries"][5]["TotalDeaths"])
    new_recovered_AG=(summary["Countries"][5]["NewRecovered"])
    total_recovered_AG=(summary["Countries"][5]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Antigua and Barbuda'
   '\nNew Confirmed : '+str(new_confirmed_AG)+
   '\nTotal Confirmed : '+str(total_confirmed_AG)+
   '\nNew Deaths : '+str(new_deaths_AG)+
   '\nTotal Deaths : '+str(total_deaths_AG)+
   '\nNew Recovered : '+str(new_recovered_AG)+
   '\nTotal Recovered : '+str(total_recovered_AG))

def AR(update, context):
    new_confirmed_AR=(summary["Countries"][6]["NewConfirmed"])
    total_confirmed_AR=(summary["Countries"][6]["TotalConfirmed"])
    new_deaths_AR=(summary["Countries"][6]["NewDeaths"])
    total_deaths_AR=(summary["Countries"][6]["TotalDeaths"])
    new_recovered_AR=(summary["Countries"][6]["NewRecovered"])
    total_recovered_AR=(summary["Countries"][6]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Argentina'
   '\nNew Confirmed : '+str(new_confirmed_AR)+
   '\nTotal Confirmed : '+str(total_confirmed_AR)+
   '\nNew Deaths : '+str(new_deaths_AR)+
   '\nTotal Deaths : '+str(total_deaths_AR)+
   '\nNew Recovered : '+str(new_recovered_AR)+
   '\nTotal Recovered : '+str(total_recovered_AR))

def AM(update, context):
    new_confirmed_AM=(summary["Countries"][7]["NewConfirmed"])
    total_confirmed_AM=(summary["Countries"][7]["TotalConfirmed"])
    new_deaths_AM=(summary["Countries"][7]["NewDeaths"])
    total_deaths_AM=(summary["Countries"][7]["TotalDeaths"])
    new_recovered_AM=(summary["Countries"][7]["NewRecovered"])
    total_recovered_AM=(summary["Countries"][7]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Armenia'
   '\nNew Confirmed : '+str(new_confirmed_AM)+
   '\nTotal Confirmed : '+str(total_confirmed_AM)+
   '\nNew Deaths : '+str(new_deaths_AM)+
   '\nTotal Deaths : '+str(total_deaths_AM)+
   '\nNew Recovered : '+str(new_recovered_AM)+
   '\nTotal Recovered : '+str(total_recovered_AM))

def AU(update, context):
    new_confirmed_AU=(summary["Countries"][8]["NewConfirmed"])
    total_confirmed_AU=(summary["Countries"][8]["TotalConfirmed"])
    new_deaths_AU=(summary["Countries"][8]["NewDeaths"])
    total_deaths_AU=(summary["Countries"][8]["TotalDeaths"])
    new_recovered_AU=(summary["Countries"][8]["NewRecovered"])
    total_recovered_AU=(summary["Countries"][8]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Australia'
   '\nNew Confirmed : '+str(new_confirmed_AU)+
   '\nTotal Confirmed : '+str(total_confirmed_AU)+
   '\nNew Deaths : '+str(new_deaths_AU)+
   '\nTotal Deaths : '+str(total_deaths_AU)+
   '\nNew Recovered : '+str(new_recovered_AU)+
   '\nTotal Recovered : '+str(total_recovered_AU))

def AT(update, context):
    new_confirmed_AT=(summary["Countries"][9]["NewConfirmed"])
    total_confirmed_AT=(summary["Countries"][9]["TotalConfirmed"])
    new_deaths_AT=(summary["Countries"][9]["NewDeaths"])
    total_deaths_AT=(summary["Countries"][9]["TotalDeaths"])
    new_recovered_AT=(summary["Countries"][9]["NewRecovered"])
    total_recovered_AT=(summary["Countries"][9]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Austria'
   '\nNew Confirmed : '+str(new_confirmed_AT)+
   '\nTotal Confirmed : '+str(total_confirmed_AT)+
   '\nNew Deaths : '+str(new_deaths_AT)+
   '\nTotal Deaths : '+str(total_deaths_AT)+
   '\nNew Recovered : '+str(new_recovered_AT)+
   '\nTotal Recovered : '+str(total_recovered_AT))

def AZ(update, context):
    new_confirmed_AZ=(summary["Countries"][10]["NewConfirmed"])
    total_confirmed_AZ=(summary["Countries"][10]["TotalConfirmed"])
    new_deaths_AZ=(summary["Countries"][10]["NewDeaths"])
    total_deaths_AZ=(summary["Countries"][10]["TotalDeaths"])
    new_recovered_AZ=(summary["Countries"][10]["NewRecovered"])
    total_recovered_AZ=(summary["Countries"][10]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Azerbaijan'
   '\nNew Confirmed : '+str(new_confirmed_AZ)+
   '\nTotal Confirmed : '+str(total_confirmed_AZ)+
   '\nNew Deaths : '+str(new_deaths_AZ)+
   '\nTotal Deaths : '+str(total_deaths_AZ)+
   '\nNew Recovered : '+str(new_recovered_AZ)+
   '\nTotal Recovered : '+str(total_recovered_AZ))

def BS(update, context):
    new_confirmed_BS=(summary["Countries"][11]["NewConfirmed"])
    total_confirmed_BS=(summary["Countries"][11]["TotalConfirmed"])
    new_deaths_BS=(summary["Countries"][11]["NewDeaths"])
    total_deaths_BS=(summary["Countries"][11]["TotalDeaths"])
    new_recovered_BS=(summary["Countries"][11]["NewRecovered"])
    total_recovered_BS=(summary["Countries"][11]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Bahamas'
   '\nNew Confirmed : '+str(new_confirmed_BS)+
   '\nTotal Confirmed : '+str(total_confirmed_BS)+
   '\nNew Deaths : '+str(new_deaths_BS)+
   '\nTotal Deaths : '+str(total_deaths_BS)+
   '\nNew Recovered : '+str(new_recovered_BS)+
   '\nTotal Recovered : '+str(total_recovered_BS))

def BH(update, context):
    new_confirmed_BH=(summary["Countries"][12]["NewConfirmed"])
    total_confirmed_BH=(summary["Countries"][12]["TotalConfirmed"])
    new_deaths_BH=(summary["Countries"][12]["NewDeaths"])
    total_deaths_BH=(summary["Countries"][12]["TotalDeaths"])
    new_recovered_BH=(summary["Countries"][12]["NewRecovered"])
    total_recovered_BH=(summary["Countries"][12]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Bahrain'
   '\nNew Confirmed : '+str(new_confirmed_BH)+
   '\nTotal Confirmed : '+str(total_confirmed_BH)+
   '\nNew Deaths : '+str(new_deaths_BH)+
   '\nTotal Deaths : '+str(total_deaths_BH)+
   '\nNew Recovered : '+str(new_recovered_BH)+
   '\nTotal Recovered : '+str(total_recovered_BH))

def BD(update, context):
    new_confirmed_BD=(summary["Countries"][13]["NewConfirmed"])
    total_confirmed_BD=(summary["Countries"][13]["TotalConfirmed"])
    new_deaths_BD=(summary["Countries"][13]["NewDeaths"])
    total_deaths_BD=(summary["Countries"][13]["TotalDeaths"])
    new_recovered_BD=(summary["Countries"][13]["NewRecovered"])
    total_recovered_BD=(summary["Countries"][13]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Bangladesh'
   '\nNew Confirmed : '+str(new_confirmed_BD)+
   '\nTotal Confirmed : '+str(total_confirmed_BD)+
   '\nNew Deaths : '+str(new_deaths_BD)+
   '\nTotal Deaths : '+str(total_deaths_BD)+
   '\nNew Recovered : '+str(new_recovered_BD)+
   '\nTotal Recovered : '+str(total_recovered_BD))

def BB(update, context):
    new_confirmed_BB=(summary["Countries"][14]["NewConfirmed"])
    total_confirmed_BB=(summary["Countries"][14]["TotalConfirmed"])
    new_deaths_BB=(summary["Countries"][14]["NewDeaths"])
    total_deaths_BB=(summary["Countries"][14]["TotalDeaths"])
    new_recovered_BB=(summary["Countries"][14]["NewRecovered"])
    total_recovered_BB=(summary["Countries"][14]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Barbados'
   '\nNew Confirmed : '+str(new_confirmed_BB)+
   '\nTotal Confirmed : '+str(total_confirmed_BB)+
   '\nNew Deaths : '+str(new_deaths_BB)+
   '\nTotal Deaths : '+str(total_deaths_BB)+
   '\nNew Recovered : '+str(new_recovered_BB)+
   '\nTotal Recovered : '+str(total_recovered_BB))

def BY(update, context):
    new_confirmed_BY=(summary["Countries"][15]["NewConfirmed"])
    total_confirmed_BY=(summary["Countries"][15]["TotalConfirmed"])
    new_deaths_BY=(summary["Countries"][15]["NewDeaths"])
    total_deaths_BY=(summary["Countries"][15]["TotalDeaths"])
    new_recovered_BY=(summary["Countries"][15]["NewRecovered"])
    total_recovered_BY=(summary["Countries"][15]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Belarus'
   '\nNew Confirmed : '+str(new_confirmed_BY)+
   '\nTotal Confirmed : '+str(total_confirmed_BY)+
   '\nNew Deaths : '+str(new_deaths_BY)+
   '\nTotal Deaths : '+str(total_deaths_BY)+
   '\nNew Recovered : '+str(new_recovered_BY)+
   '\nTotal Recovered : '+str(total_recovered_BY))

def BE(update, context):
    new_confirmed_BE=(summary["Countries"][16]["NewConfirmed"])
    total_confirmed_BE=(summary["Countries"][16]["TotalConfirmed"])
    new_deaths_BE=(summary["Countries"][16]["NewDeaths"])
    total_deaths_BE=(summary["Countries"][16]["TotalDeaths"])
    new_recovered_BE=(summary["Countries"][16]["NewRecovered"])
    total_recovered_BE=(summary["Countries"][16]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Belgium'
   '\nNew Confirmed : '+str(new_confirmed_BE)+
   '\nTotal Confirmed : '+str(total_confirmed_BE)+
   '\nNew Deaths : '+str(new_deaths_BE)+
   '\nTotal Deaths : '+str(total_deaths_BE)+
   '\nNew Recovered : '+str(new_recovered_BE)+
   '\nTotal Recovered : '+str(total_recovered_BE))

def BZ(update, context):
    new_confirmed_BZ=(summary["Countries"][17]["NewConfirmed"])
    total_confirmed_BZ=(summary["Countries"][17]["TotalConfirmed"])
    new_deaths_BZ=(summary["Countries"][17]["NewDeaths"])
    total_deaths_BZ=(summary["Countries"][17]["TotalDeaths"])
    new_recovered_BZ=(summary["Countries"][17]["NewRecovered"])
    total_recovered_BZ=(summary["Countries"][17]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Belize'
   '\nNew Confirmed : '+str(new_confirmed_BZ)+
   '\nTotal Confirmed : '+str(total_confirmed_BZ)+
   '\nNew Deaths : '+str(new_deaths_BZ)+
   '\nTotal Deaths : '+str(total_deaths_BZ)+
   '\nNew Recovered : '+str(new_recovered_BZ)+
   '\nTotal Recovered : '+str(total_recovered_BZ))

def BJ(update, context):
    new_confirmed_BJ=(summary["Countries"][18]["NewConfirmed"])
    total_confirmed_BJ=(summary["Countries"][18]["TotalConfirmed"])
    new_deaths_BJ=(summary["Countries"][18]["NewDeaths"])
    total_deaths_BJ=(summary["Countries"][18]["TotalDeaths"])
    new_recovered_BJ=(summary["Countries"][18]["NewRecovered"])
    total_recovered_BJ=(summary["Countries"][18]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Benin'
   '\nNew Confirmed : '+str(new_confirmed_BJ)+
   '\nTotal Confirmed : '+str(total_confirmed_BJ)+
   '\nNew Deaths : '+str(new_deaths_BJ)+
   '\nTotal Deaths : '+str(total_deaths_BJ)+
   '\nNew Recovered : '+str(new_recovered_BJ)+
   '\nTotal Recovered : '+str(total_recovered_BJ))

def BT(update, context):
    new_confirmed_BT=(summary["Countries"][19]["NewConfirmed"])
    total_confirmed_BT=(summary["Countries"][19]["TotalConfirmed"])
    new_deaths_BT=(summary["Countries"][19]["NewDeaths"])
    total_deaths_BT=(summary["Countries"][19]["TotalDeaths"])
    new_recovered_BT=(summary["Countries"][19]["NewRecovered"])
    total_recovered_BT=(summary["Countries"][19]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Bhutan'
   '\nNew Confirmed : '+str(new_confirmed_BT)+
   '\nTotal Confirmed : '+str(total_confirmed_BT)+
   '\nNew Deaths : '+str(new_deaths_BT)+
   '\nTotal Deaths : '+str(total_deaths_BT)+
   '\nNew Recovered : '+str(new_recovered_BT)+
   '\nTotal Recovered : '+str(total_recovered_BT))

def BO(update, context):
    new_confirmed_BO=(summary["Countries"][20]["NewConfirmed"])
    total_confirmed_BO=(summary["Countries"][20]["TotalConfirmed"])
    new_deaths_BO=(summary["Countries"][20]["NewDeaths"])
    total_deaths_BO=(summary["Countries"][20]["TotalDeaths"])
    new_recovered_BO=(summary["Countries"][20]["NewRecovered"])
    total_recovered_BO=(summary["Countries"][20]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Bolivia'
   '\nNew Confirmed : '+str(new_confirmed_BO)+
   '\nTotal Confirmed : '+str(total_confirmed_BO)+
   '\nNew Deaths : '+str(new_deaths_BO)+
   '\nTotal Deaths : '+str(total_deaths_BO)+
   '\nNew Recovered : '+str(new_recovered_BO)+
   '\nTotal Recovered : '+str(total_recovered_BO))

def BA(update, context):
    new_confirmed_BA=(summary["Countries"][21]["NewConfirmed"])
    total_confirmed_BA=(summary["Countries"][21]["TotalConfirmed"])
    new_deaths_BA=(summary["Countries"][21]["NewDeaths"])
    total_deaths_BA=(summary["Countries"][21]["TotalDeaths"])
    new_recovered_BA=(summary["Countries"][21]["NewRecovered"])
    total_recovered_BA=(summary["Countries"][21]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Bosnia and Herzegovina'
   '\nNew Confirmed : '+str(new_confirmed_BA)+
   '\nTotal Confirmed : '+str(total_confirmed_BA)+
   '\nNew Deaths : '+str(new_deaths_BA)+
   '\nTotal Deaths : '+str(total_deaths_BA)+
   '\nNew Recovered : '+str(new_recovered_BA)+
   '\nTotal Recovered : '+str(total_recovered_BA))

def BW(update, context):
    new_confirmed_BW=(summary["Countries"][22]["NewConfirmed"])
    total_confirmed_BW=(summary["Countries"][22]["TotalConfirmed"])
    new_deaths_BW=(summary["Countries"][22]["NewDeaths"])
    total_deaths_BW=(summary["Countries"][22]["TotalDeaths"])
    new_recovered_BW=(summary["Countries"][22]["NewRecovered"])
    total_recovered_BW=(summary["Countries"][22]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Botswana'
   '\nNew Confirmed : '+str(new_confirmed_BW)+
   '\nTotal Confirmed : '+str(total_confirmed_BW)+
   '\nNew Deaths : '+str(new_deaths_BW)+
   '\nTotal Deaths : '+str(total_deaths_BW)+
   '\nNew Recovered : '+str(new_recovered_BW)+
   '\nTotal Recovered : '+str(total_recovered_BW))

def BR(update, context):
    new_confirmed_BR=(summary["Countries"][23]["NewConfirmed"])
    total_confirmed_BR=(summary["Countries"][23]["TotalConfirmed"])
    new_deaths_BR=(summary["Countries"][23]["NewDeaths"])
    total_deaths_BR=(summary["Countries"][23]["TotalDeaths"])
    new_recovered_BR=(summary["Countries"][23]["NewRecovered"])
    total_recovered_BR=(summary["Countries"][23]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Brazil'
   '\nNew Confirmed : '+str(new_confirmed_BR)+
   '\nTotal Confirmed : '+str(total_confirmed_BR)+
   '\nNew Deaths : '+str(new_deaths_BR)+
   '\nTotal Deaths : '+str(total_deaths_BR)+
   '\nNew Recovered : '+str(new_recovered_BR)+
   '\nTotal Recovered : '+str(total_recovered_BR))

def BN(update, context):
    new_confirmed_BN=(summary["Countries"][24]["NewConfirmed"])
    total_confirmed_BN=(summary["Countries"][24]["TotalConfirmed"])
    new_deaths_BN=(summary["Countries"][24]["NewDeaths"])
    total_deaths_BN=(summary["Countries"][24]["TotalDeaths"])
    new_recovered_BN=(summary["Countries"][24]["NewRecovered"])
    total_recovered_BN=(summary["Countries"][24]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Brunei Darussalam'
   '\nNew Confirmed : '+str(new_confirmed_BN)+
   '\nTotal Confirmed : '+str(total_confirmed_BN)+
   '\nNew Deaths : '+str(new_deaths_BN)+
   '\nTotal Deaths : '+str(total_deaths_BN)+
   '\nNew Recovered : '+str(new_recovered_BN)+
   '\nTotal Recovered : '+str(total_recovered_BN))

def BG(update, context):
    new_confirmed_BG=(summary["Countries"][25]["NewConfirmed"])
    total_confirmed_BG=(summary["Countries"][25]["TotalConfirmed"])
    new_deaths_BG=(summary["Countries"][25]["NewDeaths"])
    total_deaths_BG=(summary["Countries"][25]["TotalDeaths"])
    new_recovered_BG=(summary["Countries"][25]["NewRecovered"])
    total_recovered_BG=(summary["Countries"][25]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Bulgaria'
   '\nNew Confirmed : '+str(new_confirmed_BG)+
   '\nTotal Confirmed : '+str(total_confirmed_BG)+
   '\nNew Deaths : '+str(new_deaths_BG)+
   '\nTotal Deaths : '+str(total_deaths_BG)+
   '\nNew Recovered : '+str(new_recovered_BG)+
   '\nTotal Recovered : '+str(total_recovered_BG))

def BF(update, context):
    new_confirmed_BF=(summary["Countries"][26]["NewConfirmed"])
    total_confirmed_BF=(summary["Countries"][26]["TotalConfirmed"])
    new_deaths_BF=(summary["Countries"][26]["NewDeaths"])
    total_deaths_BF=(summary["Countries"][26]["TotalDeaths"])
    new_recovered_BF=(summary["Countries"][26]["NewRecovered"])
    total_recovered_BF=(summary["Countries"][26]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Burkina Faso'
   '\nNew Confirmed : '+str(new_confirmed_BF)+
   '\nTotal Confirmed : '+str(total_confirmed_BF)+
   '\nNew Deaths : '+str(new_deaths_BF)+
   '\nTotal Deaths : '+str(total_deaths_BF)+
   '\nNew Recovered : '+str(new_recovered_BF)+
   '\nTotal Recovered : '+str(total_recovered_BF))

def BI(update, context):
    new_confirmed_BI=(summary["Countries"][27]["NewConfirmed"])
    total_confirmed_BI=(summary["Countries"][27]["TotalConfirmed"])
    new_deaths_BI=(summary["Countries"][27]["NewDeaths"])
    total_deaths_BI=(summary["Countries"][27]["TotalDeaths"])
    new_recovered_BI=(summary["Countries"][27]["NewRecovered"])
    total_recovered_BI=(summary["Countries"][27]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Burundi'
   '\nNew Confirmed : '+str(new_confirmed_BI)+
   '\nTotal Confirmed : '+str(total_confirmed_BI)+
   '\nNew Deaths : '+str(new_deaths_BI)+
   '\nTotal Deaths : '+str(total_deaths_BI)+
   '\nNew Recovered : '+str(new_recovered_BI)+
   '\nTotal Recovered : '+str(total_recovered_BI))

def KH(update, context):
    new_confirmed_KH=(summary["Countries"][28]["NewConfirmed"])
    total_confirmed_KH=(summary["Countries"][28]["TotalConfirmed"])
    new_deaths_KH=(summary["Countries"][28]["NewDeaths"])
    total_deaths_KH=(summary["Countries"][28]["TotalDeaths"])
    new_recovered_KH=(summary["Countries"][28]["NewRecovered"])
    total_recovered_KH=(summary["Countries"][28]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Cambodia'
   '\nNew Confirmed : '+str(new_confirmed_KH)+
   '\nTotal Confirmed : '+str(total_confirmed_KH)+
   '\nNew Deaths : '+str(new_deaths_KH)+
   '\nTotal Deaths : '+str(total_deaths_KH)+
   '\nNew Recovered : '+str(new_recovered_KH)+
   '\nTotal Recovered : '+str(total_recovered_KH))

def CM(update, context):
    new_confirmed_CM=(summary["Countries"][29]["NewConfirmed"])
    total_confirmed_CM=(summary["Countries"][29]["TotalConfirmed"])
    new_deaths_CM=(summary["Countries"][29]["NewDeaths"])
    total_deaths_CM=(summary["Countries"][29]["TotalDeaths"])
    new_recovered_CM=(summary["Countries"][29]["NewRecovered"])
    total_recovered_CM=(summary["Countries"][29]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Cameroon'
   '\nNew Confirmed : '+str(new_confirmed_CM)+
   '\nTotal Confirmed : '+str(total_confirmed_CM)+
   '\nNew Deaths : '+str(new_deaths_CM)+
   '\nTotal Deaths : '+str(total_deaths_CM)+
   '\nNew Recovered : '+str(new_recovered_CM)+
   '\nTotal Recovered : '+str(total_recovered_CM))

def CA(update, context):
    new_confirmed_CA=(summary["Countries"][30]["NewConfirmed"])
    total_confirmed_CA=(summary["Countries"][30]["TotalConfirmed"])
    new_deaths_CA=(summary["Countries"][30]["NewDeaths"])
    total_deaths_CA=(summary["Countries"][30]["TotalDeaths"])
    new_recovered_CA=(summary["Countries"][30]["NewRecovered"])
    total_recovered_CA=(summary["Countries"][30]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Canada'
   '\nNew Confirmed : '+str(new_confirmed_CA)+
   '\nTotal Confirmed : '+str(total_confirmed_CA)+
   '\nNew Deaths : '+str(new_deaths_CA)+
   '\nTotal Deaths : '+str(total_deaths_CA)+
   '\nNew Recovered : '+str(new_recovered_CA)+
   '\nTotal Recovered : '+str(total_recovered_CA))

def CV(update, context):
    new_confirmed_CV=(summary["Countries"][31]["NewConfirmed"])
    total_confirmed_CV=(summary["Countries"][31]["TotalConfirmed"])
    new_deaths_CV=(summary["Countries"][31]["NewDeaths"])
    total_deaths_CV=(summary["Countries"][31]["TotalDeaths"])
    new_recovered_CV=(summary["Countries"][31]["NewRecovered"])
    total_recovered_CV=(summary["Countries"][31]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Cape Verde'
   '\nNew Confirmed : '+str(new_confirmed_CV)+
   '\nTotal Confirmed : '+str(total_confirmed_CV)+
   '\nNew Deaths : '+str(new_deaths_CV)+
   '\nTotal Deaths : '+str(total_deaths_CV)+
   '\nNew Recovered : '+str(new_recovered_CV)+
   '\nTotal Recovered : '+str(total_recovered_CV))

def CF(update, context):
    new_confirmed_CF=(summary["Countries"][32]["NewConfirmed"])
    total_confirmed_CF=(summary["Countries"][32]["TotalConfirmed"])
    new_deaths_CF=(summary["Countries"][32]["NewDeaths"])
    total_deaths_CF=(summary["Countries"][32]["TotalDeaths"])
    new_recovered_CF=(summary["Countries"][32]["NewRecovered"])
    total_recovered_CF=(summary["Countries"][32]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Central African Republic'
   '\nNew Confirmed : '+str(new_confirmed_CF)+
   '\nTotal Confirmed : '+str(total_confirmed_CF)+
   '\nNew Deaths : '+str(new_deaths_CF)+
   '\nTotal Deaths : '+str(total_deaths_CF)+
   '\nNew Recovered : '+str(new_recovered_CF)+
   '\nTotal Recovered : '+str(total_recovered_CF))

def TD(update, context):
    new_confirmed_TD=(summary["Countries"][33]["NewConfirmed"])
    total_confirmed_TD=(summary["Countries"][33]["TotalConfirmed"])
    new_deaths_TD=(summary["Countries"][33]["NewDeaths"])
    total_deaths_TD=(summary["Countries"][33]["TotalDeaths"])
    new_recovered_TD=(summary["Countries"][33]["NewRecovered"])
    total_recovered_TD=(summary["Countries"][33]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Chad'
   '\nNew Confirmed : '+str(new_confirmed_TD)+
   '\nTotal Confirmed : '+str(total_confirmed_TD)+
   '\nNew Deaths : '+str(new_deaths_TD)+
   '\nTotal Deaths : '+str(total_deaths_TD)+
   '\nNew Recovered : '+str(new_recovered_TD)+
   '\nTotal Recovered : '+str(total_recovered_TD))

def CL(update, context):
    new_confirmed_CL=(summary["Countries"][34]["NewConfirmed"])
    total_confirmed_CL=(summary["Countries"][34]["TotalConfirmed"])
    new_deaths_CL=(summary["Countries"][34]["NewDeaths"])
    total_deaths_CL=(summary["Countries"][34]["TotalDeaths"])
    new_recovered_CL=(summary["Countries"][34]["NewRecovered"])
    total_recovered_CL=(summary["Countries"][34]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Chile'
   '\nNew Confirmed : '+str(new_confirmed_CL)+
   '\nTotal Confirmed : '+str(total_confirmed_CL)+
   '\nNew Deaths : '+str(new_deaths_CL)+
   '\nTotal Deaths : '+str(total_deaths_CL)+
   '\nNew Recovered : '+str(new_recovered_CL)+
   '\nTotal Recovered : '+str(total_recovered_CL))

def CN(update, context):
    new_confirmed_CN=(summary["Countries"][35]["NewConfirmed"])
    total_confirmed_CN=(summary["Countries"][35]["TotalConfirmed"])
    new_deaths_CN=(summary["Countries"][35]["NewDeaths"])
    total_deaths_CN=(summary["Countries"][35]["TotalDeaths"])
    new_recovered_CN=(summary["Countries"][35]["NewRecovered"])
    total_recovered_CN=(summary["Countries"][35]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': China'
   '\nNew Confirmed : '+str(new_confirmed_CN)+
   '\nTotal Confirmed : '+str(total_confirmed_CN)+
   '\nNew Deaths : '+str(new_deaths_CN)+
   '\nTotal Deaths : '+str(total_deaths_CN)+
   '\nNew Recovered : '+str(new_recovered_CN)+
   '\nTotal Recovered : '+str(total_recovered_CN))

def CO(update, context):
    new_confirmed_CO=(summary["Countries"][36]["NewConfirmed"])
    total_confirmed_CO=(summary["Countries"][36]["TotalConfirmed"])
    new_deaths_CO=(summary["Countries"][36]["NewDeaths"])
    total_deaths_CO=(summary["Countries"][36]["TotalDeaths"])
    new_recovered_CO=(summary["Countries"][36]["NewRecovered"])
    total_recovered_CO=(summary["Countries"][36]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Colombia'
   '\nNew Confirmed : '+str(new_confirmed_CO)+
   '\nTotal Confirmed : '+str(total_confirmed_CO)+
   '\nNew Deaths : '+str(new_deaths_CO)+
   '\nTotal Deaths : '+str(total_deaths_CO)+
   '\nNew Recovered : '+str(new_recovered_CO)+
   '\nTotal Recovered : '+str(total_recovered_CO))

def KM(update, context):
    new_confirmed_KM=(summary["Countries"][37]["NewConfirmed"])
    total_confirmed_KM=(summary["Countries"][37]["TotalConfirmed"])
    new_deaths_KM=(summary["Countries"][37]["NewDeaths"])
    total_deaths_KM=(summary["Countries"][37]["TotalDeaths"])
    new_recovered_KM=(summary["Countries"][37]["NewRecovered"])
    total_recovered_KM=(summary["Countries"][37]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Comoros'
   '\nNew Confirmed : '+str(new_confirmed_KM)+
   '\nTotal Confirmed : '+str(total_confirmed_KM)+
   '\nNew Deaths : '+str(new_deaths_KM)+
   '\nTotal Deaths : '+str(total_deaths_KM)+
   '\nNew Recovered : '+str(new_recovered_KM)+
   '\nTotal Recovered : '+str(total_recovered_KM))

def CG(update, context):
    new_confirmed_CG=(summary["Countries"][38]["NewConfirmed"])
    total_confirmed_CG=(summary["Countries"][38]["TotalConfirmed"])
    new_deaths_CG=(summary["Countries"][38]["NewDeaths"])
    total_deaths_CG=(summary["Countries"][38]["TotalDeaths"])
    new_recovered_CG=(summary["Countries"][38]["NewRecovered"])
    total_recovered_CG=(summary["Countries"][38]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Congo (Brazzaville)'
   '\nNew Confirmed : '+str(new_confirmed_CG)+
   '\nTotal Confirmed : '+str(total_confirmed_CG)+
   '\nNew Deaths : '+str(new_deaths_CG)+
   '\nTotal Deaths : '+str(total_deaths_CG)+
   '\nNew Recovered : '+str(new_recovered_CG)+
   '\nTotal Recovered : '+str(total_recovered_CG))

def CD(update, context):
    new_confirmed_CD=(summary["Countries"][39]["NewConfirmed"])
    total_confirmed_CD=(summary["Countries"][39]["TotalConfirmed"])
    new_deaths_CD=(summary["Countries"][39]["NewDeaths"])
    total_deaths_CD=(summary["Countries"][39]["TotalDeaths"])
    new_recovered_CD=(summary["Countries"][39]["NewRecovered"])
    total_recovered_CD=(summary["Countries"][39]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Congo (Kinshasa)'
   '\nNew Confirmed : '+str(new_confirmed_CD)+
   '\nTotal Confirmed : '+str(total_confirmed_CD)+
   '\nNew Deaths : '+str(new_deaths_CD)+
   '\nTotal Deaths : '+str(total_deaths_CD)+
   '\nNew Recovered : '+str(new_recovered_CD)+
   '\nTotal Recovered : '+str(total_recovered_CD))

def CR(update, context):
    new_confirmed_CR=(summary["Countries"][40]["NewConfirmed"])
    total_confirmed_CR=(summary["Countries"][40]["TotalConfirmed"])
    new_deaths_CR=(summary["Countries"][40]["NewDeaths"])
    total_deaths_CR=(summary["Countries"][40]["TotalDeaths"])
    new_recovered_CR=(summary["Countries"][40]["NewRecovered"])
    total_recovered_CR=(summary["Countries"][40]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Costa Rica'
   '\nNew Confirmed : '+str(new_confirmed_CR)+
   '\nTotal Confirmed : '+str(total_confirmed_CR)+
   '\nNew Deaths : '+str(new_deaths_CR)+
   '\nTotal Deaths : '+str(total_deaths_CR)+
   '\nNew Recovered : '+str(new_recovered_CR)+
   '\nTotal Recovered : '+str(total_recovered_CR))

def HR(update, context):
    new_confirmed_HR=(summary["Countries"][41]["NewConfirmed"])
    total_confirmed_HR=(summary["Countries"][41]["TotalConfirmed"])
    new_deaths_HR=(summary["Countries"][41]["NewDeaths"])
    total_deaths_HR=(summary["Countries"][41]["TotalDeaths"])
    new_recovered_HR=(summary["Countries"][41]["NewRecovered"])
    total_recovered_HR=(summary["Countries"][41]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Croatia'
   '\nNew Confirmed : '+str(new_confirmed_HR)+
   '\nTotal Confirmed : '+str(total_confirmed_HR)+
   '\nNew Deaths : '+str(new_deaths_HR)+
   '\nTotal Deaths : '+str(total_deaths_HR)+
   '\nNew Recovered : '+str(new_recovered_HR)+
   '\nTotal Recovered : '+str(total_recovered_HR))

def CU(update, context):
    new_confirmed_CU=(summary["Countries"][42]["NewConfirmed"])
    total_confirmed_CU=(summary["Countries"][42]["TotalConfirmed"])
    new_deaths_CU=(summary["Countries"][42]["NewDeaths"])
    total_deaths_CU=(summary["Countries"][42]["TotalDeaths"])
    new_recovered_CU=(summary["Countries"][42]["NewRecovered"])
    total_recovered_CU=(summary["Countries"][42]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Cuba'
   '\nNew Confirmed : '+str(new_confirmed_CU)+
   '\nTotal Confirmed : '+str(total_confirmed_CU)+
   '\nNew Deaths : '+str(new_deaths_CU)+
   '\nTotal Deaths : '+str(total_deaths_CU)+
   '\nNew Recovered : '+str(new_recovered_CU)+
   '\nTotal Recovered : '+str(total_recovered_CU))

def CY(update, context):
    new_confirmed_CY=(summary["Countries"][43]["NewConfirmed"])
    total_confirmed_CY=(summary["Countries"][43]["TotalConfirmed"])
    new_deaths_CY=(summary["Countries"][43]["NewDeaths"])
    total_deaths_CY=(summary["Countries"][43]["TotalDeaths"])
    new_recovered_CY=(summary["Countries"][43]["NewRecovered"])
    total_recovered_CY=(summary["Countries"][43]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Cyprus'
   '\nNew Confirmed : '+str(new_confirmed_CY)+
   '\nTotal Confirmed : '+str(total_confirmed_CY)+
   '\nNew Deaths : '+str(new_deaths_CY)+
   '\nTotal Deaths : '+str(total_deaths_CY)+
   '\nNew Recovered : '+str(new_recovered_CY)+
   '\nTotal Recovered : '+str(total_recovered_CY))

def CZ(update, context):
    new_confirmed_CZ=(summary["Countries"][44]["NewConfirmed"])
    total_confirmed_CZ=(summary["Countries"][44]["TotalConfirmed"])
    new_deaths_CZ=(summary["Countries"][44]["NewDeaths"])
    total_deaths_CZ=(summary["Countries"][44]["TotalDeaths"])
    new_recovered_CZ=(summary["Countries"][44]["NewRecovered"])
    total_recovered_CZ=(summary["Countries"][44]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Czech Republic'
   '\nNew Confirmed : '+str(new_confirmed_CZ)+
   '\nTotal Confirmed : '+str(total_confirmed_CZ)+
   '\nNew Deaths : '+str(new_deaths_CZ)+
   '\nTotal Deaths : '+str(total_deaths_CZ)+
   '\nNew Recovered : '+str(new_recovered_CZ)+
   '\nTotal Recovered : '+str(total_recovered_CZ))

def CI(update, context):
    new_confirmed_CI=(summary["Countries"][45]["NewConfirmed"])
    total_confirmed_CI=(summary["Countries"][45]["TotalConfirmed"])
    new_deaths_CI=(summary["Countries"][45]["NewDeaths"])
    total_deaths_CI=(summary["Countries"][45]["TotalDeaths"])
    new_recovered_CI=(summary["Countries"][45]["NewRecovered"])
    total_recovered_CI=(summary["Countries"][45]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Côte d\'Ivoire'
   '\nNew Confirmed : '+str(new_confirmed_CI)+
   '\nTotal Confirmed : '+str(total_confirmed_CI)+
   '\nNew Deaths : '+str(new_deaths_CI)+
   '\nTotal Deaths : '+str(total_deaths_CI)+
   '\nNew Recovered : '+str(new_recovered_CI)+
   '\nTotal Recovered : '+str(total_recovered_CI))

def DK(update, context):
    new_confirmed_DK=(summary["Countries"][46]["NewConfirmed"])
    total_confirmed_DK=(summary["Countries"][46]["TotalConfirmed"])
    new_deaths_DK=(summary["Countries"][46]["NewDeaths"])
    total_deaths_DK=(summary["Countries"][46]["TotalDeaths"])
    new_recovered_DK=(summary["Countries"][46]["NewRecovered"])
    total_recovered_DK=(summary["Countries"][46]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Denmark'
   '\nNew Confirmed : '+str(new_confirmed_DK)+
   '\nTotal Confirmed : '+str(total_confirmed_DK)+
   '\nNew Deaths : '+str(new_deaths_DK)+
   '\nTotal Deaths : '+str(total_deaths_DK)+
   '\nNew Recovered : '+str(new_recovered_DK)+
   '\nTotal Recovered : '+str(total_recovered_DK))

def DJ(update, context):
    new_confirmed_DJ=(summary["Countries"][47]["NewConfirmed"])
    total_confirmed_DJ=(summary["Countries"][47]["TotalConfirmed"])
    new_deaths_DJ=(summary["Countries"][47]["NewDeaths"])
    total_deaths_DJ=(summary["Countries"][47]["TotalDeaths"])
    new_recovered_DJ=(summary["Countries"][47]["NewRecovered"])
    total_recovered_DJ=(summary["Countries"][47]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Djibouti'
   '\nNew Confirmed : '+str(new_confirmed_DJ)+
   '\nTotal Confirmed : '+str(total_confirmed_DJ)+
   '\nNew Deaths : '+str(new_deaths_DJ)+
   '\nTotal Deaths : '+str(total_deaths_DJ)+
   '\nNew Recovered : '+str(new_recovered_DJ)+
   '\nTotal Recovered : '+str(total_recovered_DJ))

def DM(update, context):
    new_confirmed_DM=(summary["Countries"][48]["NewConfirmed"])
    total_confirmed_DM=(summary["Countries"][48]["TotalConfirmed"])
    new_deaths_DM=(summary["Countries"][48]["NewDeaths"])
    total_deaths_DM=(summary["Countries"][48]["TotalDeaths"])
    new_recovered_DM=(summary["Countries"][48]["NewRecovered"])
    total_recovered_DM=(summary["Countries"][48]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Dominica'
   '\nNew Confirmed : '+str(new_confirmed_DM)+
   '\nTotal Confirmed : '+str(total_confirmed_DM)+
   '\nNew Deaths : '+str(new_deaths_DM)+
   '\nTotal Deaths : '+str(total_deaths_DM)+
   '\nNew Recovered : '+str(new_recovered_DM)+
   '\nTotal Recovered : '+str(total_recovered_DM))

def DO(update, context):
    new_confirmed_DO=(summary["Countries"][49]["NewConfirmed"])
    total_confirmed_DO=(summary["Countries"][49]["TotalConfirmed"])
    new_deaths_DO=(summary["Countries"][49]["NewDeaths"])
    total_deaths_DO=(summary["Countries"][49]["TotalDeaths"])
    new_recovered_DO=(summary["Countries"][49]["NewRecovered"])
    total_recovered_DO=(summary["Countries"][49]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Dominican Republic'
   '\nNew Confirmed : '+str(new_confirmed_DO)+
   '\nTotal Confirmed : '+str(total_confirmed_DO)+
   '\nNew Deaths : '+str(new_deaths_DO)+
   '\nTotal Deaths : '+str(total_deaths_DO)+
   '\nNew Recovered : '+str(new_recovered_DO)+
   '\nTotal Recovered : '+str(total_recovered_DO)) 

def EC(update, context):
    new_confirmed_EC=(summary["Countries"][50]["NewConfirmed"])    
    total_confirmed_EC=(summary["Countries"][50]["TotalConfirmed"])
    new_deaths_EC=(summary["Countries"][50]["NewDeaths"])
    total_deaths_EC=(summary["Countries"][50]["TotalDeaths"])      
    new_recovered_EC=(summary["Countries"][50]["NewRecovered"])    
    total_recovered_EC=(summary["Countries"][50]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Ecuador'
   '\nNew Confirmed : '+str(new_confirmed_EC)+
   '\nTotal Confirmed : '+str(total_confirmed_EC)+
   '\nNew Deaths : '+str(new_deaths_EC)+
   '\nTotal Deaths : '+str(total_deaths_EC)+
   '\nNew Recovered : '+str(new_recovered_EC)+
   '\nTotal Recovered : '+str(total_recovered_EC))

def EG(update, context):
    new_confirmed_EG=(summary["Countries"][51]["NewConfirmed"])
    total_confirmed_EG=(summary["Countries"][51]["TotalConfirmed"])
    new_deaths_EG=(summary["Countries"][51]["NewDeaths"])
    total_deaths_EG=(summary["Countries"][51]["TotalDeaths"])
    new_recovered_EG=(summary["Countries"][51]["NewRecovered"])
    total_recovered_EG=(summary["Countries"][51]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Egypt'
   '\nNew Confirmed : '+str(new_confirmed_EG)+
   '\nTotal Confirmed : '+str(total_confirmed_EG)+
   '\nNew Deaths : '+str(new_deaths_EG)+
   '\nTotal Deaths : '+str(total_deaths_EG)+
   '\nNew Recovered : '+str(new_recovered_EG)+
   '\nTotal Recovered : '+str(total_recovered_EG))

def SV(update, context):
    new_confirmed_SV=(summary["Countries"][52]["NewConfirmed"])
    total_confirmed_SV=(summary["Countries"][52]["TotalConfirmed"])
    new_deaths_SV=(summary["Countries"][52]["NewDeaths"])
    total_deaths_SV=(summary["Countries"][52]["TotalDeaths"])
    new_recovered_SV=(summary["Countries"][52]["NewRecovered"])
    total_recovered_SV=(summary["Countries"][52]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': El Salvador'
   '\nNew Confirmed : '+str(new_confirmed_SV)+
   '\nTotal Confirmed : '+str(total_confirmed_SV)+
   '\nNew Deaths : '+str(new_deaths_SV)+
   '\nTotal Deaths : '+str(total_deaths_SV)+
   '\nNew Recovered : '+str(new_recovered_SV)+
   '\nTotal Recovered : '+str(total_recovered_SV))

def GQ(update, context):
    new_confirmed_GQ=(summary["Countries"][53]["NewConfirmed"])
    total_confirmed_GQ=(summary["Countries"][53]["TotalConfirmed"])
    new_deaths_GQ=(summary["Countries"][53]["NewDeaths"])
    total_deaths_GQ=(summary["Countries"][53]["TotalDeaths"])
    new_recovered_GQ=(summary["Countries"][53]["NewRecovered"])
    total_recovered_GQ=(summary["Countries"][53]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Equatorial Guinea'
   '\nNew Confirmed : '+str(new_confirmed_GQ)+
   '\nTotal Confirmed : '+str(total_confirmed_GQ)+
   '\nNew Deaths : '+str(new_deaths_GQ)+
   '\nTotal Deaths : '+str(total_deaths_GQ)+
   '\nNew Recovered : '+str(new_recovered_GQ)+
   '\nTotal Recovered : '+str(total_recovered_GQ))

def ER(update, context):
    new_confirmed_ER=(summary["Countries"][54]["NewConfirmed"])
    total_confirmed_ER=(summary["Countries"][54]["TotalConfirmed"])
    new_deaths_ER=(summary["Countries"][54]["NewDeaths"])
    total_deaths_ER=(summary["Countries"][54]["TotalDeaths"])
    new_recovered_ER=(summary["Countries"][54]["NewRecovered"])
    total_recovered_ER=(summary["Countries"][54]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Eritrea'
   '\nNew Confirmed : '+str(new_confirmed_ER)+
   '\nTotal Confirmed : '+str(total_confirmed_ER)+
   '\nNew Deaths : '+str(new_deaths_ER)+
   '\nTotal Deaths : '+str(total_deaths_ER)+
   '\nNew Recovered : '+str(new_recovered_ER)+
   '\nTotal Recovered : '+str(total_recovered_ER))

def EE(update, context):
    new_confirmed_EE=(summary["Countries"][55]["NewConfirmed"])
    total_confirmed_EE=(summary["Countries"][55]["TotalConfirmed"])
    new_deaths_EE=(summary["Countries"][55]["NewDeaths"])
    total_deaths_EE=(summary["Countries"][55]["TotalDeaths"])
    new_recovered_EE=(summary["Countries"][55]["NewRecovered"])
    total_recovered_EE=(summary["Countries"][55]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Estonia'
   '\nNew Confirmed : '+str(new_confirmed_EE)+
   '\nTotal Confirmed : '+str(total_confirmed_EE)+
   '\nNew Deaths : '+str(new_deaths_EE)+
   '\nTotal Deaths : '+str(total_deaths_EE)+
   '\nNew Recovered : '+str(new_recovered_EE)+
   '\nTotal Recovered : '+str(total_recovered_EE))

def ET(update, context):
    new_confirmed_ET=(summary["Countries"][56]["NewConfirmed"])
    total_confirmed_ET=(summary["Countries"][56]["TotalConfirmed"])
    new_deaths_ET=(summary["Countries"][56]["NewDeaths"])
    total_deaths_ET=(summary["Countries"][56]["TotalDeaths"])
    new_recovered_ET=(summary["Countries"][56]["NewRecovered"])
    total_recovered_ET=(summary["Countries"][56]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Ethiopia'
   '\nNew Confirmed : '+str(new_confirmed_ET)+
   '\nTotal Confirmed : '+str(total_confirmed_ET)+
   '\nNew Deaths : '+str(new_deaths_ET)+
   '\nTotal Deaths : '+str(total_deaths_ET)+
   '\nNew Recovered : '+str(new_recovered_ET)+
   '\nTotal Recovered : '+str(total_recovered_ET))

def FJ(update, context):
    new_confirmed_FJ=(summary["Countries"][57]["NewConfirmed"])
    total_confirmed_FJ=(summary["Countries"][57]["TotalConfirmed"])
    new_deaths_FJ=(summary["Countries"][57]["NewDeaths"])
    total_deaths_FJ=(summary["Countries"][57]["TotalDeaths"])
    new_recovered_FJ=(summary["Countries"][57]["NewRecovered"])
    total_recovered_FJ=(summary["Countries"][57]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Fiji'
   '\nNew Confirmed : '+str(new_confirmed_FJ)+
   '\nTotal Confirmed : '+str(total_confirmed_FJ)+
   '\nNew Deaths : '+str(new_deaths_FJ)+
   '\nTotal Deaths : '+str(total_deaths_FJ)+
   '\nNew Recovered : '+str(new_recovered_FJ)+
   '\nTotal Recovered : '+str(total_recovered_FJ))

def FI(update, context):
    new_confirmed_FI=(summary["Countries"][58]["NewConfirmed"])
    total_confirmed_FI=(summary["Countries"][58]["TotalConfirmed"])
    new_deaths_FI=(summary["Countries"][58]["NewDeaths"])
    total_deaths_FI=(summary["Countries"][58]["TotalDeaths"])
    new_recovered_FI=(summary["Countries"][58]["NewRecovered"])
    total_recovered_FI=(summary["Countries"][58]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Finland'
   '\nNew Confirmed : '+str(new_confirmed_FI)+
   '\nTotal Confirmed : '+str(total_confirmed_FI)+
   '\nNew Deaths : '+str(new_deaths_FI)+
   '\nTotal Deaths : '+str(total_deaths_FI)+
   '\nNew Recovered : '+str(new_recovered_FI)+
   '\nTotal Recovered : '+str(total_recovered_FI))

def FR(update, context):
    new_confirmed_FR=(summary["Countries"][59]["NewConfirmed"])
    total_confirmed_FR=(summary["Countries"][59]["TotalConfirmed"])
    new_deaths_FR=(summary["Countries"][59]["NewDeaths"])
    total_deaths_FR=(summary["Countries"][59]["TotalDeaths"])
    new_recovered_FR=(summary["Countries"][59]["NewRecovered"])
    total_recovered_FR=(summary["Countries"][59]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': France'
   '\nNew Confirmed : '+str(new_confirmed_FR)+
   '\nTotal Confirmed : '+str(total_confirmed_FR)+
   '\nNew Deaths : '+str(new_deaths_FR)+
   '\nTotal Deaths : '+str(total_deaths_FR)+
   '\nNew Recovered : '+str(new_recovered_FR)+
   '\nTotal Recovered : '+str(total_recovered_FR))

def GA(update, context):
    new_confirmed_GA=(summary["Countries"][60]["NewConfirmed"])
    total_confirmed_GA=(summary["Countries"][60]["TotalConfirmed"])
    new_deaths_GA=(summary["Countries"][60]["NewDeaths"])
    total_deaths_GA=(summary["Countries"][60]["TotalDeaths"])
    new_recovered_GA=(summary["Countries"][60]["NewRecovered"])
    total_recovered_GA=(summary["Countries"][60]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Gabon'
   '\nNew Confirmed : '+str(new_confirmed_GA)+
   '\nTotal Confirmed : '+str(total_confirmed_GA)+
   '\nNew Deaths : '+str(new_deaths_GA)+
   '\nTotal Deaths : '+str(total_deaths_GA)+
   '\nNew Recovered : '+str(new_recovered_GA)+
   '\nTotal Recovered : '+str(total_recovered_GA))

def GM(update, context):
    new_confirmed_GM=(summary["Countries"][61]["NewConfirmed"])
    total_confirmed_GM=(summary["Countries"][61]["TotalConfirmed"])
    new_deaths_GM=(summary["Countries"][61]["NewDeaths"])
    total_deaths_GM=(summary["Countries"][61]["TotalDeaths"])
    new_recovered_GM=(summary["Countries"][61]["NewRecovered"])
    total_recovered_GM=(summary["Countries"][61]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Gambia'
   '\nNew Confirmed : '+str(new_confirmed_GM)+
   '\nTotal Confirmed : '+str(total_confirmed_GM)+
   '\nNew Deaths : '+str(new_deaths_GM)+
   '\nTotal Deaths : '+str(total_deaths_GM)+
   '\nNew Recovered : '+str(new_recovered_GM)+
   '\nTotal Recovered : '+str(total_recovered_GM))

def GE(update, context):
    new_confirmed_GE=(summary["Countries"][62]["NewConfirmed"])
    total_confirmed_GE=(summary["Countries"][62]["TotalConfirmed"])
    new_deaths_GE=(summary["Countries"][62]["NewDeaths"])
    total_deaths_GE=(summary["Countries"][62]["TotalDeaths"])
    new_recovered_GE=(summary["Countries"][62]["NewRecovered"])
    total_recovered_GE=(summary["Countries"][62]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Georgia'
   '\nNew Confirmed : '+str(new_confirmed_GE)+
   '\nTotal Confirmed : '+str(total_confirmed_GE)+
   '\nNew Deaths : '+str(new_deaths_GE)+
   '\nTotal Deaths : '+str(total_deaths_GE)+
   '\nNew Recovered : '+str(new_recovered_GE)+
   '\nTotal Recovered : '+str(total_recovered_GE))

def DE(update, context):
    new_confirmed_DE=(summary["Countries"][63]["NewConfirmed"])
    total_confirmed_DE=(summary["Countries"][63]["TotalConfirmed"])
    new_deaths_DE=(summary["Countries"][63]["NewDeaths"])
    total_deaths_DE=(summary["Countries"][63]["TotalDeaths"])
    new_recovered_DE=(summary["Countries"][63]["NewRecovered"])
    total_recovered_DE=(summary["Countries"][63]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Germany'
   '\nNew Confirmed : '+str(new_confirmed_DE)+
   '\nTotal Confirmed : '+str(total_confirmed_DE)+
   '\nNew Deaths : '+str(new_deaths_DE)+
   '\nTotal Deaths : '+str(total_deaths_DE)+
   '\nNew Recovered : '+str(new_recovered_DE)+
   '\nTotal Recovered : '+str(total_recovered_DE))

def GH(update, context):
    new_confirmed_GH=(summary["Countries"][64]["NewConfirmed"])
    total_confirmed_GH=(summary["Countries"][64]["TotalConfirmed"])
    new_deaths_GH=(summary["Countries"][64]["NewDeaths"])
    total_deaths_GH=(summary["Countries"][64]["TotalDeaths"])
    new_recovered_GH=(summary["Countries"][64]["NewRecovered"])
    total_recovered_GH=(summary["Countries"][64]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Ghana'
   '\nNew Confirmed : '+str(new_confirmed_GH)+
   '\nTotal Confirmed : '+str(total_confirmed_GH)+
   '\nNew Deaths : '+str(new_deaths_GH)+
   '\nTotal Deaths : '+str(total_deaths_GH)+
   '\nNew Recovered : '+str(new_recovered_GH)+
   '\nTotal Recovered : '+str(total_recovered_GH))

def GR(update, context):
    new_confirmed_GR=(summary["Countries"][65]["NewConfirmed"])
    total_confirmed_GR=(summary["Countries"][65]["TotalConfirmed"])
    new_deaths_GR=(summary["Countries"][65]["NewDeaths"])
    total_deaths_GR=(summary["Countries"][65]["TotalDeaths"])
    new_recovered_GR=(summary["Countries"][65]["NewRecovered"])
    total_recovered_GR=(summary["Countries"][65]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Greece'
   '\nNew Confirmed : '+str(new_confirmed_GR)+
   '\nTotal Confirmed : '+str(total_confirmed_GR)+
   '\nNew Deaths : '+str(new_deaths_GR)+
   '\nTotal Deaths : '+str(total_deaths_GR)+
   '\nNew Recovered : '+str(new_recovered_GR)+
   '\nTotal Recovered : '+str(total_recovered_GR))

def GD(update, context):
    new_confirmed_GD=(summary["Countries"][66]["NewConfirmed"])
    total_confirmed_GD=(summary["Countries"][66]["TotalConfirmed"])
    new_deaths_GD=(summary["Countries"][66]["NewDeaths"])
    total_deaths_GD=(summary["Countries"][66]["TotalDeaths"])
    new_recovered_GD=(summary["Countries"][66]["NewRecovered"])
    total_recovered_GD=(summary["Countries"][66]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Grenada'
   '\nNew Confirmed : '+str(new_confirmed_GD)+
   '\nTotal Confirmed : '+str(total_confirmed_GD)+
   '\nNew Deaths : '+str(new_deaths_GD)+
   '\nTotal Deaths : '+str(total_deaths_GD)+
   '\nNew Recovered : '+str(new_recovered_GD)+
   '\nTotal Recovered : '+str(total_recovered_GD))

def GT(update, context):
    new_confirmed_GT=(summary["Countries"][67]["NewConfirmed"])
    total_confirmed_GT=(summary["Countries"][67]["TotalConfirmed"])
    new_deaths_GT=(summary["Countries"][67]["NewDeaths"])
    total_deaths_GT=(summary["Countries"][67]["TotalDeaths"])
    new_recovered_GT=(summary["Countries"][67]["NewRecovered"])
    total_recovered_GT=(summary["Countries"][67]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Guatemala'
   '\nNew Confirmed : '+str(new_confirmed_GT)+
   '\nTotal Confirmed : '+str(total_confirmed_GT)+
   '\nNew Deaths : '+str(new_deaths_GT)+
   '\nTotal Deaths : '+str(total_deaths_GT)+
   '\nNew Recovered : '+str(new_recovered_GT)+
   '\nTotal Recovered : '+str(total_recovered_GT))

def GN(update, context):
    new_confirmed_GN=(summary["Countries"][68]["NewConfirmed"])
    total_confirmed_GN=(summary["Countries"][68]["TotalConfirmed"])
    new_deaths_GN=(summary["Countries"][68]["NewDeaths"])
    total_deaths_GN=(summary["Countries"][68]["TotalDeaths"])
    new_recovered_GN=(summary["Countries"][68]["NewRecovered"])
    total_recovered_GN=(summary["Countries"][68]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Guinea'
   '\nNew Confirmed : '+str(new_confirmed_GN)+
   '\nTotal Confirmed : '+str(total_confirmed_GN)+
   '\nNew Deaths : '+str(new_deaths_GN)+
   '\nTotal Deaths : '+str(total_deaths_GN)+
   '\nNew Recovered : '+str(new_recovered_GN)+
   '\nTotal Recovered : '+str(total_recovered_GN))

def GW(update, context):
    new_confirmed_GW=(summary["Countries"][69]["NewConfirmed"])
    total_confirmed_GW=(summary["Countries"][69]["TotalConfirmed"])
    new_deaths_GW=(summary["Countries"][69]["NewDeaths"])
    total_deaths_GW=(summary["Countries"][69]["TotalDeaths"])
    new_recovered_GW=(summary["Countries"][69]["NewRecovered"])
    total_recovered_GW=(summary["Countries"][69]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Guinea-Bissau'
   '\nNew Confirmed : '+str(new_confirmed_GW)+
   '\nTotal Confirmed : '+str(total_confirmed_GW)+
   '\nNew Deaths : '+str(new_deaths_GW)+
   '\nTotal Deaths : '+str(total_deaths_GW)+
   '\nNew Recovered : '+str(new_recovered_GW)+
   '\nTotal Recovered : '+str(total_recovered_GW))

def GY(update, context):
    new_confirmed_GY=(summary["Countries"][70]["NewConfirmed"])
    total_confirmed_GY=(summary["Countries"][70]["TotalConfirmed"])
    new_deaths_GY=(summary["Countries"][70]["NewDeaths"])
    total_deaths_GY=(summary["Countries"][70]["TotalDeaths"])
    new_recovered_GY=(summary["Countries"][70]["NewRecovered"])
    total_recovered_GY=(summary["Countries"][70]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Guyana'
   '\nNew Confirmed : '+str(new_confirmed_GY)+
   '\nTotal Confirmed : '+str(total_confirmed_GY)+
   '\nNew Deaths : '+str(new_deaths_GY)+
   '\nTotal Deaths : '+str(total_deaths_GY)+
   '\nNew Recovered : '+str(new_recovered_GY)+
   '\nTotal Recovered : '+str(total_recovered_GY))

def HT(update, context):
    new_confirmed_HT=(summary["Countries"][71]["NewConfirmed"])
    total_confirmed_HT=(summary["Countries"][71]["TotalConfirmed"])
    new_deaths_HT=(summary["Countries"][71]["NewDeaths"])
    total_deaths_HT=(summary["Countries"][71]["TotalDeaths"])
    new_recovered_HT=(summary["Countries"][71]["NewRecovered"])
    total_recovered_HT=(summary["Countries"][71]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Haiti'
   '\nNew Confirmed : '+str(new_confirmed_HT)+
   '\nTotal Confirmed : '+str(total_confirmed_HT)+
   '\nNew Deaths : '+str(new_deaths_HT)+
   '\nTotal Deaths : '+str(total_deaths_HT)+
   '\nNew Recovered : '+str(new_recovered_HT)+
   '\nTotal Recovered : '+str(total_recovered_HT))

def VA(update, context):
    new_confirmed_VA=(summary["Countries"][72]["NewConfirmed"])
    total_confirmed_VA=(summary["Countries"][72]["TotalConfirmed"])
    new_deaths_VA=(summary["Countries"][72]["NewDeaths"])
    total_deaths_VA=(summary["Countries"][72]["TotalDeaths"])
    new_recovered_VA=(summary["Countries"][72]["NewRecovered"])
    total_recovered_VA=(summary["Countries"][72]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Holy See (Vatican City State)'
   '\nNew Confirmed : '+str(new_confirmed_VA)+
   '\nTotal Confirmed : '+str(total_confirmed_VA)+
   '\nNew Deaths : '+str(new_deaths_VA)+
   '\nTotal Deaths : '+str(total_deaths_VA)+
   '\nNew Recovered : '+str(new_recovered_VA)+
   '\nTotal Recovered : '+str(total_recovered_VA))

def HN(update, context):
    new_confirmed_HN=(summary["Countries"][73]["NewConfirmed"])
    total_confirmed_HN=(summary["Countries"][73]["TotalConfirmed"])
    new_deaths_HN=(summary["Countries"][73]["NewDeaths"])
    total_deaths_HN=(summary["Countries"][73]["TotalDeaths"])
    new_recovered_HN=(summary["Countries"][73]["NewRecovered"])
    total_recovered_HN=(summary["Countries"][73]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Honduras'
   '\nNew Confirmed : '+str(new_confirmed_HN)+
   '\nTotal Confirmed : '+str(total_confirmed_HN)+
   '\nNew Deaths : '+str(new_deaths_HN)+
   '\nTotal Deaths : '+str(total_deaths_HN)+
   '\nNew Recovered : '+str(new_recovered_HN)+
   '\nTotal Recovered : '+str(total_recovered_HN))

def HU(update, context):
    new_confirmed_HU=(summary["Countries"][74]["NewConfirmed"])
    total_confirmed_HU=(summary["Countries"][74]["TotalConfirmed"])
    new_deaths_HU=(summary["Countries"][74]["NewDeaths"])
    total_deaths_HU=(summary["Countries"][74]["TotalDeaths"])
    new_recovered_HU=(summary["Countries"][74]["NewRecovered"])
    total_recovered_HU=(summary["Countries"][74]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Hungary'
   '\nNew Confirmed : '+str(new_confirmed_HU)+
   '\nTotal Confirmed : '+str(total_confirmed_HU)+
   '\nNew Deaths : '+str(new_deaths_HU)+
   '\nTotal Deaths : '+str(total_deaths_HU)+
   '\nNew Recovered : '+str(new_recovered_HU)+
   '\nTotal Recovered : '+str(total_recovered_HU))

def IS(update, context):
    new_confirmed_IS=(summary["Countries"][75]["NewConfirmed"])
    total_confirmed_IS=(summary["Countries"][75]["TotalConfirmed"])
    new_deaths_IS=(summary["Countries"][75]["NewDeaths"])
    total_deaths_IS=(summary["Countries"][75]["TotalDeaths"])
    new_recovered_IS=(summary["Countries"][75]["NewRecovered"])
    total_recovered_IS=(summary["Countries"][75]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Iceland'
   '\nNew Confirmed : '+str(new_confirmed_IS)+
   '\nTotal Confirmed : '+str(total_confirmed_IS)+
   '\nNew Deaths : '+str(new_deaths_IS)+
   '\nTotal Deaths : '+str(total_deaths_IS)+
   '\nNew Recovered : '+str(new_recovered_IS)+
   '\nTotal Recovered : '+str(total_recovered_IS))

def IN(update, context):
    new_confirmed_IN=(summary["Countries"][76]["NewConfirmed"])
    total_confirmed_IN=(summary["Countries"][76]["TotalConfirmed"])
    new_deaths_IN=(summary["Countries"][76]["NewDeaths"])
    total_deaths_IN=(summary["Countries"][76]["TotalDeaths"])
    new_recovered_IN=(summary["Countries"][76]["NewRecovered"])
    total_recovered_IN=(summary["Countries"][76]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': India'
   '\nNew Confirmed : '+str(new_confirmed_IN)+
   '\nTotal Confirmed : '+str(total_confirmed_IN)+
   '\nNew Deaths : '+str(new_deaths_IN)+
   '\nTotal Deaths : '+str(total_deaths_IN)+
   '\nNew Recovered : '+str(new_recovered_IN)+
   '\nTotal Recovered : '+str(total_recovered_IN))

def ID(update, context):
    new_confirmed_ID=(summary["Countries"][77]["NewConfirmed"])
    total_confirmed_ID=(summary["Countries"][77]["TotalConfirmed"])
    new_deaths_ID=(summary["Countries"][77]["NewDeaths"])
    total_deaths_ID=(summary["Countries"][77]["TotalDeaths"])
    new_recovered_ID=(summary["Countries"][77]["NewRecovered"])
    total_recovered_ID=(summary["Countries"][77]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Indonesia'
   '\nNew Confirmed : '+str(new_confirmed_ID)+
   '\nTotal Confirmed : '+str(total_confirmed_ID)+
   '\nNew Deaths : '+str(new_deaths_ID)+
   '\nTotal Deaths : '+str(total_deaths_ID)+
   '\nNew Recovered : '+str(new_recovered_ID)+
   '\nTotal Recovered : '+str(total_recovered_ID))

def IR(update, context):
    new_confirmed_IR=(summary["Countries"][78]["NewConfirmed"])
    total_confirmed_IR=(summary["Countries"][78]["TotalConfirmed"])
    new_deaths_IR=(summary["Countries"][78]["NewDeaths"])
    total_deaths_IR=(summary["Countries"][78]["TotalDeaths"])
    new_recovered_IR=(summary["Countries"][78]["NewRecovered"])
    total_recovered_IR=(summary["Countries"][78]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Iran, Islamic Republic of'
   '\nNew Confirmed : '+str(new_confirmed_IR)+
   '\nTotal Confirmed : '+str(total_confirmed_IR)+
   '\nNew Deaths : '+str(new_deaths_IR)+
   '\nTotal Deaths : '+str(total_deaths_IR)+
   '\nNew Recovered : '+str(new_recovered_IR)+
   '\nTotal Recovered : '+str(total_recovered_IR))

def IQ(update, context):
    new_confirmed_IQ=(summary["Countries"][79]["NewConfirmed"])
    total_confirmed_IQ=(summary["Countries"][79]["TotalConfirmed"])
    new_deaths_IQ=(summary["Countries"][79]["NewDeaths"])
    total_deaths_IQ=(summary["Countries"][79]["TotalDeaths"])
    new_recovered_IQ=(summary["Countries"][79]["NewRecovered"])
    total_recovered_IQ=(summary["Countries"][79]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Iraq'
   '\nNew Confirmed : '+str(new_confirmed_IQ)+
   '\nTotal Confirmed : '+str(total_confirmed_IQ)+
   '\nNew Deaths : '+str(new_deaths_IQ)+
   '\nTotal Deaths : '+str(total_deaths_IQ)+
   '\nNew Recovered : '+str(new_recovered_IQ)+
   '\nTotal Recovered : '+str(total_recovered_IQ))

def IE(update, context):
    new_confirmed_IE=(summary["Countries"][80]["NewConfirmed"])
    total_confirmed_IE=(summary["Countries"][80]["TotalConfirmed"])
    new_deaths_IE=(summary["Countries"][80]["NewDeaths"])
    total_deaths_IE=(summary["Countries"][80]["TotalDeaths"])
    new_recovered_IE=(summary["Countries"][80]["NewRecovered"])
    total_recovered_IE=(summary["Countries"][80]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Ireland'
   '\nNew Confirmed : '+str(new_confirmed_IE)+
   '\nTotal Confirmed : '+str(total_confirmed_IE)+
   '\nNew Deaths : '+str(new_deaths_IE)+
   '\nTotal Deaths : '+str(total_deaths_IE)+
   '\nNew Recovered : '+str(new_recovered_IE)+
   '\nTotal Recovered : '+str(total_recovered_IE))

def IL(update, context):
    new_confirmed_IL=(summary["Countries"][81]["NewConfirmed"])
    total_confirmed_IL=(summary["Countries"][81]["TotalConfirmed"])
    new_deaths_IL=(summary["Countries"][81]["NewDeaths"])
    total_deaths_IL=(summary["Countries"][81]["TotalDeaths"])
    new_recovered_IL=(summary["Countries"][81]["NewRecovered"])
    total_recovered_IL=(summary["Countries"][81]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Israel'
   '\nNew Confirmed : '+str(new_confirmed_IL)+
   '\nTotal Confirmed : '+str(total_confirmed_IL)+
   '\nNew Deaths : '+str(new_deaths_IL)+
   '\nTotal Deaths : '+str(total_deaths_IL)+
   '\nNew Recovered : '+str(new_recovered_IL)+
   '\nTotal Recovered : '+str(total_recovered_IL))

def IT(update, context):
    new_confirmed_IT=(summary["Countries"][82]["NewConfirmed"])
    total_confirmed_IT=(summary["Countries"][82]["TotalConfirmed"])
    new_deaths_IT=(summary["Countries"][82]["NewDeaths"])
    total_deaths_IT=(summary["Countries"][82]["TotalDeaths"])
    new_recovered_IT=(summary["Countries"][82]["NewRecovered"])
    total_recovered_IT=(summary["Countries"][82]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Italy'
   '\nNew Confirmed : '+str(new_confirmed_IT)+
   '\nTotal Confirmed : '+str(total_confirmed_IT)+
   '\nNew Deaths : '+str(new_deaths_IT)+
   '\nTotal Deaths : '+str(total_deaths_IT)+
   '\nNew Recovered : '+str(new_recovered_IT)+
   '\nTotal Recovered : '+str(total_recovered_IT))

def JM(update, context):
    new_confirmed_JM=(summary["Countries"][83]["NewConfirmed"])
    total_confirmed_JM=(summary["Countries"][83]["TotalConfirmed"])
    new_deaths_JM=(summary["Countries"][83]["NewDeaths"])
    total_deaths_JM=(summary["Countries"][83]["TotalDeaths"])
    new_recovered_JM=(summary["Countries"][83]["NewRecovered"])
    total_recovered_JM=(summary["Countries"][83]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Jamaica'
   '\nNew Confirmed : '+str(new_confirmed_JM)+
   '\nTotal Confirmed : '+str(total_confirmed_JM)+
   '\nNew Deaths : '+str(new_deaths_JM)+
   '\nTotal Deaths : '+str(total_deaths_JM)+
   '\nNew Recovered : '+str(new_recovered_JM)+
   '\nTotal Recovered : '+str(total_recovered_JM))

def JP(update, context):
    new_confirmed_JP=(summary["Countries"][84]["NewConfirmed"])
    total_confirmed_JP=(summary["Countries"][84]["TotalConfirmed"])
    new_deaths_JP=(summary["Countries"][84]["NewDeaths"])
    total_deaths_JP=(summary["Countries"][84]["TotalDeaths"])
    new_recovered_JP=(summary["Countries"][84]["NewRecovered"])
    total_recovered_JP=(summary["Countries"][84]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Japan'
   '\nNew Confirmed : '+str(new_confirmed_JP)+
   '\nTotal Confirmed : '+str(total_confirmed_JP)+
   '\nNew Deaths : '+str(new_deaths_JP)+
   '\nTotal Deaths : '+str(total_deaths_JP)+
   '\nNew Recovered : '+str(new_recovered_JP)+
   '\nTotal Recovered : '+str(total_recovered_JP))

def JO(update, context):
    new_confirmed_JO=(summary["Countries"][85]["NewConfirmed"])
    total_confirmed_JO=(summary["Countries"][85]["TotalConfirmed"])
    new_deaths_JO=(summary["Countries"][85]["NewDeaths"])
    total_deaths_JO=(summary["Countries"][85]["TotalDeaths"])
    new_recovered_JO=(summary["Countries"][85]["NewRecovered"])
    total_recovered_JO=(summary["Countries"][85]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Jordan'
   '\nNew Confirmed : '+str(new_confirmed_JO)+
   '\nTotal Confirmed : '+str(total_confirmed_JO)+
   '\nNew Deaths : '+str(new_deaths_JO)+
   '\nTotal Deaths : '+str(total_deaths_JO)+
   '\nNew Recovered : '+str(new_recovered_JO)+
   '\nTotal Recovered : '+str(total_recovered_JO))

def KZ(update, context):
    new_confirmed_KZ=(summary["Countries"][86]["NewConfirmed"])
    total_confirmed_KZ=(summary["Countries"][86]["TotalConfirmed"])
    new_deaths_KZ=(summary["Countries"][86]["NewDeaths"])
    total_deaths_KZ=(summary["Countries"][86]["TotalDeaths"])
    new_recovered_KZ=(summary["Countries"][86]["NewRecovered"])
    total_recovered_KZ=(summary["Countries"][86]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Kazakhstan'
   '\nNew Confirmed : '+str(new_confirmed_KZ)+
   '\nTotal Confirmed : '+str(total_confirmed_KZ)+
   '\nNew Deaths : '+str(new_deaths_KZ)+
   '\nTotal Deaths : '+str(total_deaths_KZ)+
   '\nNew Recovered : '+str(new_recovered_KZ)+
   '\nTotal Recovered : '+str(total_recovered_KZ))

def KE(update, context):
    new_confirmed_KE=(summary["Countries"][87]["NewConfirmed"])
    total_confirmed_KE=(summary["Countries"][87]["TotalConfirmed"])
    new_deaths_KE=(summary["Countries"][87]["NewDeaths"])
    total_deaths_KE=(summary["Countries"][87]["TotalDeaths"])
    new_recovered_KE=(summary["Countries"][87]["NewRecovered"])
    total_recovered_KE=(summary["Countries"][87]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Kenya'
   '\nNew Confirmed : '+str(new_confirmed_KE)+
   '\nTotal Confirmed : '+str(total_confirmed_KE)+
   '\nNew Deaths : '+str(new_deaths_KE)+
   '\nTotal Deaths : '+str(total_deaths_KE)+
   '\nNew Recovered : '+str(new_recovered_KE)+
   '\nTotal Recovered : '+str(total_recovered_KE))

def KR(update, context):
    new_confirmed_KR=(summary["Countries"][88]["NewConfirmed"])
    total_confirmed_KR=(summary["Countries"][88]["TotalConfirmed"])
    new_deaths_KR=(summary["Countries"][88]["NewDeaths"])
    total_deaths_KR=(summary["Countries"][88]["TotalDeaths"])
    new_recovered_KR=(summary["Countries"][88]["NewRecovered"])
    total_recovered_KR=(summary["Countries"][88]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Korea (South)'
   '\nNew Confirmed : '+str(new_confirmed_KR)+
   '\nTotal Confirmed : '+str(total_confirmed_KR)+
   '\nNew Deaths : '+str(new_deaths_KR)+
   '\nTotal Deaths : '+str(total_deaths_KR)+
   '\nNew Recovered : '+str(new_recovered_KR)+
   '\nTotal Recovered : '+str(total_recovered_KR))

def KW(update, context):
    new_confirmed_KW=(summary["Countries"][89]["NewConfirmed"])
    total_confirmed_KW=(summary["Countries"][89]["TotalConfirmed"])
    new_deaths_KW=(summary["Countries"][89]["NewDeaths"])
    total_deaths_KW=(summary["Countries"][89]["TotalDeaths"])
    new_recovered_KW=(summary["Countries"][89]["NewRecovered"])
    total_recovered_KW=(summary["Countries"][89]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Kuwait'
   '\nNew Confirmed : '+str(new_confirmed_KW)+
   '\nTotal Confirmed : '+str(total_confirmed_KW)+
   '\nNew Deaths : '+str(new_deaths_KW)+
   '\nTotal Deaths : '+str(total_deaths_KW)+
   '\nNew Recovered : '+str(new_recovered_KW)+
   '\nTotal Recovered : '+str(total_recovered_KW))

def KG(update, context):
    new_confirmed_KG=(summary["Countries"][90]["NewConfirmed"])
    total_confirmed_KG=(summary["Countries"][90]["TotalConfirmed"])
    new_deaths_KG=(summary["Countries"][90]["NewDeaths"])
    total_deaths_KG=(summary["Countries"][90]["TotalDeaths"])
    new_recovered_KG=(summary["Countries"][90]["NewRecovered"])
    total_recovered_KG=(summary["Countries"][90]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Kyrgyzstan'
   '\nNew Confirmed : '+str(new_confirmed_KG)+
   '\nTotal Confirmed : '+str(total_confirmed_KG)+
   '\nNew Deaths : '+str(new_deaths_KG)+
   '\nTotal Deaths : '+str(total_deaths_KG)+
   '\nNew Recovered : '+str(new_recovered_KG)+
   '\nTotal Recovered : '+str(total_recovered_KG))

def LA(update, context):
    new_confirmed_LA=(summary["Countries"][91]["NewConfirmed"])
    total_confirmed_LA=(summary["Countries"][91]["TotalConfirmed"])
    new_deaths_LA=(summary["Countries"][91]["NewDeaths"])
    total_deaths_LA=(summary["Countries"][91]["TotalDeaths"])
    new_recovered_LA=(summary["Countries"][91]["NewRecovered"])
    total_recovered_LA=(summary["Countries"][91]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Lao PDR'
   '\nNew Confirmed : '+str(new_confirmed_LA)+
   '\nTotal Confirmed : '+str(total_confirmed_LA)+
   '\nNew Deaths : '+str(new_deaths_LA)+
   '\nTotal Deaths : '+str(total_deaths_LA)+
   '\nNew Recovered : '+str(new_recovered_LA)+
   '\nTotal Recovered : '+str(total_recovered_LA))

def LV(update, context):
    new_confirmed_LV=(summary["Countries"][92]["NewConfirmed"])
    total_confirmed_LV=(summary["Countries"][92]["TotalConfirmed"])
    new_deaths_LV=(summary["Countries"][92]["NewDeaths"])
    total_deaths_LV=(summary["Countries"][92]["TotalDeaths"])
    new_recovered_LV=(summary["Countries"][92]["NewRecovered"])
    total_recovered_LV=(summary["Countries"][92]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Latvia'
   '\nNew Confirmed : '+str(new_confirmed_LV)+
   '\nTotal Confirmed : '+str(total_confirmed_LV)+
   '\nNew Deaths : '+str(new_deaths_LV)+
   '\nTotal Deaths : '+str(total_deaths_LV)+
   '\nNew Recovered : '+str(new_recovered_LV)+
   '\nTotal Recovered : '+str(total_recovered_LV))

def LB(update, context):
    new_confirmed_LB=(summary["Countries"][93]["NewConfirmed"])
    total_confirmed_LB=(summary["Countries"][93]["TotalConfirmed"])
    new_deaths_LB=(summary["Countries"][93]["NewDeaths"])
    total_deaths_LB=(summary["Countries"][93]["TotalDeaths"])
    new_recovered_LB=(summary["Countries"][93]["NewRecovered"])
    total_recovered_LB=(summary["Countries"][93]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Lebanon'
   '\nNew Confirmed : '+str(new_confirmed_LB)+
   '\nTotal Confirmed : '+str(total_confirmed_LB)+
   '\nNew Deaths : '+str(new_deaths_LB)+
   '\nTotal Deaths : '+str(total_deaths_LB)+
   '\nNew Recovered : '+str(new_recovered_LB)+
   '\nTotal Recovered : '+str(total_recovered_LB))

def LS(update, context):
    new_confirmed_LS=(summary["Countries"][94]["NewConfirmed"])
    total_confirmed_LS=(summary["Countries"][94]["TotalConfirmed"])
    new_deaths_LS=(summary["Countries"][94]["NewDeaths"])
    total_deaths_LS=(summary["Countries"][94]["TotalDeaths"])
    new_recovered_LS=(summary["Countries"][94]["NewRecovered"])
    total_recovered_LS=(summary["Countries"][94]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Lesotho'
   '\nNew Confirmed : '+str(new_confirmed_LS)+
   '\nTotal Confirmed : '+str(total_confirmed_LS)+
   '\nNew Deaths : '+str(new_deaths_LS)+
   '\nTotal Deaths : '+str(total_deaths_LS)+
   '\nNew Recovered : '+str(new_recovered_LS)+
   '\nTotal Recovered : '+str(total_recovered_LS))

def LR(update, context):
    new_confirmed_LR=(summary["Countries"][95]["NewConfirmed"])
    total_confirmed_LR=(summary["Countries"][95]["TotalConfirmed"])
    new_deaths_LR=(summary["Countries"][95]["NewDeaths"])
    total_deaths_LR=(summary["Countries"][95]["TotalDeaths"])
    new_recovered_LR=(summary["Countries"][95]["NewRecovered"])
    total_recovered_LR=(summary["Countries"][95]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Liberia'
   '\nNew Confirmed : '+str(new_confirmed_LR)+
   '\nTotal Confirmed : '+str(total_confirmed_LR)+
   '\nNew Deaths : '+str(new_deaths_LR)+
   '\nTotal Deaths : '+str(total_deaths_LR)+
   '\nNew Recovered : '+str(new_recovered_LR)+
   '\nTotal Recovered : '+str(total_recovered_LR))

def LY(update, context):
    new_confirmed_LY=(summary["Countries"][96]["NewConfirmed"])
    total_confirmed_LY=(summary["Countries"][96]["TotalConfirmed"])
    new_deaths_LY=(summary["Countries"][96]["NewDeaths"])
    total_deaths_LY=(summary["Countries"][96]["TotalDeaths"])
    new_recovered_LY=(summary["Countries"][96]["NewRecovered"])
    total_recovered_LY=(summary["Countries"][96]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Libya'
   '\nNew Confirmed : '+str(new_confirmed_LY)+
   '\nTotal Confirmed : '+str(total_confirmed_LY)+
   '\nNew Deaths : '+str(new_deaths_LY)+
   '\nTotal Deaths : '+str(total_deaths_LY)+
   '\nNew Recovered : '+str(new_recovered_LY)+
   '\nTotal Recovered : '+str(total_recovered_LY))

def LI(update, context):
    new_confirmed_LI=(summary["Countries"][97]["NewConfirmed"])
    total_confirmed_LI=(summary["Countries"][97]["TotalConfirmed"])
    new_deaths_LI=(summary["Countries"][97]["NewDeaths"])
    total_deaths_LI=(summary["Countries"][97]["TotalDeaths"])
    new_recovered_LI=(summary["Countries"][97]["NewRecovered"])
    total_recovered_LI=(summary["Countries"][97]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Liechtenstein'
   '\nNew Confirmed : '+str(new_confirmed_LI)+
   '\nTotal Confirmed : '+str(total_confirmed_LI)+
   '\nNew Deaths : '+str(new_deaths_LI)+
   '\nTotal Deaths : '+str(total_deaths_LI)+
   '\nNew Recovered : '+str(new_recovered_LI)+
   '\nTotal Recovered : '+str(total_recovered_LI))

def LT(update, context):
    new_confirmed_LT=(summary["Countries"][98]["NewConfirmed"])
    total_confirmed_LT=(summary["Countries"][98]["TotalConfirmed"])
    new_deaths_LT=(summary["Countries"][98]["NewDeaths"])
    total_deaths_LT=(summary["Countries"][98]["TotalDeaths"])
    new_recovered_LT=(summary["Countries"][98]["NewRecovered"])
    total_recovered_LT=(summary["Countries"][98]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Lithuania'
   '\nNew Confirmed : '+str(new_confirmed_LT)+
   '\nTotal Confirmed : '+str(total_confirmed_LT)+
   '\nNew Deaths : '+str(new_deaths_LT)+
   '\nTotal Deaths : '+str(total_deaths_LT)+
   '\nNew Recovered : '+str(new_recovered_LT)+
   '\nTotal Recovered : '+str(total_recovered_LT))

def LU(update, context):
    new_confirmed_LU=(summary["Countries"][99]["NewConfirmed"])
    total_confirmed_LU=(summary["Countries"][99]["TotalConfirmed"])
    new_deaths_LU=(summary["Countries"][99]["NewDeaths"])
    total_deaths_LU=(summary["Countries"][99]["TotalDeaths"])
    new_recovered_LU=(summary["Countries"][99]["NewRecovered"])
    total_recovered_LU=(summary["Countries"][99]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Luxembourg'
   '\nNew Confirmed : '+str(new_confirmed_LU)+
   '\nTotal Confirmed : '+str(total_confirmed_LU)+
   '\nNew Deaths : '+str(new_deaths_LU)+
   '\nTotal Deaths : '+str(total_deaths_LU)+
   '\nNew Recovered : '+str(new_recovered_LU)+
   '\nTotal Recovered : '+str(total_recovered_LU))

def MK(update, context):
    new_confirmed_MK=(summary["Countries"][100]["NewConfirmed"])    
    total_confirmed_MK=(summary["Countries"][100]["TotalConfirmed"])
    new_deaths_MK=(summary["Countries"][100]["NewDeaths"])
    total_deaths_MK=(summary["Countries"][100]["TotalDeaths"])      
    new_recovered_MK=(summary["Countries"][100]["NewRecovered"])    
    total_recovered_MK=(summary["Countries"][100]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Macedonia, Republic of'
   '\nNew Confirmed : '+str(new_confirmed_MK)+
   '\nTotal Confirmed : '+str(total_confirmed_MK)+
   '\nNew Deaths : '+str(new_deaths_MK)+
   '\nTotal Deaths : '+str(total_deaths_MK)+
   '\nNew Recovered : '+str(new_recovered_MK)+
   '\nTotal Recovered : '+str(total_recovered_MK))

def MG(update, context):
    new_confirmed_MG=(summary["Countries"][101]["NewConfirmed"])
    total_confirmed_MG=(summary["Countries"][101]["TotalConfirmed"])
    new_deaths_MG=(summary["Countries"][101]["NewDeaths"])
    total_deaths_MG=(summary["Countries"][101]["TotalDeaths"])
    new_recovered_MG=(summary["Countries"][101]["NewRecovered"])
    total_recovered_MG=(summary["Countries"][101]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Madagascar'
   '\nNew Confirmed : '+str(new_confirmed_MG)+
   '\nTotal Confirmed : '+str(total_confirmed_MG)+
   '\nNew Deaths : '+str(new_deaths_MG)+
   '\nTotal Deaths : '+str(total_deaths_MG)+
   '\nNew Recovered : '+str(new_recovered_MG)+
   '\nTotal Recovered : '+str(total_recovered_MG))

def MW(update, context):
    new_confirmed_MW=(summary["Countries"][102]["NewConfirmed"])
    total_confirmed_MW=(summary["Countries"][102]["TotalConfirmed"])
    new_deaths_MW=(summary["Countries"][102]["NewDeaths"])
    total_deaths_MW=(summary["Countries"][102]["TotalDeaths"])
    new_recovered_MW=(summary["Countries"][102]["NewRecovered"])
    total_recovered_MW=(summary["Countries"][102]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Malawi'
   '\nNew Confirmed : '+str(new_confirmed_MW)+
   '\nTotal Confirmed : '+str(total_confirmed_MW)+
   '\nNew Deaths : '+str(new_deaths_MW)+
   '\nTotal Deaths : '+str(total_deaths_MW)+
   '\nNew Recovered : '+str(new_recovered_MW)+
   '\nTotal Recovered : '+str(total_recovered_MW))

def MY(update, context):
    new_confirmed_MY=(summary["Countries"][103]["NewConfirmed"])
    total_confirmed_MY=(summary["Countries"][103]["TotalConfirmed"])
    new_deaths_MY=(summary["Countries"][103]["NewDeaths"])
    total_deaths_MY=(summary["Countries"][103]["TotalDeaths"])
    new_recovered_MY=(summary["Countries"][103]["NewRecovered"])
    total_recovered_MY=(summary["Countries"][103]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Malaysia'
   '\nNew Confirmed : '+str(new_confirmed_MY)+
   '\nTotal Confirmed : '+str(total_confirmed_MY)+
   '\nNew Deaths : '+str(new_deaths_MY)+
   '\nTotal Deaths : '+str(total_deaths_MY)+
   '\nNew Recovered : '+str(new_recovered_MY)+
   '\nTotal Recovered : '+str(total_recovered_MY))

def MV(update, context):
    new_confirmed_MV=(summary["Countries"][104]["NewConfirmed"])
    total_confirmed_MV=(summary["Countries"][104]["TotalConfirmed"])
    new_deaths_MV=(summary["Countries"][104]["NewDeaths"])
    total_deaths_MV=(summary["Countries"][104]["TotalDeaths"])
    new_recovered_MV=(summary["Countries"][104]["NewRecovered"])
    total_recovered_MV=(summary["Countries"][104]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Maldives'
   '\nNew Confirmed : '+str(new_confirmed_MV)+
   '\nTotal Confirmed : '+str(total_confirmed_MV)+
   '\nNew Deaths : '+str(new_deaths_MV)+
   '\nTotal Deaths : '+str(total_deaths_MV)+
   '\nNew Recovered : '+str(new_recovered_MV)+
   '\nTotal Recovered : '+str(total_recovered_MV))

def ML(update, context):
    new_confirmed_ML=(summary["Countries"][105]["NewConfirmed"])
    total_confirmed_ML=(summary["Countries"][105]["TotalConfirmed"])
    new_deaths_ML=(summary["Countries"][105]["NewDeaths"])
    total_deaths_ML=(summary["Countries"][105]["TotalDeaths"])
    new_recovered_ML=(summary["Countries"][105]["NewRecovered"])
    total_recovered_ML=(summary["Countries"][105]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Mali'
   '\nNew Confirmed : '+str(new_confirmed_ML)+
   '\nTotal Confirmed : '+str(total_confirmed_ML)+
   '\nNew Deaths : '+str(new_deaths_ML)+
   '\nTotal Deaths : '+str(total_deaths_ML)+
   '\nNew Recovered : '+str(new_recovered_ML)+
   '\nTotal Recovered : '+str(total_recovered_ML))

def MT(update, context):
    new_confirmed_MT=(summary["Countries"][106]["NewConfirmed"])
    total_confirmed_MT=(summary["Countries"][106]["TotalConfirmed"])
    new_deaths_MT=(summary["Countries"][106]["NewDeaths"])
    total_deaths_MT=(summary["Countries"][106]["TotalDeaths"])
    new_recovered_MT=(summary["Countries"][106]["NewRecovered"])
    total_recovered_MT=(summary["Countries"][106]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Malta'
   '\nNew Confirmed : '+str(new_confirmed_MT)+
   '\nTotal Confirmed : '+str(total_confirmed_MT)+
   '\nNew Deaths : '+str(new_deaths_MT)+
   '\nTotal Deaths : '+str(total_deaths_MT)+
   '\nNew Recovered : '+str(new_recovered_MT)+
   '\nTotal Recovered : '+str(total_recovered_MT))

def MR(update, context):
    new_confirmed_MR=(summary["Countries"][107]["NewConfirmed"])
    total_confirmed_MR=(summary["Countries"][107]["TotalConfirmed"])
    new_deaths_MR=(summary["Countries"][107]["NewDeaths"])
    total_deaths_MR=(summary["Countries"][107]["TotalDeaths"])
    new_recovered_MR=(summary["Countries"][107]["NewRecovered"])
    total_recovered_MR=(summary["Countries"][107]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Mauritania'
   '\nNew Confirmed : '+str(new_confirmed_MR)+
   '\nTotal Confirmed : '+str(total_confirmed_MR)+
   '\nNew Deaths : '+str(new_deaths_MR)+
   '\nTotal Deaths : '+str(total_deaths_MR)+
   '\nNew Recovered : '+str(new_recovered_MR)+
   '\nTotal Recovered : '+str(total_recovered_MR))

def MU(update, context):
    new_confirmed_MU=(summary["Countries"][108]["NewConfirmed"])
    total_confirmed_MU=(summary["Countries"][108]["TotalConfirmed"])
    new_deaths_MU=(summary["Countries"][108]["NewDeaths"])
    total_deaths_MU=(summary["Countries"][108]["TotalDeaths"])
    new_recovered_MU=(summary["Countries"][108]["NewRecovered"])
    total_recovered_MU=(summary["Countries"][108]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Mauritius'
   '\nNew Confirmed : '+str(new_confirmed_MU)+
   '\nTotal Confirmed : '+str(total_confirmed_MU)+
   '\nNew Deaths : '+str(new_deaths_MU)+
   '\nTotal Deaths : '+str(total_deaths_MU)+
   '\nNew Recovered : '+str(new_recovered_MU)+
   '\nTotal Recovered : '+str(total_recovered_MU))

def MX(update, context):
    new_confirmed_MX=(summary["Countries"][109]["NewConfirmed"])
    total_confirmed_MX=(summary["Countries"][109]["TotalConfirmed"])
    new_deaths_MX=(summary["Countries"][109]["NewDeaths"])
    total_deaths_MX=(summary["Countries"][109]["TotalDeaths"])
    new_recovered_MX=(summary["Countries"][109]["NewRecovered"])
    total_recovered_MX=(summary["Countries"][109]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Mexico'
   '\nNew Confirmed : '+str(new_confirmed_MX)+
   '\nTotal Confirmed : '+str(total_confirmed_MX)+
   '\nNew Deaths : '+str(new_deaths_MX)+
   '\nTotal Deaths : '+str(total_deaths_MX)+
   '\nNew Recovered : '+str(new_recovered_MX)+
   '\nTotal Recovered : '+str(total_recovered_MX))

def MD(update, context):
    new_confirmed_MD=(summary["Countries"][110]["NewConfirmed"])
    total_confirmed_MD=(summary["Countries"][110]["TotalConfirmed"])
    new_deaths_MD=(summary["Countries"][110]["NewDeaths"])
    total_deaths_MD=(summary["Countries"][110]["TotalDeaths"])
    new_recovered_MD=(summary["Countries"][110]["NewRecovered"])
    total_recovered_MD=(summary["Countries"][110]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Moldova'
   '\nNew Confirmed : '+str(new_confirmed_MD)+
   '\nTotal Confirmed : '+str(total_confirmed_MD)+
   '\nNew Deaths : '+str(new_deaths_MD)+
   '\nTotal Deaths : '+str(total_deaths_MD)+
   '\nNew Recovered : '+str(new_recovered_MD)+
   '\nTotal Recovered : '+str(total_recovered_MD))

def MC(update, context):
    new_confirmed_MC=(summary["Countries"][111]["NewConfirmed"])
    total_confirmed_MC=(summary["Countries"][111]["TotalConfirmed"])
    new_deaths_MC=(summary["Countries"][111]["NewDeaths"])
    total_deaths_MC=(summary["Countries"][111]["TotalDeaths"])
    new_recovered_MC=(summary["Countries"][111]["NewRecovered"])
    total_recovered_MC=(summary["Countries"][111]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Monaco'
   '\nNew Confirmed : '+str(new_confirmed_MC)+
   '\nTotal Confirmed : '+str(total_confirmed_MC)+
   '\nNew Deaths : '+str(new_deaths_MC)+
   '\nTotal Deaths : '+str(total_deaths_MC)+
   '\nNew Recovered : '+str(new_recovered_MC)+
   '\nTotal Recovered : '+str(total_recovered_MC))

def MN(update, context):
    new_confirmed_MN=(summary["Countries"][112]["NewConfirmed"])
    total_confirmed_MN=(summary["Countries"][112]["TotalConfirmed"])
    new_deaths_MN=(summary["Countries"][112]["NewDeaths"])
    total_deaths_MN=(summary["Countries"][112]["TotalDeaths"])
    new_recovered_MN=(summary["Countries"][112]["NewRecovered"])
    total_recovered_MN=(summary["Countries"][112]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Mongolia'
   '\nNew Confirmed : '+str(new_confirmed_MN)+
   '\nTotal Confirmed : '+str(total_confirmed_MN)+
   '\nNew Deaths : '+str(new_deaths_MN)+
   '\nTotal Deaths : '+str(total_deaths_MN)+
   '\nNew Recovered : '+str(new_recovered_MN)+
   '\nTotal Recovered : '+str(total_recovered_MN))

def ME(update, context):
    new_confirmed_ME=(summary["Countries"][113]["NewConfirmed"])
    total_confirmed_ME=(summary["Countries"][113]["TotalConfirmed"])
    new_deaths_ME=(summary["Countries"][113]["NewDeaths"])
    total_deaths_ME=(summary["Countries"][113]["TotalDeaths"])
    new_recovered_ME=(summary["Countries"][113]["NewRecovered"])
    total_recovered_ME=(summary["Countries"][113]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Montenegro'
   '\nNew Confirmed : '+str(new_confirmed_ME)+
   '\nTotal Confirmed : '+str(total_confirmed_ME)+
   '\nNew Deaths : '+str(new_deaths_ME)+
   '\nTotal Deaths : '+str(total_deaths_ME)+
   '\nNew Recovered : '+str(new_recovered_ME)+
   '\nTotal Recovered : '+str(total_recovered_ME))

def MA(update, context):
    new_confirmed_MA=(summary["Countries"][114]["NewConfirmed"])
    total_confirmed_MA=(summary["Countries"][114]["TotalConfirmed"])
    new_deaths_MA=(summary["Countries"][114]["NewDeaths"])
    total_deaths_MA=(summary["Countries"][114]["TotalDeaths"])
    new_recovered_MA=(summary["Countries"][114]["NewRecovered"])
    total_recovered_MA=(summary["Countries"][114]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Morocco'
   '\nNew Confirmed : '+str(new_confirmed_MA)+
   '\nTotal Confirmed : '+str(total_confirmed_MA)+
   '\nNew Deaths : '+str(new_deaths_MA)+
   '\nTotal Deaths : '+str(total_deaths_MA)+
   '\nNew Recovered : '+str(new_recovered_MA)+
   '\nTotal Recovered : '+str(total_recovered_MA))

def MZ(update, context):
    new_confirmed_MZ=(summary["Countries"][115]["NewConfirmed"])
    total_confirmed_MZ=(summary["Countries"][115]["TotalConfirmed"])
    new_deaths_MZ=(summary["Countries"][115]["NewDeaths"])
    total_deaths_MZ=(summary["Countries"][115]["TotalDeaths"])
    new_recovered_MZ=(summary["Countries"][115]["NewRecovered"])
    total_recovered_MZ=(summary["Countries"][115]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Mozambique'
   '\nNew Confirmed : '+str(new_confirmed_MZ)+
   '\nTotal Confirmed : '+str(total_confirmed_MZ)+
   '\nNew Deaths : '+str(new_deaths_MZ)+
   '\nTotal Deaths : '+str(total_deaths_MZ)+
   '\nNew Recovered : '+str(new_recovered_MZ)+
   '\nTotal Recovered : '+str(total_recovered_MZ))

def MM(update, context):
    new_confirmed_MM=(summary["Countries"][116]["NewConfirmed"])
    total_confirmed_MM=(summary["Countries"][116]["TotalConfirmed"])
    new_deaths_MM=(summary["Countries"][116]["NewDeaths"])
    total_deaths_MM=(summary["Countries"][116]["TotalDeaths"])
    new_recovered_MM=(summary["Countries"][116]["NewRecovered"])
    total_recovered_MM=(summary["Countries"][116]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Myanmar'
   '\nNew Confirmed : '+str(new_confirmed_MM)+
   '\nTotal Confirmed : '+str(total_confirmed_MM)+
   '\nNew Deaths : '+str(new_deaths_MM)+
   '\nTotal Deaths : '+str(total_deaths_MM)+
   '\nNew Recovered : '+str(new_recovered_MM)+
   '\nTotal Recovered : '+str(total_recovered_MM))

def NA(update, context):
    new_confirmed_NA=(summary["Countries"][117]["NewConfirmed"])
    total_confirmed_NA=(summary["Countries"][117]["TotalConfirmed"])
    new_deaths_NA=(summary["Countries"][117]["NewDeaths"])
    total_deaths_NA=(summary["Countries"][117]["TotalDeaths"])
    new_recovered_NA=(summary["Countries"][117]["NewRecovered"])
    total_recovered_NA=(summary["Countries"][117]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Namibia'
   '\nNew Confirmed : '+str(new_confirmed_NA)+
   '\nTotal Confirmed : '+str(total_confirmed_NA)+
   '\nNew Deaths : '+str(new_deaths_NA)+
   '\nTotal Deaths : '+str(total_deaths_NA)+
   '\nNew Recovered : '+str(new_recovered_NA)+
   '\nTotal Recovered : '+str(total_recovered_NA))

def NP(update, context):
    new_confirmed_NP=(summary["Countries"][118]["NewConfirmed"])
    total_confirmed_NP=(summary["Countries"][118]["TotalConfirmed"])
    new_deaths_NP=(summary["Countries"][118]["NewDeaths"])
    total_deaths_NP=(summary["Countries"][118]["TotalDeaths"])
    new_recovered_NP=(summary["Countries"][118]["NewRecovered"])
    total_recovered_NP=(summary["Countries"][118]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Nepal'
   '\nNew Confirmed : '+str(new_confirmed_NP)+
   '\nTotal Confirmed : '+str(total_confirmed_NP)+
   '\nNew Deaths : '+str(new_deaths_NP)+
   '\nTotal Deaths : '+str(total_deaths_NP)+
   '\nNew Recovered : '+str(new_recovered_NP)+
   '\nTotal Recovered : '+str(total_recovered_NP))

def NL(update, context):
    new_confirmed_NL=(summary["Countries"][119]["NewConfirmed"])
    total_confirmed_NL=(summary["Countries"][119]["TotalConfirmed"])
    new_deaths_NL=(summary["Countries"][119]["NewDeaths"])
    total_deaths_NL=(summary["Countries"][119]["TotalDeaths"])
    new_recovered_NL=(summary["Countries"][119]["NewRecovered"])
    total_recovered_NL=(summary["Countries"][119]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Netherlands'
   '\nNew Confirmed : '+str(new_confirmed_NL)+
   '\nTotal Confirmed : '+str(total_confirmed_NL)+
   '\nNew Deaths : '+str(new_deaths_NL)+
   '\nTotal Deaths : '+str(total_deaths_NL)+
   '\nNew Recovered : '+str(new_recovered_NL)+
   '\nTotal Recovered : '+str(total_recovered_NL))

def NZ(update, context):
    new_confirmed_NZ=(summary["Countries"][120]["NewConfirmed"])
    total_confirmed_NZ=(summary["Countries"][120]["TotalConfirmed"])
    new_deaths_NZ=(summary["Countries"][120]["NewDeaths"])
    total_deaths_NZ=(summary["Countries"][120]["TotalDeaths"])
    new_recovered_NZ=(summary["Countries"][120]["NewRecovered"])
    total_recovered_NZ=(summary["Countries"][120]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': New Zealand'
   '\nNew Confirmed : '+str(new_confirmed_NZ)+
   '\nTotal Confirmed : '+str(total_confirmed_NZ)+
   '\nNew Deaths : '+str(new_deaths_NZ)+
   '\nTotal Deaths : '+str(total_deaths_NZ)+
   '\nNew Recovered : '+str(new_recovered_NZ)+
   '\nTotal Recovered : '+str(total_recovered_NZ))

def NI(update, context):
    new_confirmed_NI=(summary["Countries"][121]["NewConfirmed"])
    total_confirmed_NI=(summary["Countries"][121]["TotalConfirmed"])
    new_deaths_NI=(summary["Countries"][121]["NewDeaths"])
    total_deaths_NI=(summary["Countries"][121]["TotalDeaths"])
    new_recovered_NI=(summary["Countries"][121]["NewRecovered"])
    total_recovered_NI=(summary["Countries"][121]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Nicaragua'
   '\nNew Confirmed : '+str(new_confirmed_NI)+
   '\nTotal Confirmed : '+str(total_confirmed_NI)+
   '\nNew Deaths : '+str(new_deaths_NI)+
   '\nTotal Deaths : '+str(total_deaths_NI)+
   '\nNew Recovered : '+str(new_recovered_NI)+
   '\nTotal Recovered : '+str(total_recovered_NI))

def NE(update, context):
    new_confirmed_NE=(summary["Countries"][122]["NewConfirmed"])
    total_confirmed_NE=(summary["Countries"][122]["TotalConfirmed"])
    new_deaths_NE=(summary["Countries"][122]["NewDeaths"])
    total_deaths_NE=(summary["Countries"][122]["TotalDeaths"])
    new_recovered_NE=(summary["Countries"][122]["NewRecovered"])
    total_recovered_NE=(summary["Countries"][122]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Niger'
   '\nNew Confirmed : '+str(new_confirmed_NE)+
   '\nTotal Confirmed : '+str(total_confirmed_NE)+
   '\nNew Deaths : '+str(new_deaths_NE)+
   '\nTotal Deaths : '+str(total_deaths_NE)+
   '\nNew Recovered : '+str(new_recovered_NE)+
   '\nTotal Recovered : '+str(total_recovered_NE))

def NG(update, context):
    new_confirmed_NG=(summary["Countries"][123]["NewConfirmed"])
    total_confirmed_NG=(summary["Countries"][123]["TotalConfirmed"])
    new_deaths_NG=(summary["Countries"][123]["NewDeaths"])
    total_deaths_NG=(summary["Countries"][123]["TotalDeaths"])
    new_recovered_NG=(summary["Countries"][123]["NewRecovered"])
    total_recovered_NG=(summary["Countries"][123]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Nigeria'
   '\nNew Confirmed : '+str(new_confirmed_NG)+
   '\nTotal Confirmed : '+str(total_confirmed_NG)+
   '\nNew Deaths : '+str(new_deaths_NG)+
   '\nTotal Deaths : '+str(total_deaths_NG)+
   '\nNew Recovered : '+str(new_recovered_NG)+
   '\nTotal Recovered : '+str(total_recovered_NG))

def NO(update, context):
    new_confirmed_NO=(summary["Countries"][124]["NewConfirmed"])
    total_confirmed_NO=(summary["Countries"][124]["TotalConfirmed"])
    new_deaths_NO=(summary["Countries"][124]["NewDeaths"])
    total_deaths_NO=(summary["Countries"][124]["TotalDeaths"])
    new_recovered_NO=(summary["Countries"][124]["NewRecovered"])
    total_recovered_NO=(summary["Countries"][124]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Norway'
   '\nNew Confirmed : '+str(new_confirmed_NO)+
   '\nTotal Confirmed : '+str(total_confirmed_NO)+
   '\nNew Deaths : '+str(new_deaths_NO)+
   '\nTotal Deaths : '+str(total_deaths_NO)+
   '\nNew Recovered : '+str(new_recovered_NO)+
   '\nTotal Recovered : '+str(total_recovered_NO))

def OM(update, context):
    new_confirmed_OM=(summary["Countries"][125]["NewConfirmed"])
    total_confirmed_OM=(summary["Countries"][125]["TotalConfirmed"])
    new_deaths_OM=(summary["Countries"][125]["NewDeaths"])
    total_deaths_OM=(summary["Countries"][125]["TotalDeaths"])
    new_recovered_OM=(summary["Countries"][125]["NewRecovered"])
    total_recovered_OM=(summary["Countries"][125]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Oman'
   '\nNew Confirmed : '+str(new_confirmed_OM)+
   '\nTotal Confirmed : '+str(total_confirmed_OM)+
   '\nNew Deaths : '+str(new_deaths_OM)+
   '\nTotal Deaths : '+str(total_deaths_OM)+
   '\nNew Recovered : '+str(new_recovered_OM)+
   '\nTotal Recovered : '+str(total_recovered_OM))

def PK(update, context):
    new_confirmed_PK=(summary["Countries"][126]["NewConfirmed"])
    total_confirmed_PK=(summary["Countries"][126]["TotalConfirmed"])
    new_deaths_PK=(summary["Countries"][126]["NewDeaths"])
    total_deaths_PK=(summary["Countries"][126]["TotalDeaths"])
    new_recovered_PK=(summary["Countries"][126]["NewRecovered"])
    total_recovered_PK=(summary["Countries"][126]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Pakistan'
   '\nNew Confirmed : '+str(new_confirmed_PK)+
   '\nTotal Confirmed : '+str(total_confirmed_PK)+
   '\nNew Deaths : '+str(new_deaths_PK)+
   '\nTotal Deaths : '+str(total_deaths_PK)+
   '\nNew Recovered : '+str(new_recovered_PK)+
   '\nTotal Recovered : '+str(total_recovered_PK))

def PS(update, context):
    new_confirmed_PS=(summary["Countries"][127]["NewConfirmed"])
    total_confirmed_PS=(summary["Countries"][127]["TotalConfirmed"])
    new_deaths_PS=(summary["Countries"][127]["NewDeaths"])
    total_deaths_PS=(summary["Countries"][127]["TotalDeaths"])
    new_recovered_PS=(summary["Countries"][127]["NewRecovered"])
    total_recovered_PS=(summary["Countries"][127]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Palestinian Territory'
   '\nNew Confirmed : '+str(new_confirmed_PS)+
   '\nTotal Confirmed : '+str(total_confirmed_PS)+
   '\nNew Deaths : '+str(new_deaths_PS)+
   '\nTotal Deaths : '+str(total_deaths_PS)+
   '\nNew Recovered : '+str(new_recovered_PS)+
   '\nTotal Recovered : '+str(total_recovered_PS))

def PA(update, context):
    new_confirmed_PA=(summary["Countries"][128]["NewConfirmed"])
    total_confirmed_PA=(summary["Countries"][128]["TotalConfirmed"])
    new_deaths_PA=(summary["Countries"][128]["NewDeaths"])
    total_deaths_PA=(summary["Countries"][128]["TotalDeaths"])
    new_recovered_PA=(summary["Countries"][128]["NewRecovered"])
    total_recovered_PA=(summary["Countries"][128]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Panama'
   '\nNew Confirmed : '+str(new_confirmed_PA)+
   '\nTotal Confirmed : '+str(total_confirmed_PA)+
   '\nNew Deaths : '+str(new_deaths_PA)+
   '\nTotal Deaths : '+str(total_deaths_PA)+
   '\nNew Recovered : '+str(new_recovered_PA)+
   '\nTotal Recovered : '+str(total_recovered_PA))

def PG(update, context):
    new_confirmed_PG=(summary["Countries"][129]["NewConfirmed"])
    total_confirmed_PG=(summary["Countries"][129]["TotalConfirmed"])
    new_deaths_PG=(summary["Countries"][129]["NewDeaths"])
    total_deaths_PG=(summary["Countries"][129]["TotalDeaths"])
    new_recovered_PG=(summary["Countries"][129]["NewRecovered"])
    total_recovered_PG=(summary["Countries"][129]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Papua New Guinea'
   '\nNew Confirmed : '+str(new_confirmed_PG)+
   '\nTotal Confirmed : '+str(total_confirmed_PG)+
   '\nNew Deaths : '+str(new_deaths_PG)+
   '\nTotal Deaths : '+str(total_deaths_PG)+
   '\nNew Recovered : '+str(new_recovered_PG)+
   '\nTotal Recovered : '+str(total_recovered_PG))

def PY(update, context):
    new_confirmed_PY=(summary["Countries"][130]["NewConfirmed"])
    total_confirmed_PY=(summary["Countries"][130]["TotalConfirmed"])
    new_deaths_PY=(summary["Countries"][130]["NewDeaths"])
    total_deaths_PY=(summary["Countries"][130]["TotalDeaths"])
    new_recovered_PY=(summary["Countries"][130]["NewRecovered"])
    total_recovered_PY=(summary["Countries"][130]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Paraguay'
   '\nNew Confirmed : '+str(new_confirmed_PY)+
   '\nTotal Confirmed : '+str(total_confirmed_PY)+
   '\nNew Deaths : '+str(new_deaths_PY)+
   '\nTotal Deaths : '+str(total_deaths_PY)+
   '\nNew Recovered : '+str(new_recovered_PY)+
   '\nTotal Recovered : '+str(total_recovered_PY))

def PE(update, context):
    new_confirmed_PE=(summary["Countries"][131]["NewConfirmed"])
    total_confirmed_PE=(summary["Countries"][131]["TotalConfirmed"])
    new_deaths_PE=(summary["Countries"][131]["NewDeaths"])
    total_deaths_PE=(summary["Countries"][131]["TotalDeaths"])
    new_recovered_PE=(summary["Countries"][131]["NewRecovered"])
    total_recovered_PE=(summary["Countries"][131]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Peru'
   '\nNew Confirmed : '+str(new_confirmed_PE)+
   '\nTotal Confirmed : '+str(total_confirmed_PE)+
   '\nNew Deaths : '+str(new_deaths_PE)+
   '\nTotal Deaths : '+str(total_deaths_PE)+
   '\nNew Recovered : '+str(new_recovered_PE)+
   '\nTotal Recovered : '+str(total_recovered_PE))

def PH(update, context):
    new_confirmed_PH=(summary["Countries"][132]["NewConfirmed"])
    total_confirmed_PH=(summary["Countries"][132]["TotalConfirmed"])
    new_deaths_PH=(summary["Countries"][132]["NewDeaths"])
    total_deaths_PH=(summary["Countries"][132]["TotalDeaths"])
    new_recovered_PH=(summary["Countries"][132]["NewRecovered"])
    total_recovered_PH=(summary["Countries"][132]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Philippines'
   '\nNew Confirmed : '+str(new_confirmed_PH)+
   '\nTotal Confirmed : '+str(total_confirmed_PH)+
   '\nNew Deaths : '+str(new_deaths_PH)+
   '\nTotal Deaths : '+str(total_deaths_PH)+
   '\nNew Recovered : '+str(new_recovered_PH)+
   '\nTotal Recovered : '+str(total_recovered_PH))

def PL(update, context):
    new_confirmed_PL=(summary["Countries"][133]["NewConfirmed"])
    total_confirmed_PL=(summary["Countries"][133]["TotalConfirmed"])
    new_deaths_PL=(summary["Countries"][133]["NewDeaths"])
    total_deaths_PL=(summary["Countries"][133]["TotalDeaths"])
    new_recovered_PL=(summary["Countries"][133]["NewRecovered"])
    total_recovered_PL=(summary["Countries"][133]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Poland'
   '\nNew Confirmed : '+str(new_confirmed_PL)+
   '\nTotal Confirmed : '+str(total_confirmed_PL)+
   '\nNew Deaths : '+str(new_deaths_PL)+
   '\nTotal Deaths : '+str(total_deaths_PL)+
   '\nNew Recovered : '+str(new_recovered_PL)+
   '\nTotal Recovered : '+str(total_recovered_PL))

def PT(update, context):
    new_confirmed_PT=(summary["Countries"][134]["NewConfirmed"])
    total_confirmed_PT=(summary["Countries"][134]["TotalConfirmed"])
    new_deaths_PT=(summary["Countries"][134]["NewDeaths"])
    total_deaths_PT=(summary["Countries"][134]["TotalDeaths"])
    new_recovered_PT=(summary["Countries"][134]["NewRecovered"])
    total_recovered_PT=(summary["Countries"][134]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Portugal'
   '\nNew Confirmed : '+str(new_confirmed_PT)+
   '\nTotal Confirmed : '+str(total_confirmed_PT)+
   '\nNew Deaths : '+str(new_deaths_PT)+
   '\nTotal Deaths : '+str(total_deaths_PT)+
   '\nNew Recovered : '+str(new_recovered_PT)+
   '\nTotal Recovered : '+str(total_recovered_PT))

def QA(update, context):
    new_confirmed_QA=(summary["Countries"][135]["NewConfirmed"])
    total_confirmed_QA=(summary["Countries"][135]["TotalConfirmed"])
    new_deaths_QA=(summary["Countries"][135]["NewDeaths"])
    total_deaths_QA=(summary["Countries"][135]["TotalDeaths"])
    new_recovered_QA=(summary["Countries"][135]["NewRecovered"])
    total_recovered_QA=(summary["Countries"][135]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Qatar'
   '\nNew Confirmed : '+str(new_confirmed_QA)+
   '\nTotal Confirmed : '+str(total_confirmed_QA)+
   '\nNew Deaths : '+str(new_deaths_QA)+
   '\nTotal Deaths : '+str(total_deaths_QA)+
   '\nNew Recovered : '+str(new_recovered_QA)+
   '\nTotal Recovered : '+str(total_recovered_QA))

def XK(update, context):
    new_confirmed_XK=(summary["Countries"][136]["NewConfirmed"])
    total_confirmed_XK=(summary["Countries"][136]["TotalConfirmed"])
    new_deaths_XK=(summary["Countries"][136]["NewDeaths"])
    total_deaths_XK=(summary["Countries"][136]["TotalDeaths"])
    new_recovered_XK=(summary["Countries"][136]["NewRecovered"])
    total_recovered_XK=(summary["Countries"][136]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Republic of Kosovo'
   '\nNew Confirmed : '+str(new_confirmed_XK)+
   '\nTotal Confirmed : '+str(total_confirmed_XK)+
   '\nNew Deaths : '+str(new_deaths_XK)+
   '\nTotal Deaths : '+str(total_deaths_XK)+
   '\nNew Recovered : '+str(new_recovered_XK)+
   '\nTotal Recovered : '+str(total_recovered_XK))

def RO(update, context):
    new_confirmed_RO=(summary["Countries"][137]["NewConfirmed"])
    total_confirmed_RO=(summary["Countries"][137]["TotalConfirmed"])
    new_deaths_RO=(summary["Countries"][137]["NewDeaths"])
    total_deaths_RO=(summary["Countries"][137]["TotalDeaths"])
    new_recovered_RO=(summary["Countries"][137]["NewRecovered"])
    total_recovered_RO=(summary["Countries"][137]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Romania'
   '\nNew Confirmed : '+str(new_confirmed_RO)+
   '\nTotal Confirmed : '+str(total_confirmed_RO)+
   '\nNew Deaths : '+str(new_deaths_RO)+
   '\nTotal Deaths : '+str(total_deaths_RO)+
   '\nNew Recovered : '+str(new_recovered_RO)+
   '\nTotal Recovered : '+str(total_recovered_RO))

def RU(update, context):
    new_confirmed_RU=(summary["Countries"][138]["NewConfirmed"])
    total_confirmed_RU=(summary["Countries"][138]["TotalConfirmed"])
    new_deaths_RU=(summary["Countries"][138]["NewDeaths"])
    total_deaths_RU=(summary["Countries"][138]["TotalDeaths"])
    new_recovered_RU=(summary["Countries"][138]["NewRecovered"])
    total_recovered_RU=(summary["Countries"][138]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Russian Federation'
   '\nNew Confirmed : '+str(new_confirmed_RU)+
   '\nTotal Confirmed : '+str(total_confirmed_RU)+
   '\nNew Deaths : '+str(new_deaths_RU)+
   '\nTotal Deaths : '+str(total_deaths_RU)+
   '\nNew Recovered : '+str(new_recovered_RU)+
   '\nTotal Recovered : '+str(total_recovered_RU))

def RW(update, context):
    new_confirmed_RW=(summary["Countries"][139]["NewConfirmed"])
    total_confirmed_RW=(summary["Countries"][139]["TotalConfirmed"])
    new_deaths_RW=(summary["Countries"][139]["NewDeaths"])
    total_deaths_RW=(summary["Countries"][139]["TotalDeaths"])
    new_recovered_RW=(summary["Countries"][139]["NewRecovered"])
    total_recovered_RW=(summary["Countries"][139]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Rwanda'
   '\nNew Confirmed : '+str(new_confirmed_RW)+
   '\nTotal Confirmed : '+str(total_confirmed_RW)+
   '\nNew Deaths : '+str(new_deaths_RW)+
   '\nTotal Deaths : '+str(total_deaths_RW)+
   '\nNew Recovered : '+str(new_recovered_RW)+
   '\nTotal Recovered : '+str(total_recovered_RW))

def KN(update, context):
    new_confirmed_KN=(summary["Countries"][140]["NewConfirmed"])
    total_confirmed_KN=(summary["Countries"][140]["TotalConfirmed"])
    new_deaths_KN=(summary["Countries"][140]["NewDeaths"])
    total_deaths_KN=(summary["Countries"][140]["TotalDeaths"])
    new_recovered_KN=(summary["Countries"][140]["NewRecovered"])
    total_recovered_KN=(summary["Countries"][140]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Saint Kitts and Nevis'
   '\nNew Confirmed : '+str(new_confirmed_KN)+
   '\nTotal Confirmed : '+str(total_confirmed_KN)+
   '\nNew Deaths : '+str(new_deaths_KN)+
   '\nTotal Deaths : '+str(total_deaths_KN)+
   '\nNew Recovered : '+str(new_recovered_KN)+
   '\nTotal Recovered : '+str(total_recovered_KN))

def LC(update, context):
    new_confirmed_LC=(summary["Countries"][141]["NewConfirmed"])
    total_confirmed_LC=(summary["Countries"][141]["TotalConfirmed"])
    new_deaths_LC=(summary["Countries"][141]["NewDeaths"])
    total_deaths_LC=(summary["Countries"][141]["TotalDeaths"])
    new_recovered_LC=(summary["Countries"][141]["NewRecovered"])
    total_recovered_LC=(summary["Countries"][141]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Saint Lucia'
   '\nNew Confirmed : '+str(new_confirmed_LC)+
   '\nTotal Confirmed : '+str(total_confirmed_LC)+
   '\nNew Deaths : '+str(new_deaths_LC)+
   '\nTotal Deaths : '+str(total_deaths_LC)+
   '\nNew Recovered : '+str(new_recovered_LC)+
   '\nTotal Recovered : '+str(total_recovered_LC))

def VC(update, context):
    new_confirmed_VC=(summary["Countries"][142]["NewConfirmed"])
    total_confirmed_VC=(summary["Countries"][142]["TotalConfirmed"])
    new_deaths_VC=(summary["Countries"][142]["NewDeaths"])
    total_deaths_VC=(summary["Countries"][142]["TotalDeaths"])
    new_recovered_VC=(summary["Countries"][142]["NewRecovered"])
    total_recovered_VC=(summary["Countries"][142]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Saint Vincent and Grenadines'
   '\nNew Confirmed : '+str(new_confirmed_VC)+
   '\nTotal Confirmed : '+str(total_confirmed_VC)+
   '\nNew Deaths : '+str(new_deaths_VC)+
   '\nTotal Deaths : '+str(total_deaths_VC)+
   '\nNew Recovered : '+str(new_recovered_VC)+
   '\nTotal Recovered : '+str(total_recovered_VC))

def SM(update, context):
    new_confirmed_SM=(summary["Countries"][143]["NewConfirmed"])
    total_confirmed_SM=(summary["Countries"][143]["TotalConfirmed"])
    new_deaths_SM=(summary["Countries"][143]["NewDeaths"])
    total_deaths_SM=(summary["Countries"][143]["TotalDeaths"])
    new_recovered_SM=(summary["Countries"][143]["NewRecovered"])
    total_recovered_SM=(summary["Countries"][143]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': San Marino'
   '\nNew Confirmed : '+str(new_confirmed_SM)+
   '\nTotal Confirmed : '+str(total_confirmed_SM)+
   '\nNew Deaths : '+str(new_deaths_SM)+
   '\nTotal Deaths : '+str(total_deaths_SM)+
   '\nNew Recovered : '+str(new_recovered_SM)+
   '\nTotal Recovered : '+str(total_recovered_SM))

def ST(update, context):
    new_confirmed_ST=(summary["Countries"][144]["NewConfirmed"])
    total_confirmed_ST=(summary["Countries"][144]["TotalConfirmed"])
    new_deaths_ST=(summary["Countries"][144]["NewDeaths"])
    total_deaths_ST=(summary["Countries"][144]["TotalDeaths"])
    new_recovered_ST=(summary["Countries"][144]["NewRecovered"])
    total_recovered_ST=(summary["Countries"][144]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Sao Tome and Principe'
   '\nNew Confirmed : '+str(new_confirmed_ST)+
   '\nTotal Confirmed : '+str(total_confirmed_ST)+
   '\nNew Deaths : '+str(new_deaths_ST)+
   '\nTotal Deaths : '+str(total_deaths_ST)+
   '\nNew Recovered : '+str(new_recovered_ST)+
   '\nTotal Recovered : '+str(total_recovered_ST))

def SA(update, context):
    new_confirmed_SA=(summary["Countries"][145]["NewConfirmed"])
    total_confirmed_SA=(summary["Countries"][145]["TotalConfirmed"])
    new_deaths_SA=(summary["Countries"][145]["NewDeaths"])
    total_deaths_SA=(summary["Countries"][145]["TotalDeaths"])
    new_recovered_SA=(summary["Countries"][145]["NewRecovered"])
    total_recovered_SA=(summary["Countries"][145]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Saudi Arabia'
   '\nNew Confirmed : '+str(new_confirmed_SA)+
   '\nTotal Confirmed : '+str(total_confirmed_SA)+
   '\nNew Deaths : '+str(new_deaths_SA)+
   '\nTotal Deaths : '+str(total_deaths_SA)+
   '\nNew Recovered : '+str(new_recovered_SA)+
   '\nTotal Recovered : '+str(total_recovered_SA))

def SN(update, context):
    new_confirmed_SN=(summary["Countries"][146]["NewConfirmed"])
    total_confirmed_SN=(summary["Countries"][146]["TotalConfirmed"])
    new_deaths_SN=(summary["Countries"][146]["NewDeaths"])
    total_deaths_SN=(summary["Countries"][146]["TotalDeaths"])
    new_recovered_SN=(summary["Countries"][146]["NewRecovered"])
    total_recovered_SN=(summary["Countries"][146]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Senegal'
   '\nNew Confirmed : '+str(new_confirmed_SN)+
   '\nTotal Confirmed : '+str(total_confirmed_SN)+
   '\nNew Deaths : '+str(new_deaths_SN)+
   '\nTotal Deaths : '+str(total_deaths_SN)+
   '\nNew Recovered : '+str(new_recovered_SN)+
   '\nTotal Recovered : '+str(total_recovered_SN))

def RS(update, context):
    new_confirmed_RS=(summary["Countries"][147]["NewConfirmed"])
    total_confirmed_RS=(summary["Countries"][147]["TotalConfirmed"])
    new_deaths_RS=(summary["Countries"][147]["NewDeaths"])
    total_deaths_RS=(summary["Countries"][147]["TotalDeaths"])
    new_recovered_RS=(summary["Countries"][147]["NewRecovered"])
    total_recovered_RS=(summary["Countries"][147]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Serbia'
   '\nNew Confirmed : '+str(new_confirmed_RS)+
   '\nTotal Confirmed : '+str(total_confirmed_RS)+
   '\nNew Deaths : '+str(new_deaths_RS)+
   '\nTotal Deaths : '+str(total_deaths_RS)+
   '\nNew Recovered : '+str(new_recovered_RS)+
   '\nTotal Recovered : '+str(total_recovered_RS))

def SC(update, context):
    new_confirmed_SC=(summary["Countries"][148]["NewConfirmed"])
    total_confirmed_SC=(summary["Countries"][148]["TotalConfirmed"])
    new_deaths_SC=(summary["Countries"][148]["NewDeaths"])
    total_deaths_SC=(summary["Countries"][148]["TotalDeaths"])
    new_recovered_SC=(summary["Countries"][148]["NewRecovered"])
    total_recovered_SC=(summary["Countries"][148]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Seychelles'
   '\nNew Confirmed : '+str(new_confirmed_SC)+
   '\nTotal Confirmed : '+str(total_confirmed_SC)+
   '\nNew Deaths : '+str(new_deaths_SC)+
   '\nTotal Deaths : '+str(total_deaths_SC)+
   '\nNew Recovered : '+str(new_recovered_SC)+
   '\nTotal Recovered : '+str(total_recovered_SC))

def SL(update, context):
    new_confirmed_SL=(summary["Countries"][149]["NewConfirmed"])
    total_confirmed_SL=(summary["Countries"][149]["TotalConfirmed"])
    new_deaths_SL=(summary["Countries"][149]["NewDeaths"])
    total_deaths_SL=(summary["Countries"][149]["TotalDeaths"])
    new_recovered_SL=(summary["Countries"][149]["NewRecovered"])
    total_recovered_SL=(summary["Countries"][149]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Sierra Leone'
   '\nNew Confirmed : '+str(new_confirmed_SL)+
   '\nTotal Confirmed : '+str(total_confirmed_SL)+
   '\nNew Deaths : '+str(new_deaths_SL)+
   '\nTotal Deaths : '+str(total_deaths_SL)+
   '\nNew Recovered : '+str(new_recovered_SL)+
   '\nTotal Recovered : '+str(total_recovered_SL))

def SG(update, context):
    new_confirmed_SG=(summary["Countries"][150]["NewConfirmed"])    
    total_confirmed_SG=(summary["Countries"][150]["TotalConfirmed"])
    new_deaths_SG=(summary["Countries"][150]["NewDeaths"])
    total_deaths_SG=(summary["Countries"][150]["TotalDeaths"])      
    new_recovered_SG=(summary["Countries"][150]["NewRecovered"])    
    total_recovered_SG=(summary["Countries"][150]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Singapore'
   '\nNew Confirmed : '+str(new_confirmed_SG)+
   '\nTotal Confirmed : '+str(total_confirmed_SG)+
   '\nNew Deaths : '+str(new_deaths_SG)+
   '\nTotal Deaths : '+str(total_deaths_SG)+
   '\nNew Recovered : '+str(new_recovered_SG)+
   '\nTotal Recovered : '+str(total_recovered_SG))

def SK(update, context):
    new_confirmed_SK=(summary["Countries"][151]["NewConfirmed"])
    total_confirmed_SK=(summary["Countries"][151]["TotalConfirmed"])
    new_deaths_SK=(summary["Countries"][151]["NewDeaths"])
    total_deaths_SK=(summary["Countries"][151]["TotalDeaths"])
    new_recovered_SK=(summary["Countries"][151]["NewRecovered"])
    total_recovered_SK=(summary["Countries"][151]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Slovakia'
   '\nNew Confirmed : '+str(new_confirmed_SK)+
   '\nTotal Confirmed : '+str(total_confirmed_SK)+
   '\nNew Deaths : '+str(new_deaths_SK)+
   '\nTotal Deaths : '+str(total_deaths_SK)+
   '\nNew Recovered : '+str(new_recovered_SK)+
   '\nTotal Recovered : '+str(total_recovered_SK))

def SI(update, context):
    new_confirmed_SI=(summary["Countries"][152]["NewConfirmed"])
    total_confirmed_SI=(summary["Countries"][152]["TotalConfirmed"])
    new_deaths_SI=(summary["Countries"][152]["NewDeaths"])
    total_deaths_SI=(summary["Countries"][152]["TotalDeaths"])
    new_recovered_SI=(summary["Countries"][152]["NewRecovered"])
    total_recovered_SI=(summary["Countries"][152]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Slovenia'
   '\nNew Confirmed : '+str(new_confirmed_SI)+
   '\nTotal Confirmed : '+str(total_confirmed_SI)+
   '\nNew Deaths : '+str(new_deaths_SI)+
   '\nTotal Deaths : '+str(total_deaths_SI)+
   '\nNew Recovered : '+str(new_recovered_SI)+
   '\nTotal Recovered : '+str(total_recovered_SI))

def SO(update, context):
    new_confirmed_SO=(summary["Countries"][153]["NewConfirmed"])
    total_confirmed_SO=(summary["Countries"][153]["TotalConfirmed"])
    new_deaths_SO=(summary["Countries"][153]["NewDeaths"])
    total_deaths_SO=(summary["Countries"][153]["TotalDeaths"])
    new_recovered_SO=(summary["Countries"][153]["NewRecovered"])
    total_recovered_SO=(summary["Countries"][153]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Somalia'
   '\nNew Confirmed : '+str(new_confirmed_SO)+
   '\nTotal Confirmed : '+str(total_confirmed_SO)+
   '\nNew Deaths : '+str(new_deaths_SO)+
   '\nTotal Deaths : '+str(total_deaths_SO)+
   '\nNew Recovered : '+str(new_recovered_SO)+
   '\nTotal Recovered : '+str(total_recovered_SO))

def ZA(update, context):
    new_confirmed_ZA=(summary["Countries"][154]["NewConfirmed"])
    total_confirmed_ZA=(summary["Countries"][154]["TotalConfirmed"])
    new_deaths_ZA=(summary["Countries"][154]["NewDeaths"])
    total_deaths_ZA=(summary["Countries"][154]["TotalDeaths"])
    new_recovered_ZA=(summary["Countries"][154]["NewRecovered"])
    total_recovered_ZA=(summary["Countries"][154]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': South Africa'
   '\nNew Confirmed : '+str(new_confirmed_ZA)+
   '\nTotal Confirmed : '+str(total_confirmed_ZA)+
   '\nNew Deaths : '+str(new_deaths_ZA)+
   '\nTotal Deaths : '+str(total_deaths_ZA)+
   '\nNew Recovered : '+str(new_recovered_ZA)+
   '\nTotal Recovered : '+str(total_recovered_ZA))

def SS(update, context):
    new_confirmed_SS=(summary["Countries"][155]["NewConfirmed"])
    total_confirmed_SS=(summary["Countries"][155]["TotalConfirmed"])
    new_deaths_SS=(summary["Countries"][155]["NewDeaths"])
    total_deaths_SS=(summary["Countries"][155]["TotalDeaths"])
    new_recovered_SS=(summary["Countries"][155]["NewRecovered"])
    total_recovered_SS=(summary["Countries"][155]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': South Sudan'
   '\nNew Confirmed : '+str(new_confirmed_SS)+
   '\nTotal Confirmed : '+str(total_confirmed_SS)+
   '\nNew Deaths : '+str(new_deaths_SS)+
   '\nTotal Deaths : '+str(total_deaths_SS)+
   '\nNew Recovered : '+str(new_recovered_SS)+
   '\nTotal Recovered : '+str(total_recovered_SS))

def ES(update, context):
    new_confirmed_ES=(summary["Countries"][156]["NewConfirmed"])
    total_confirmed_ES=(summary["Countries"][156]["TotalConfirmed"])
    new_deaths_ES=(summary["Countries"][156]["NewDeaths"])
    total_deaths_ES=(summary["Countries"][156]["TotalDeaths"])
    new_recovered_ES=(summary["Countries"][156]["NewRecovered"])
    total_recovered_ES=(summary["Countries"][156]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Spain'
   '\nNew Confirmed : '+str(new_confirmed_ES)+
   '\nTotal Confirmed : '+str(total_confirmed_ES)+
   '\nNew Deaths : '+str(new_deaths_ES)+
   '\nTotal Deaths : '+str(total_deaths_ES)+
   '\nNew Recovered : '+str(new_recovered_ES)+
   '\nTotal Recovered : '+str(total_recovered_ES))

def LK(update, context):
    new_confirmed_LK=(summary["Countries"][157]["NewConfirmed"])
    total_confirmed_LK=(summary["Countries"][157]["TotalConfirmed"])
    new_deaths_LK=(summary["Countries"][157]["NewDeaths"])
    total_deaths_LK=(summary["Countries"][157]["TotalDeaths"])
    new_recovered_LK=(summary["Countries"][157]["NewRecovered"])
    total_recovered_LK=(summary["Countries"][157]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Sri Lanka'
   '\nNew Confirmed : '+str(new_confirmed_LK)+
   '\nTotal Confirmed : '+str(total_confirmed_LK)+
   '\nNew Deaths : '+str(new_deaths_LK)+
   '\nTotal Deaths : '+str(total_deaths_LK)+
   '\nNew Recovered : '+str(new_recovered_LK)+
   '\nTotal Recovered : '+str(total_recovered_LK))

def SD(update, context):
    new_confirmed_SD=(summary["Countries"][158]["NewConfirmed"])
    total_confirmed_SD=(summary["Countries"][158]["TotalConfirmed"])
    new_deaths_SD=(summary["Countries"][158]["NewDeaths"])
    total_deaths_SD=(summary["Countries"][158]["TotalDeaths"])
    new_recovered_SD=(summary["Countries"][158]["NewRecovered"])
    total_recovered_SD=(summary["Countries"][158]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Sudan'
   '\nNew Confirmed : '+str(new_confirmed_SD)+
   '\nTotal Confirmed : '+str(total_confirmed_SD)+
   '\nNew Deaths : '+str(new_deaths_SD)+
   '\nTotal Deaths : '+str(total_deaths_SD)+
   '\nNew Recovered : '+str(new_recovered_SD)+
   '\nTotal Recovered : '+str(total_recovered_SD))

def SR(update, context):
    new_confirmed_SR=(summary["Countries"][159]["NewConfirmed"])
    total_confirmed_SR=(summary["Countries"][159]["TotalConfirmed"])
    new_deaths_SR=(summary["Countries"][159]["NewDeaths"])
    total_deaths_SR=(summary["Countries"][159]["TotalDeaths"])
    new_recovered_SR=(summary["Countries"][159]["NewRecovered"])
    total_recovered_SR=(summary["Countries"][159]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Suriname'
   '\nNew Confirmed : '+str(new_confirmed_SR)+
   '\nTotal Confirmed : '+str(total_confirmed_SR)+
   '\nNew Deaths : '+str(new_deaths_SR)+
   '\nTotal Deaths : '+str(total_deaths_SR)+
   '\nNew Recovered : '+str(new_recovered_SR)+
   '\nTotal Recovered : '+str(total_recovered_SR))

def SZ(update, context):
    new_confirmed_SZ=(summary["Countries"][160]["NewConfirmed"])
    total_confirmed_SZ=(summary["Countries"][160]["TotalConfirmed"])
    new_deaths_SZ=(summary["Countries"][160]["NewDeaths"])
    total_deaths_SZ=(summary["Countries"][160]["TotalDeaths"])
    new_recovered_SZ=(summary["Countries"][160]["NewRecovered"])
    total_recovered_SZ=(summary["Countries"][160]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Swaziland'
   '\nNew Confirmed : '+str(new_confirmed_SZ)+
   '\nTotal Confirmed : '+str(total_confirmed_SZ)+
   '\nNew Deaths : '+str(new_deaths_SZ)+
   '\nTotal Deaths : '+str(total_deaths_SZ)+
   '\nNew Recovered : '+str(new_recovered_SZ)+
   '\nTotal Recovered : '+str(total_recovered_SZ))

def SE(update, context):
    new_confirmed_SE=(summary["Countries"][161]["NewConfirmed"])
    total_confirmed_SE=(summary["Countries"][161]["TotalConfirmed"])
    new_deaths_SE=(summary["Countries"][161]["NewDeaths"])
    total_deaths_SE=(summary["Countries"][161]["TotalDeaths"])
    new_recovered_SE=(summary["Countries"][161]["NewRecovered"])
    total_recovered_SE=(summary["Countries"][161]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Sweden'
   '\nNew Confirmed : '+str(new_confirmed_SE)+
   '\nTotal Confirmed : '+str(total_confirmed_SE)+
   '\nNew Deaths : '+str(new_deaths_SE)+
   '\nTotal Deaths : '+str(total_deaths_SE)+
   '\nNew Recovered : '+str(new_recovered_SE)+
   '\nTotal Recovered : '+str(total_recovered_SE))

def CH(update, context):
    new_confirmed_CH=(summary["Countries"][162]["NewConfirmed"])
    total_confirmed_CH=(summary["Countries"][162]["TotalConfirmed"])
    new_deaths_CH=(summary["Countries"][162]["NewDeaths"])
    total_deaths_CH=(summary["Countries"][162]["TotalDeaths"])
    new_recovered_CH=(summary["Countries"][162]["NewRecovered"])
    total_recovered_CH=(summary["Countries"][162]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Switzerland'
   '\nNew Confirmed : '+str(new_confirmed_CH)+
   '\nTotal Confirmed : '+str(total_confirmed_CH)+
   '\nNew Deaths : '+str(new_deaths_CH)+
   '\nTotal Deaths : '+str(total_deaths_CH)+
   '\nNew Recovered : '+str(new_recovered_CH)+
   '\nTotal Recovered : '+str(total_recovered_CH))

def SY(update, context):
    new_confirmed_SY=(summary["Countries"][163]["NewConfirmed"])
    total_confirmed_SY=(summary["Countries"][163]["TotalConfirmed"])
    new_deaths_SY=(summary["Countries"][163]["NewDeaths"])
    total_deaths_SY=(summary["Countries"][163]["TotalDeaths"])
    new_recovered_SY=(summary["Countries"][163]["NewRecovered"])
    total_recovered_SY=(summary["Countries"][163]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Syrian Arab Republic (Syria)'
   '\nNew Confirmed : '+str(new_confirmed_SY)+
   '\nTotal Confirmed : '+str(total_confirmed_SY)+
   '\nNew Deaths : '+str(new_deaths_SY)+
   '\nTotal Deaths : '+str(total_deaths_SY)+
   '\nNew Recovered : '+str(new_recovered_SY)+
   '\nTotal Recovered : '+str(total_recovered_SY))

def TW(update, context):
    new_confirmed_TW=(summary["Countries"][164]["NewConfirmed"])
    total_confirmed_TW=(summary["Countries"][164]["TotalConfirmed"])
    new_deaths_TW=(summary["Countries"][164]["NewDeaths"])
    total_deaths_TW=(summary["Countries"][164]["TotalDeaths"])
    new_recovered_TW=(summary["Countries"][164]["NewRecovered"])
    total_recovered_TW=(summary["Countries"][164]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Taiwan, Republic of China'
   '\nNew Confirmed : '+str(new_confirmed_TW)+
   '\nTotal Confirmed : '+str(total_confirmed_TW)+
   '\nNew Deaths : '+str(new_deaths_TW)+
   '\nTotal Deaths : '+str(total_deaths_TW)+
   '\nNew Recovered : '+str(new_recovered_TW)+
   '\nTotal Recovered : '+str(total_recovered_TW))

def TJ(update, context):
    new_confirmed_TJ=(summary["Countries"][165]["NewConfirmed"])
    total_confirmed_TJ=(summary["Countries"][165]["TotalConfirmed"])
    new_deaths_TJ=(summary["Countries"][165]["NewDeaths"])
    total_deaths_TJ=(summary["Countries"][165]["TotalDeaths"])
    new_recovered_TJ=(summary["Countries"][165]["NewRecovered"])
    total_recovered_TJ=(summary["Countries"][165]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Tajikistan'
   '\nNew Confirmed : '+str(new_confirmed_TJ)+
   '\nTotal Confirmed : '+str(total_confirmed_TJ)+
   '\nNew Deaths : '+str(new_deaths_TJ)+
   '\nTotal Deaths : '+str(total_deaths_TJ)+
   '\nNew Recovered : '+str(new_recovered_TJ)+
   '\nTotal Recovered : '+str(total_recovered_TJ))

def TZ(update, context):
    new_confirmed_TZ=(summary["Countries"][166]["NewConfirmed"])
    total_confirmed_TZ=(summary["Countries"][166]["TotalConfirmed"])
    new_deaths_TZ=(summary["Countries"][166]["NewDeaths"])
    total_deaths_TZ=(summary["Countries"][166]["TotalDeaths"])
    new_recovered_TZ=(summary["Countries"][166]["NewRecovered"])
    total_recovered_TZ=(summary["Countries"][166]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Tanzania, United Republic of'
   '\nNew Confirmed : '+str(new_confirmed_TZ)+
   '\nTotal Confirmed : '+str(total_confirmed_TZ)+
   '\nNew Deaths : '+str(new_deaths_TZ)+
   '\nTotal Deaths : '+str(total_deaths_TZ)+
   '\nNew Recovered : '+str(new_recovered_TZ)+
   '\nTotal Recovered : '+str(total_recovered_TZ))

def TH(update, context):
    new_confirmed_TH=(summary["Countries"][167]["NewConfirmed"])
    total_confirmed_TH=(summary["Countries"][167]["TotalConfirmed"])
    new_deaths_TH=(summary["Countries"][167]["NewDeaths"])
    total_deaths_TH=(summary["Countries"][167]["TotalDeaths"])
    new_recovered_TH=(summary["Countries"][167]["NewRecovered"])
    total_recovered_TH=(summary["Countries"][167]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Thailand'
   '\nNew Confirmed : '+str(new_confirmed_TH)+
   '\nTotal Confirmed : '+str(total_confirmed_TH)+
   '\nNew Deaths : '+str(new_deaths_TH)+
   '\nTotal Deaths : '+str(total_deaths_TH)+
   '\nNew Recovered : '+str(new_recovered_TH)+
   '\nTotal Recovered : '+str(total_recovered_TH))

def TL(update, context):
    new_confirmed_TL=(summary["Countries"][168]["NewConfirmed"])
    total_confirmed_TL=(summary["Countries"][168]["TotalConfirmed"])
    new_deaths_TL=(summary["Countries"][168]["NewDeaths"])
    total_deaths_TL=(summary["Countries"][168]["TotalDeaths"])
    new_recovered_TL=(summary["Countries"][168]["NewRecovered"])
    total_recovered_TL=(summary["Countries"][168]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Timor-Leste'
   '\nNew Confirmed : '+str(new_confirmed_TL)+
   '\nTotal Confirmed : '+str(total_confirmed_TL)+
   '\nNew Deaths : '+str(new_deaths_TL)+
   '\nTotal Deaths : '+str(total_deaths_TL)+
   '\nNew Recovered : '+str(new_recovered_TL)+
   '\nTotal Recovered : '+str(total_recovered_TL))

def TG(update, context):
    new_confirmed_TG=(summary["Countries"][169]["NewConfirmed"])
    total_confirmed_TG=(summary["Countries"][169]["TotalConfirmed"])
    new_deaths_TG=(summary["Countries"][169]["NewDeaths"])
    total_deaths_TG=(summary["Countries"][169]["TotalDeaths"])
    new_recovered_TG=(summary["Countries"][169]["NewRecovered"])
    total_recovered_TG=(summary["Countries"][169]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Togo'
   '\nNew Confirmed : '+str(new_confirmed_TG)+
   '\nTotal Confirmed : '+str(total_confirmed_TG)+
   '\nNew Deaths : '+str(new_deaths_TG)+
   '\nTotal Deaths : '+str(total_deaths_TG)+
   '\nNew Recovered : '+str(new_recovered_TG)+
   '\nTotal Recovered : '+str(total_recovered_TG))

def TT(update, context):
    new_confirmed_TT=(summary["Countries"][170]["NewConfirmed"])
    total_confirmed_TT=(summary["Countries"][170]["TotalConfirmed"])
    new_deaths_TT=(summary["Countries"][170]["NewDeaths"])
    total_deaths_TT=(summary["Countries"][170]["TotalDeaths"])
    new_recovered_TT=(summary["Countries"][170]["NewRecovered"])
    total_recovered_TT=(summary["Countries"][170]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Trinidad and Tobago'
   '\nNew Confirmed : '+str(new_confirmed_TT)+
   '\nTotal Confirmed : '+str(total_confirmed_TT)+
   '\nNew Deaths : '+str(new_deaths_TT)+
   '\nTotal Deaths : '+str(total_deaths_TT)+
   '\nNew Recovered : '+str(new_recovered_TT)+
   '\nTotal Recovered : '+str(total_recovered_TT))

def TN(update, context):
    new_confirmed_TN=(summary["Countries"][171]["NewConfirmed"])
    total_confirmed_TN=(summary["Countries"][171]["TotalConfirmed"])
    new_deaths_TN=(summary["Countries"][171]["NewDeaths"])
    total_deaths_TN=(summary["Countries"][171]["TotalDeaths"])
    new_recovered_TN=(summary["Countries"][171]["NewRecovered"])
    total_recovered_TN=(summary["Countries"][171]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Tunisia'
   '\nNew Confirmed : '+str(new_confirmed_TN)+
   '\nTotal Confirmed : '+str(total_confirmed_TN)+
   '\nNew Deaths : '+str(new_deaths_TN)+
   '\nTotal Deaths : '+str(total_deaths_TN)+
   '\nNew Recovered : '+str(new_recovered_TN)+
   '\nTotal Recovered : '+str(total_recovered_TN))

def TR(update, context):
    new_confirmed_TR=(summary["Countries"][172]["NewConfirmed"])
    total_confirmed_TR=(summary["Countries"][172]["TotalConfirmed"])
    new_deaths_TR=(summary["Countries"][172]["NewDeaths"])
    total_deaths_TR=(summary["Countries"][172]["TotalDeaths"])
    new_recovered_TR=(summary["Countries"][172]["NewRecovered"])
    total_recovered_TR=(summary["Countries"][172]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Turkey'
   '\nNew Confirmed : '+str(new_confirmed_TR)+
   '\nTotal Confirmed : '+str(total_confirmed_TR)+
   '\nNew Deaths : '+str(new_deaths_TR)+
   '\nTotal Deaths : '+str(total_deaths_TR)+
   '\nNew Recovered : '+str(new_recovered_TR)+
   '\nTotal Recovered : '+str(total_recovered_TR))

def UG(update, context):
    new_confirmed_UG=(summary["Countries"][173]["NewConfirmed"])
    total_confirmed_UG=(summary["Countries"][173]["TotalConfirmed"])
    new_deaths_UG=(summary["Countries"][173]["NewDeaths"])
    total_deaths_UG=(summary["Countries"][173]["TotalDeaths"])
    new_recovered_UG=(summary["Countries"][173]["NewRecovered"])
    total_recovered_UG=(summary["Countries"][173]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Uganda'
   '\nNew Confirmed : '+str(new_confirmed_UG)+
   '\nTotal Confirmed : '+str(total_confirmed_UG)+
   '\nNew Deaths : '+str(new_deaths_UG)+
   '\nTotal Deaths : '+str(total_deaths_UG)+
   '\nNew Recovered : '+str(new_recovered_UG)+
   '\nTotal Recovered : '+str(total_recovered_UG))

def UA(update, context):
    new_confirmed_UA=(summary["Countries"][174]["NewConfirmed"])
    total_confirmed_UA=(summary["Countries"][174]["TotalConfirmed"])
    new_deaths_UA=(summary["Countries"][174]["NewDeaths"])
    total_deaths_UA=(summary["Countries"][174]["TotalDeaths"])
    new_recovered_UA=(summary["Countries"][174]["NewRecovered"])
    total_recovered_UA=(summary["Countries"][174]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Ukraine'
   '\nNew Confirmed : '+str(new_confirmed_UA)+
   '\nTotal Confirmed : '+str(total_confirmed_UA)+
   '\nNew Deaths : '+str(new_deaths_UA)+
   '\nTotal Deaths : '+str(total_deaths_UA)+
   '\nNew Recovered : '+str(new_recovered_UA)+
   '\nTotal Recovered : '+str(total_recovered_UA))

def AE(update, context):
    new_confirmed_AE=(summary["Countries"][175]["NewConfirmed"])
    total_confirmed_AE=(summary["Countries"][175]["TotalConfirmed"])
    new_deaths_AE=(summary["Countries"][175]["NewDeaths"])
    total_deaths_AE=(summary["Countries"][175]["TotalDeaths"])
    new_recovered_AE=(summary["Countries"][175]["NewRecovered"])
    total_recovered_AE=(summary["Countries"][175]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': United Arab Emirates'
   '\nNew Confirmed : '+str(new_confirmed_AE)+
   '\nTotal Confirmed : '+str(total_confirmed_AE)+
   '\nNew Deaths : '+str(new_deaths_AE)+
   '\nTotal Deaths : '+str(total_deaths_AE)+
   '\nNew Recovered : '+str(new_recovered_AE)+
   '\nTotal Recovered : '+str(total_recovered_AE))

def GB(update, context):
    new_confirmed_GB=(summary["Countries"][176]["NewConfirmed"])
    total_confirmed_GB=(summary["Countries"][176]["TotalConfirmed"])
    new_deaths_GB=(summary["Countries"][176]["NewDeaths"])
    total_deaths_GB=(summary["Countries"][176]["TotalDeaths"])
    new_recovered_GB=(summary["Countries"][176]["NewRecovered"])
    total_recovered_GB=(summary["Countries"][176]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': United Kingdom'
   '\nNew Confirmed : '+str(new_confirmed_GB)+
   '\nTotal Confirmed : '+str(total_confirmed_GB)+
   '\nNew Deaths : '+str(new_deaths_GB)+
   '\nTotal Deaths : '+str(total_deaths_GB)+
   '\nNew Recovered : '+str(new_recovered_GB)+
   '\nTotal Recovered : '+str(total_recovered_GB))

def US(update, context):
    new_confirmed_US=(summary["Countries"][177]["NewConfirmed"])
    total_confirmed_US=(summary["Countries"][177]["TotalConfirmed"])
    new_deaths_US=(summary["Countries"][177]["NewDeaths"])
    total_deaths_US=(summary["Countries"][177]["TotalDeaths"])
    new_recovered_US=(summary["Countries"][177]["NewRecovered"])
    total_recovered_US=(summary["Countries"][177]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': United States of America'
   '\nNew Confirmed : '+str(new_confirmed_US)+
   '\nTotal Confirmed : '+str(total_confirmed_US)+
   '\nNew Deaths : '+str(new_deaths_US)+
   '\nTotal Deaths : '+str(total_deaths_US)+
   '\nNew Recovered : '+str(new_recovered_US)+
   '\nTotal Recovered : '+str(total_recovered_US))

def UY(update, context):
    new_confirmed_UY=(summary["Countries"][178]["NewConfirmed"])
    total_confirmed_UY=(summary["Countries"][178]["TotalConfirmed"])
    new_deaths_UY=(summary["Countries"][178]["NewDeaths"])
    total_deaths_UY=(summary["Countries"][178]["TotalDeaths"])
    new_recovered_UY=(summary["Countries"][178]["NewRecovered"])
    total_recovered_UY=(summary["Countries"][178]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Uruguay'
   '\nNew Confirmed : '+str(new_confirmed_UY)+
   '\nTotal Confirmed : '+str(total_confirmed_UY)+
   '\nNew Deaths : '+str(new_deaths_UY)+
   '\nTotal Deaths : '+str(total_deaths_UY)+
   '\nNew Recovered : '+str(new_recovered_UY)+
   '\nTotal Recovered : '+str(total_recovered_UY))

def UZ(update, context):
    new_confirmed_UZ=(summary["Countries"][179]["NewConfirmed"])
    total_confirmed_UZ=(summary["Countries"][179]["TotalConfirmed"])
    new_deaths_UZ=(summary["Countries"][179]["NewDeaths"])
    total_deaths_UZ=(summary["Countries"][179]["TotalDeaths"])
    new_recovered_UZ=(summary["Countries"][179]["NewRecovered"])
    total_recovered_UZ=(summary["Countries"][179]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Uzbekistan'
   '\nNew Confirmed : '+str(new_confirmed_UZ)+
   '\nTotal Confirmed : '+str(total_confirmed_UZ)+
   '\nNew Deaths : '+str(new_deaths_UZ)+
   '\nTotal Deaths : '+str(total_deaths_UZ)+
   '\nNew Recovered : '+str(new_recovered_UZ)+
   '\nTotal Recovered : '+str(total_recovered_UZ))

def VE(update, context):
    new_confirmed_VE=(summary["Countries"][180]["NewConfirmed"])
    total_confirmed_VE=(summary["Countries"][180]["TotalConfirmed"])
    new_deaths_VE=(summary["Countries"][180]["NewDeaths"])
    total_deaths_VE=(summary["Countries"][180]["TotalDeaths"])
    new_recovered_VE=(summary["Countries"][180]["NewRecovered"])
    total_recovered_VE=(summary["Countries"][180]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Venezuela (Bolivarian Republic)'
   '\nNew Confirmed : '+str(new_confirmed_VE)+
   '\nTotal Confirmed : '+str(total_confirmed_VE)+
   '\nNew Deaths : '+str(new_deaths_VE)+
   '\nTotal Deaths : '+str(total_deaths_VE)+
   '\nNew Recovered : '+str(new_recovered_VE)+
   '\nTotal Recovered : '+str(total_recovered_VE))

def VN(update, context):
    new_confirmed_VN=(summary["Countries"][181]["NewConfirmed"])
    total_confirmed_VN=(summary["Countries"][181]["TotalConfirmed"])
    new_deaths_VN=(summary["Countries"][181]["NewDeaths"])
    total_deaths_VN=(summary["Countries"][181]["TotalDeaths"])
    new_recovered_VN=(summary["Countries"][181]["NewRecovered"])
    total_recovered_VN=(summary["Countries"][181]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Viet Nam'
   '\nNew Confirmed : '+str(new_confirmed_VN)+
   '\nTotal Confirmed : '+str(total_confirmed_VN)+
   '\nNew Deaths : '+str(new_deaths_VN)+
   '\nTotal Deaths : '+str(total_deaths_VN)+
   '\nNew Recovered : '+str(new_recovered_VN)+
   '\nTotal Recovered : '+str(total_recovered_VN))

def EH(update, context):
    new_confirmed_EH=(summary["Countries"][182]["NewConfirmed"])
    total_confirmed_EH=(summary["Countries"][182]["TotalConfirmed"])
    new_deaths_EH=(summary["Countries"][182]["NewDeaths"])
    total_deaths_EH=(summary["Countries"][182]["TotalDeaths"])
    new_recovered_EH=(summary["Countries"][182]["NewRecovered"])
    total_recovered_EH=(summary["Countries"][182]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Western Sahara'
   '\nNew Confirmed : '+str(new_confirmed_EH)+
   '\nTotal Confirmed : '+str(total_confirmed_EH)+
   '\nNew Deaths : '+str(new_deaths_EH)+
   '\nTotal Deaths : '+str(total_deaths_EH)+
   '\nNew Recovered : '+str(new_recovered_EH)+
   '\nTotal Recovered : '+str(total_recovered_EH))

def YE(update, context):
    new_confirmed_YE=(summary["Countries"][183]["NewConfirmed"])
    total_confirmed_YE=(summary["Countries"][183]["TotalConfirmed"])
    new_deaths_YE=(summary["Countries"][183]["NewDeaths"])
    total_deaths_YE=(summary["Countries"][183]["TotalDeaths"])
    new_recovered_YE=(summary["Countries"][183]["NewRecovered"])
    total_recovered_YE=(summary["Countries"][183]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Yemen'
   '\nNew Confirmed : '+str(new_confirmed_YE)+
   '\nTotal Confirmed : '+str(total_confirmed_YE)+
   '\nNew Deaths : '+str(new_deaths_YE)+
   '\nTotal Deaths : '+str(total_deaths_YE)+
   '\nNew Recovered : '+str(new_recovered_YE)+
   '\nTotal Recovered : '+str(total_recovered_YE))

def ZM(update, context):
    new_confirmed_ZM=(summary["Countries"][184]["NewConfirmed"])
    total_confirmed_ZM=(summary["Countries"][184]["TotalConfirmed"])
    new_deaths_ZM=(summary["Countries"][184]["NewDeaths"])
    total_deaths_ZM=(summary["Countries"][184]["TotalDeaths"])
    new_recovered_ZM=(summary["Countries"][184]["NewRecovered"])
    total_recovered_ZM=(summary["Countries"][184]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Zambia'
   '\nNew Confirmed : '+str(new_confirmed_ZM)+
   '\nTotal Confirmed : '+str(total_confirmed_ZM)+
   '\nNew Deaths : '+str(new_deaths_ZM)+
   '\nTotal Deaths : '+str(total_deaths_ZM)+
   '\nNew Recovered : '+str(new_recovered_ZM)+
   '\nTotal Recovered : '+str(total_recovered_ZM))

def ZW(update, context):
    new_confirmed_ZW=(summary["Countries"][185]["NewConfirmed"])
    total_confirmed_ZW=(summary["Countries"][185]["TotalConfirmed"])
    new_deaths_ZW=(summary["Countries"][185]["NewDeaths"])
    total_deaths_ZW=(summary["Countries"][185]["TotalDeaths"])
    new_recovered_ZW=(summary["Countries"][185]["NewRecovered"])
    total_recovered_ZW=(summary["Countries"][185]["TotalRecovered"])
    update.message.reply_text('Corona Statistics' ': Zimbabwe'
   '\nNew Confirmed : '+str(new_confirmed_ZW)+
   '\nTotal Confirmed : '+str(total_confirmed_ZW)+
   '\nNew Deaths : '+str(new_deaths_ZW)+
   '\nTotal Deaths : '+str(total_deaths_ZW)+
   '\nNew Recovered : '+str(new_recovered_ZW)+
   '\nTotal Recovered : '+str(total_recovered_ZW))

def help(update, context):
    update.message.reply_text("Hi! , I\'m Corona Chan!\nSo what I basically do is, I give you\nCorona Statistics.\nTo know Global Stats do /global\nTo know the stats of a specific country, do /<country code>\nWondering where to find country codes?\nDon\'t Worry! We got you covered .\nSimply do /countrycodes\nA message with all country codes will pop up.\nUse those country codes to gt the statistics of a country .\nI hope you guys will enjoy this Bot.\nArigatou!") 

def about(update, context):
    update.message.reply_text("Corona Chan will get you Corona Statistics from all around the world.\nDeveloper : @iLEWDloli\nDeveloped in Python using python-telegram-bot\nMade possible due to Coronavirus COVID19 API\nIf you liked this Bot and want to support me\n Then donate here-->https://paypal.me/adenosinetp10")

def main():
    bot_token = os.environ.get("BOT_TOKEN","")
    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('global',global1))
    dp.add_handler(CommandHandler('countrycodes',countrycode))
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(CommandHandler('about',about))
    dp.add_handler(CommandHandler("AF",AF))
    dp.add_handler(CommandHandler("AL",AL))
    dp.add_handler(CommandHandler("DZ",DZ))
    dp.add_handler(CommandHandler("AD",AD))
    dp.add_handler(CommandHandler("AO",AO))
    dp.add_handler(CommandHandler("AG",AG))
    dp.add_handler(CommandHandler("AR",AR))
    dp.add_handler(CommandHandler("AM",AM))
    dp.add_handler(CommandHandler("AU",AU))
    dp.add_handler(CommandHandler("AT",AT))
    dp.add_handler(CommandHandler("AZ",AZ))
    dp.add_handler(CommandHandler("BS",BS))
    dp.add_handler(CommandHandler("BH",BH))
    dp.add_handler(CommandHandler("BB",BB))
    dp.add_handler(CommandHandler("BY",BY))
    dp.add_handler(CommandHandler("BE",BE))
    dp.add_handler(CommandHandler("BZ",BZ))
    dp.add_handler(CommandHandler("BJ",BJ))
    dp.add_handler(CommandHandler("BT",BT))
    dp.add_handler(CommandHandler("BO",BO))
    dp.add_handler(CommandHandler("BA",BA))
    dp.add_handler(CommandHandler("BW",BW))
    dp.add_handler(CommandHandler("BR",BR))
    dp.add_handler(CommandHandler("BN",BN))
    dp.add_handler(CommandHandler("BG",BG))
    dp.add_handler(CommandHandler("BF",BF))
    dp.add_handler(CommandHandler("BI",BI))
    dp.add_handler(CommandHandler("KH",KH))
    dp.add_handler(CommandHandler("CM",CM))
    dp.add_handler(CommandHandler("CA",CA))
    dp.add_handler(CommandHandler("CV",CV))
    dp.add_handler(CommandHandler("CF",CF))
    dp.add_handler(CommandHandler("TD",TD))
    dp.add_handler(CommandHandler("CL",CL))
    dp.add_handler(CommandHandler("CN",CN))
    dp.add_handler(CommandHandler("CO",CO))
    dp.add_handler(CommandHandler("KM",KM))
    dp.add_handler(CommandHandler("CG",CG))
    dp.add_handler(CommandHandler("CD",CD))
    dp.add_handler(CommandHandler("CR",CR))
    dp.add_handler(CommandHandler("HR",HR))
    dp.add_handler(CommandHandler("CU",CU))
    dp.add_handler(CommandHandler("CY",CY))
    dp.add_handler(CommandHandler("CZ",CZ))
    dp.add_handler(CommandHandler("CI",CI))
    dp.add_handler(CommandHandler("DK",DK))
    dp.add_handler(CommandHandler("DJ",DJ))
    dp.add_handler(CommandHandler("DM",DM))
    dp.add_handler(CommandHandler("DO",DO))
    dp.add_handler(CommandHandler("EC",EC))
    dp.add_handler(CommandHandler("EG",EG))
    dp.add_handler(CommandHandler("SV",SV))
    dp.add_handler(CommandHandler("GQ",GQ))
    dp.add_handler(CommandHandler("ER",ER))
    dp.add_handler(CommandHandler("EE",EE))
    dp.add_handler(CommandHandler("ET",ET))
    dp.add_handler(CommandHandler("FJ",FJ))
    dp.add_handler(CommandHandler("FI",FI))
    dp.add_handler(CommandHandler("FR",FR))
    dp.add_handler(CommandHandler("GA",GA))
    dp.add_handler(CommandHandler("GM",GM))
    dp.add_handler(CommandHandler("GE",GE))
    dp.add_handler(CommandHandler("DE",DE))
    dp.add_handler(CommandHandler("GH",GH))
    dp.add_handler(CommandHandler("GR",GR))
    dp.add_handler(CommandHandler("GD",GD))
    dp.add_handler(CommandHandler("GT",GT))
    dp.add_handler(CommandHandler("GN",GN))
    dp.add_handler(CommandHandler("GW",GW))
    dp.add_handler(CommandHandler("GY",GY))
    dp.add_handler(CommandHandler("HT",HT))
    dp.add_handler(CommandHandler("VA",VA))
    dp.add_handler(CommandHandler("HN",HN))
    dp.add_handler(CommandHandler("HU",HU))
    dp.add_handler(CommandHandler("IS",IS))
    dp.add_handler(CommandHandler("IN",IN))
    dp.add_handler(CommandHandler("ID",ID))
    dp.add_handler(CommandHandler("IR",IR))
    dp.add_handler(CommandHandler("IQ",IQ))
    dp.add_handler(CommandHandler("IE",IE))
    dp.add_handler(CommandHandler("IL",IL))
    dp.add_handler(CommandHandler("IT",IT))
    dp.add_handler(CommandHandler("JM",JM))
    dp.add_handler(CommandHandler("JP",JP))
    dp.add_handler(CommandHandler("JO",JO))
    dp.add_handler(CommandHandler("KZ",KZ))
    dp.add_handler(CommandHandler("KE",KE))
    dp.add_handler(CommandHandler("KR",KR))
    dp.add_handler(CommandHandler("KW",KW))
    dp.add_handler(CommandHandler("KG",KG))
    dp.add_handler(CommandHandler("LA",LA))
    dp.add_handler(CommandHandler("LV",LV))
    dp.add_handler(CommandHandler("LB",LB))
    dp.add_handler(CommandHandler("LS",LS))
    dp.add_handler(CommandHandler("LR",LR))
    dp.add_handler(CommandHandler("LY",LY))
    dp.add_handler(CommandHandler("LI",LI))
    dp.add_handler(CommandHandler("LT",LT))
    dp.add_handler(CommandHandler("LU",LU))
    dp.add_handler(CommandHandler("MK",MK))
    dp.add_handler(CommandHandler("MG",MG))
    dp.add_handler(CommandHandler("MW",MW))
    dp.add_handler(CommandHandler("MY",MY))
    dp.add_handler(CommandHandler("MV",MV))
    dp.add_handler(CommandHandler("ML",ML))
    dp.add_handler(CommandHandler("MT",MT))
    dp.add_handler(CommandHandler("MR",MR))
    dp.add_handler(CommandHandler("MU",MU))
    dp.add_handler(CommandHandler("MX",MX))
    dp.add_handler(CommandHandler("MD",MD))
    dp.add_handler(CommandHandler("MC",MC))
    dp.add_handler(CommandHandler("MN",MN))
    dp.add_handler(CommandHandler("ME",ME))
    dp.add_handler(CommandHandler("MA",MA))
    dp.add_handler(CommandHandler("MZ",MZ))
    dp.add_handler(CommandHandler("MM",MM))
    dp.add_handler(CommandHandler("NA",NA))
    dp.add_handler(CommandHandler("NP",NP))
    dp.add_handler(CommandHandler("NL",NL))
    dp.add_handler(CommandHandler("NZ",NZ))
    dp.add_handler(CommandHandler("NI",NI))
    dp.add_handler(CommandHandler("NE",NE))
    dp.add_handler(CommandHandler("NG",NG))
    dp.add_handler(CommandHandler("NO",NO))
    dp.add_handler(CommandHandler("OM",OM))
    dp.add_handler(CommandHandler("PK",PK))
    dp.add_handler(CommandHandler("PS",PS))
    dp.add_handler(CommandHandler("PA",PA))
    dp.add_handler(CommandHandler("PG",PG))
    dp.add_handler(CommandHandler("PY",PY))
    dp.add_handler(CommandHandler("PE",PE))
    dp.add_handler(CommandHandler("PH",PH))
    dp.add_handler(CommandHandler("PL",PL))
    dp.add_handler(CommandHandler("PT",PT))
    dp.add_handler(CommandHandler("QA",QA))
    dp.add_handler(CommandHandler("XK",XK))
    dp.add_handler(CommandHandler("RO",RO))
    dp.add_handler(CommandHandler("RU",RU))
    dp.add_handler(CommandHandler("RW",RW))
    dp.add_handler(CommandHandler("KN",KN))
    dp.add_handler(CommandHandler("LC",LC))
    dp.add_handler(CommandHandler("VC",VC))
    dp.add_handler(CommandHandler("SM",SM))
    dp.add_handler(CommandHandler("ST",ST))
    dp.add_handler(CommandHandler("SA",SA))
    dp.add_handler(CommandHandler("SN",SN))
    dp.add_handler(CommandHandler("RS",RS))
    dp.add_handler(CommandHandler("SC",SC))
    dp.add_handler(CommandHandler("SL",SL))
    dp.add_handler(CommandHandler("SG",SG))
    dp.add_handler(CommandHandler("SK",SK))
    dp.add_handler(CommandHandler("SI",SI))
    dp.add_handler(CommandHandler("SO",SO))
    dp.add_handler(CommandHandler("ZA",ZA))
    dp.add_handler(CommandHandler("SS",SS))
    dp.add_handler(CommandHandler("ES",ES))
    dp.add_handler(CommandHandler("LK",LK))
    dp.add_handler(CommandHandler("SD",SD))
    dp.add_handler(CommandHandler("SR",SR))
    dp.add_handler(CommandHandler("SZ",SZ))
    dp.add_handler(CommandHandler("SE",SE))
    dp.add_handler(CommandHandler("CH",CH))
    dp.add_handler(CommandHandler("SY",SY))
    dp.add_handler(CommandHandler("TW",TW))
    dp.add_handler(CommandHandler("TJ",TJ))
    dp.add_handler(CommandHandler("TZ",TZ))
    dp.add_handler(CommandHandler("TH",TH))
    dp.add_handler(CommandHandler("TL",TL))
    dp.add_handler(CommandHandler("TG",TG))
    dp.add_handler(CommandHandler("TT",TT))
    dp.add_handler(CommandHandler("TN",TN))
    dp.add_handler(CommandHandler("TR",TR))
    dp.add_handler(CommandHandler("UG",UG))
    dp.add_handler(CommandHandler("UA",UA))
    dp.add_handler(CommandHandler("AE",AE))
    dp.add_handler(CommandHandler("GB",GB))
    dp.add_handler(CommandHandler("US",US))
    dp.add_handler(CommandHandler("UY",UY))
    dp.add_handler(CommandHandler("UZ",UZ))
    dp.add_handler(CommandHandler("VE",VE))
    dp.add_handler(CommandHandler("VN",VN))
    dp.add_handler(CommandHandler("EH",EH))
    dp.add_handler(CommandHandler("YE",YE))
    dp.add_handler(CommandHandler("ZM",ZM))
    dp.add_handler(CommandHandler("ZW",ZW))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
