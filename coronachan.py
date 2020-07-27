from telegram.ext import Updater,CommandHandler,MessageHandler
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
import telegram
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
    update.message.reply_text('<b>Corona Statistics:</b><pre>Afghanistan</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_AF)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_AF)+'</pre>'       
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_AF)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_AF)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_AF)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_AF)+'</pre>',parse_mode='HTML')
def AL(update, context):
    new_confirmed_AL=(summary["Countries"][1]["NewConfirmed"])
    total_confirmed_AL=(summary["Countries"][1]["TotalConfirmed"])
    new_deaths_AL=(summary["Countries"][1]["NewDeaths"])
    total_deaths_AL=(summary["Countries"][1]["TotalDeaths"])
    new_recovered_AL=(summary["Countries"][1]["NewRecovered"])
    total_recovered_AL=(summary["Countries"][1]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Albania</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_AL)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_AL)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_AL)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_AL)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_AL)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_AL)+'</pre>',parse_mode='HTML')
def DZ(update, context):
    new_confirmed_DZ=(summary["Countries"][2]["NewConfirmed"])
    total_confirmed_DZ=(summary["Countries"][2]["TotalConfirmed"])
    new_deaths_DZ=(summary["Countries"][2]["NewDeaths"])
    total_deaths_DZ=(summary["Countries"][2]["TotalDeaths"])
    new_recovered_DZ=(summary["Countries"][2]["NewRecovered"])
    total_recovered_DZ=(summary["Countries"][2]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Algeria</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_DZ)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_DZ)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_DZ)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_DZ)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_DZ)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_DZ)+'</pre>',parse_mode='HTML')
def AD(update, context):
    new_confirmed_AD=(summary["Countries"][3]["NewConfirmed"])
    total_confirmed_AD=(summary["Countries"][3]["TotalConfirmed"])
    new_deaths_AD=(summary["Countries"][3]["NewDeaths"])
    total_deaths_AD=(summary["Countries"][3]["TotalDeaths"])
    new_recovered_AD=(summary["Countries"][3]["NewRecovered"])
    total_recovered_AD=(summary["Countries"][3]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Andorra</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_AD)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_AD)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_AD)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_AD)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_AD)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_AD)+'</pre>',parse_mode='HTML')
def AO(update, context):
    new_confirmed_AO=(summary["Countries"][4]["NewConfirmed"])
    total_confirmed_AO=(summary["Countries"][4]["TotalConfirmed"])
    new_deaths_AO=(summary["Countries"][4]["NewDeaths"])
    total_deaths_AO=(summary["Countries"][4]["TotalDeaths"])
    new_recovered_AO=(summary["Countries"][4]["NewRecovered"])
    total_recovered_AO=(summary["Countries"][4]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Angola</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_AO)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_AO)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_AO)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_AO)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_AO)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_AO)+'</pre>',parse_mode='HTML')
def AG(update, context):
    new_confirmed_AG=(summary["Countries"][5]["NewConfirmed"])
    total_confirmed_AG=(summary["Countries"][5]["TotalConfirmed"])
    new_deaths_AG=(summary["Countries"][5]["NewDeaths"])
    total_deaths_AG=(summary["Countries"][5]["TotalDeaths"])
    new_recovered_AG=(summary["Countries"][5]["NewRecovered"])
    total_recovered_AG=(summary["Countries"][5]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Antigua and Barbuda</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_AG)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_AG)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_AG)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_AG)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_AG)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_AG)+'</pre>',parse_mode='HTML')
def AR(update, context):
    new_confirmed_AR=(summary["Countries"][6]["NewConfirmed"])
    total_confirmed_AR=(summary["Countries"][6]["TotalConfirmed"])
    new_deaths_AR=(summary["Countries"][6]["NewDeaths"])
    total_deaths_AR=(summary["Countries"][6]["TotalDeaths"])
    new_recovered_AR=(summary["Countries"][6]["NewRecovered"])
    total_recovered_AR=(summary["Countries"][6]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Argentina</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_AR)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_AR)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_AR)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_AR)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_AR)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_AR)+'</pre>',parse_mode='HTML')
def AM(update, context):
    new_confirmed_AM=(summary["Countries"][7]["NewConfirmed"])
    total_confirmed_AM=(summary["Countries"][7]["TotalConfirmed"])
    new_deaths_AM=(summary["Countries"][7]["NewDeaths"])
    total_deaths_AM=(summary["Countries"][7]["TotalDeaths"])
    new_recovered_AM=(summary["Countries"][7]["NewRecovered"])
    total_recovered_AM=(summary["Countries"][7]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Armenia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_AM)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_AM)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_AM)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_AM)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_AM)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_AM)+'</pre>',parse_mode='HTML')
def AU(update, context):
    new_confirmed_AU=(summary["Countries"][8]["NewConfirmed"])
    total_confirmed_AU=(summary["Countries"][8]["TotalConfirmed"])
    new_deaths_AU=(summary["Countries"][8]["NewDeaths"])
    total_deaths_AU=(summary["Countries"][8]["TotalDeaths"])
    new_recovered_AU=(summary["Countries"][8]["NewRecovered"])
    total_recovered_AU=(summary["Countries"][8]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Australia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_AU)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_AU)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_AU)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_AU)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_AU)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_AU)+'</pre>',parse_mode='HTML')
def AT(update, context):
    new_confirmed_AT=(summary["Countries"][9]["NewConfirmed"])
    total_confirmed_AT=(summary["Countries"][9]["TotalConfirmed"])
    new_deaths_AT=(summary["Countries"][9]["NewDeaths"])
    total_deaths_AT=(summary["Countries"][9]["TotalDeaths"])
    new_recovered_AT=(summary["Countries"][9]["NewRecovered"])
    total_recovered_AT=(summary["Countries"][9]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Austria</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_AT)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_AT)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_AT)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_AT)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_AT)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_AT)+'</pre>',parse_mode='HTML')
def AZ(update, context):
    new_confirmed_AZ=(summary["Countries"][10]["NewConfirmed"])
    total_confirmed_AZ=(summary["Countries"][10]["TotalConfirmed"])
    new_deaths_AZ=(summary["Countries"][10]["NewDeaths"])
    total_deaths_AZ=(summary["Countries"][10]["TotalDeaths"])
    new_recovered_AZ=(summary["Countries"][10]["NewRecovered"])
    total_recovered_AZ=(summary["Countries"][10]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Azerbaijan</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_AZ)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_AZ)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_AZ)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_AZ)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_AZ)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_AZ)+'</pre>',parse_mode='HTML')
def BS(update, context):
    new_confirmed_BS=(summary["Countries"][11]["NewConfirmed"])
    total_confirmed_BS=(summary["Countries"][11]["TotalConfirmed"])
    new_deaths_BS=(summary["Countries"][11]["NewDeaths"])
    total_deaths_BS=(summary["Countries"][11]["TotalDeaths"])
    new_recovered_BS=(summary["Countries"][11]["NewRecovered"])
    total_recovered_BS=(summary["Countries"][11]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Bahamas</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_BS)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_BS)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_BS)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_BS)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_BS)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_BS)+'</pre>',parse_mode='HTML')
def BH(update, context):
    new_confirmed_BH=(summary["Countries"][12]["NewConfirmed"])
    total_confirmed_BH=(summary["Countries"][12]["TotalConfirmed"])
    new_deaths_BH=(summary["Countries"][12]["NewDeaths"])
    total_deaths_BH=(summary["Countries"][12]["TotalDeaths"])
    new_recovered_BH=(summary["Countries"][12]["NewRecovered"])
    total_recovered_BH=(summary["Countries"][12]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Bahrain</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_BH)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_BH)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_BH)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_BH)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_BH)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_BH)+'</pre>',parse_mode='HTML')
def BD(update, context):
    new_confirmed_BD=(summary["Countries"][13]["NewConfirmed"])
    total_confirmed_BD=(summary["Countries"][13]["TotalConfirmed"])
    new_deaths_BD=(summary["Countries"][13]["NewDeaths"])
    total_deaths_BD=(summary["Countries"][13]["TotalDeaths"])
    new_recovered_BD=(summary["Countries"][13]["NewRecovered"])
    total_recovered_BD=(summary["Countries"][13]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Bangladesh</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_BD)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_BD)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_BD)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_BD)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_BD)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_BD)+'</pre>',parse_mode='HTML')
def BB(update, context):
    new_confirmed_BB=(summary["Countries"][14]["NewConfirmed"])
    total_confirmed_BB=(summary["Countries"][14]["TotalConfirmed"])
    new_deaths_BB=(summary["Countries"][14]["NewDeaths"])
    total_deaths_BB=(summary["Countries"][14]["TotalDeaths"])
    new_recovered_BB=(summary["Countries"][14]["NewRecovered"])
    total_recovered_BB=(summary["Countries"][14]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Barbados</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_BB)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_BB)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_BB)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_BB)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_BB)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_BB)+'</pre>',parse_mode='HTML')
def BY(update, context):
    new_confirmed_BY=(summary["Countries"][15]["NewConfirmed"])
    total_confirmed_BY=(summary["Countries"][15]["TotalConfirmed"])
    new_deaths_BY=(summary["Countries"][15]["NewDeaths"])
    total_deaths_BY=(summary["Countries"][15]["TotalDeaths"])
    new_recovered_BY=(summary["Countries"][15]["NewRecovered"])
    total_recovered_BY=(summary["Countries"][15]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Belarus</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_BY)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_BY)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_BY)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_BY)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_BY)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_BY)+'</pre>',parse_mode='HTML')
def BE(update, context):
    new_confirmed_BE=(summary["Countries"][16]["NewConfirmed"])
    total_confirmed_BE=(summary["Countries"][16]["TotalConfirmed"])
    new_deaths_BE=(summary["Countries"][16]["NewDeaths"])
    total_deaths_BE=(summary["Countries"][16]["TotalDeaths"])
    new_recovered_BE=(summary["Countries"][16]["NewRecovered"])
    total_recovered_BE=(summary["Countries"][16]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Belgium</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_BE)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_BE)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_BE)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_BE)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_BE)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_BE)+'</pre>',parse_mode='HTML')
def BZ(update, context):
    new_confirmed_BZ=(summary["Countries"][17]["NewConfirmed"])
    total_confirmed_BZ=(summary["Countries"][17]["TotalConfirmed"])
    new_deaths_BZ=(summary["Countries"][17]["NewDeaths"])
    total_deaths_BZ=(summary["Countries"][17]["TotalDeaths"])
    new_recovered_BZ=(summary["Countries"][17]["NewRecovered"])
    total_recovered_BZ=(summary["Countries"][17]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Belize</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_BZ)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_BZ)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_BZ)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_BZ)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_BZ)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_BZ)+'</pre>',parse_mode='HTML')
def BJ(update, context):
    new_confirmed_BJ=(summary["Countries"][18]["NewConfirmed"])
    total_confirmed_BJ=(summary["Countries"][18]["TotalConfirmed"])
    new_deaths_BJ=(summary["Countries"][18]["NewDeaths"])
    total_deaths_BJ=(summary["Countries"][18]["TotalDeaths"])
    new_recovered_BJ=(summary["Countries"][18]["NewRecovered"])
    total_recovered_BJ=(summary["Countries"][18]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Benin</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_BJ)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_BJ)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_BJ)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_BJ)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_BJ)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_BJ)+'</pre>',parse_mode='HTML')
def BT(update, context):
    new_confirmed_BT=(summary["Countries"][19]["NewConfirmed"])
    total_confirmed_BT=(summary["Countries"][19]["TotalConfirmed"])
    new_deaths_BT=(summary["Countries"][19]["NewDeaths"])
    total_deaths_BT=(summary["Countries"][19]["TotalDeaths"])
    new_recovered_BT=(summary["Countries"][19]["NewRecovered"])
    total_recovered_BT=(summary["Countries"][19]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Bhutan</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_BT)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_BT)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_BT)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_BT)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_BT)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_BT)+'</pre>',parse_mode='HTML')
def BO(update, context):
    new_confirmed_BO=(summary["Countries"][20]["NewConfirmed"])
    total_confirmed_BO=(summary["Countries"][20]["TotalConfirmed"])
    new_deaths_BO=(summary["Countries"][20]["NewDeaths"])
    total_deaths_BO=(summary["Countries"][20]["TotalDeaths"])
    new_recovered_BO=(summary["Countries"][20]["NewRecovered"])
    total_recovered_BO=(summary["Countries"][20]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Bolivia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_BO)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_BO)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_BO)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_BO)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_BO)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_BO)+'</pre>',parse_mode='HTML')
def BA(update, context):
    new_confirmed_BA=(summary["Countries"][21]["NewConfirmed"])
    total_confirmed_BA=(summary["Countries"][21]["TotalConfirmed"])
    new_deaths_BA=(summary["Countries"][21]["NewDeaths"])
    total_deaths_BA=(summary["Countries"][21]["TotalDeaths"])
    new_recovered_BA=(summary["Countries"][21]["NewRecovered"])
    total_recovered_BA=(summary["Countries"][21]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Bosnia and Herzegovina</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_BA)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_BA)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_BA)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_BA)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_BA)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_BA)+'</pre>',parse_mode='HTML')
def BW(update, context):
    new_confirmed_BW=(summary["Countries"][22]["NewConfirmed"])
    total_confirmed_BW=(summary["Countries"][22]["TotalConfirmed"])
    new_deaths_BW=(summary["Countries"][22]["NewDeaths"])
    total_deaths_BW=(summary["Countries"][22]["TotalDeaths"])
    new_recovered_BW=(summary["Countries"][22]["NewRecovered"])
    total_recovered_BW=(summary["Countries"][22]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Botswana</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_BW)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_BW)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_BW)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_BW)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_BW)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_BW)+'</pre>',parse_mode='HTML')
def BR(update, context):
    new_confirmed_BR=(summary["Countries"][23]["NewConfirmed"])
    total_confirmed_BR=(summary["Countries"][23]["TotalConfirmed"])
    new_deaths_BR=(summary["Countries"][23]["NewDeaths"])
    total_deaths_BR=(summary["Countries"][23]["TotalDeaths"])
    new_recovered_BR=(summary["Countries"][23]["NewRecovered"])
    total_recovered_BR=(summary["Countries"][23]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Brazil</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_BR)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_BR)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_BR)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_BR)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_BR)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_BR)+'</pre>',parse_mode='HTML')
def BN(update, context):
    new_confirmed_BN=(summary["Countries"][24]["NewConfirmed"])
    total_confirmed_BN=(summary["Countries"][24]["TotalConfirmed"])
    new_deaths_BN=(summary["Countries"][24]["NewDeaths"])
    total_deaths_BN=(summary["Countries"][24]["TotalDeaths"])
    new_recovered_BN=(summary["Countries"][24]["NewRecovered"])
    total_recovered_BN=(summary["Countries"][24]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Brunei Darussalam</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_BN)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_BN)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_BN)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_BN)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_BN)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_BN)+'</pre>',parse_mode='HTML')
def BG(update, context):
    new_confirmed_BG=(summary["Countries"][25]["NewConfirmed"])
    total_confirmed_BG=(summary["Countries"][25]["TotalConfirmed"])
    new_deaths_BG=(summary["Countries"][25]["NewDeaths"])
    total_deaths_BG=(summary["Countries"][25]["TotalDeaths"])
    new_recovered_BG=(summary["Countries"][25]["NewRecovered"])
    total_recovered_BG=(summary["Countries"][25]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Bulgaria</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_BG)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_BG)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_BG)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_BG)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_BG)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_BG)+'</pre>',parse_mode='HTML')
def BF(update, context):
    new_confirmed_BF=(summary["Countries"][26]["NewConfirmed"])
    total_confirmed_BF=(summary["Countries"][26]["TotalConfirmed"])
    new_deaths_BF=(summary["Countries"][26]["NewDeaths"])
    total_deaths_BF=(summary["Countries"][26]["TotalDeaths"])
    new_recovered_BF=(summary["Countries"][26]["NewRecovered"])
    total_recovered_BF=(summary["Countries"][26]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Burkina Faso</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_BF)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_BF)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_BF)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_BF)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_BF)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_BF)+'</pre>',parse_mode='HTML')
def BI(update, context):
    new_confirmed_BI=(summary["Countries"][27]["NewConfirmed"])
    total_confirmed_BI=(summary["Countries"][27]["TotalConfirmed"])
    new_deaths_BI=(summary["Countries"][27]["NewDeaths"])
    total_deaths_BI=(summary["Countries"][27]["TotalDeaths"])
    new_recovered_BI=(summary["Countries"][27]["NewRecovered"])
    total_recovered_BI=(summary["Countries"][27]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Burundi</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_BI)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_BI)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_BI)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_BI)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_BI)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_BI)+'</pre>',parse_mode='HTML')
def KH(update, context):
    new_confirmed_KH=(summary["Countries"][28]["NewConfirmed"])
    total_confirmed_KH=(summary["Countries"][28]["TotalConfirmed"])
    new_deaths_KH=(summary["Countries"][28]["NewDeaths"])
    total_deaths_KH=(summary["Countries"][28]["TotalDeaths"])
    new_recovered_KH=(summary["Countries"][28]["NewRecovered"])
    total_recovered_KH=(summary["Countries"][28]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Cambodia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_KH)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_KH)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_KH)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_KH)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_KH)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_KH)+'</pre>',parse_mode='HTML')
def CM(update, context):
    new_confirmed_CM=(summary["Countries"][29]["NewConfirmed"])
    total_confirmed_CM=(summary["Countries"][29]["TotalConfirmed"])
    new_deaths_CM=(summary["Countries"][29]["NewDeaths"])
    total_deaths_CM=(summary["Countries"][29]["TotalDeaths"])
    new_recovered_CM=(summary["Countries"][29]["NewRecovered"])
    total_recovered_CM=(summary["Countries"][29]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Cameroon</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_CM)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_CM)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_CM)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_CM)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_CM)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_CM)+'</pre>',parse_mode='HTML')
def CA(update, context):
    new_confirmed_CA=(summary["Countries"][30]["NewConfirmed"])
    total_confirmed_CA=(summary["Countries"][30]["TotalConfirmed"])
    new_deaths_CA=(summary["Countries"][30]["NewDeaths"])
    total_deaths_CA=(summary["Countries"][30]["TotalDeaths"])
    new_recovered_CA=(summary["Countries"][30]["NewRecovered"])
    total_recovered_CA=(summary["Countries"][30]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Canada</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_CA)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_CA)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_CA)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_CA)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_CA)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_CA)+'</pre>',parse_mode='HTML')
def CV(update, context):
    new_confirmed_CV=(summary["Countries"][31]["NewConfirmed"])
    total_confirmed_CV=(summary["Countries"][31]["TotalConfirmed"])
    new_deaths_CV=(summary["Countries"][31]["NewDeaths"])
    total_deaths_CV=(summary["Countries"][31]["TotalDeaths"])
    new_recovered_CV=(summary["Countries"][31]["NewRecovered"])
    total_recovered_CV=(summary["Countries"][31]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Cape Verde</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_CV)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_CV)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_CV)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_CV)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_CV)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_CV)+'</pre>',parse_mode='HTML')
def CF(update, context):
    new_confirmed_CF=(summary["Countries"][32]["NewConfirmed"])
    total_confirmed_CF=(summary["Countries"][32]["TotalConfirmed"])
    new_deaths_CF=(summary["Countries"][32]["NewDeaths"])
    total_deaths_CF=(summary["Countries"][32]["TotalDeaths"])
    new_recovered_CF=(summary["Countries"][32]["NewRecovered"])
    total_recovered_CF=(summary["Countries"][32]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Central African Republic</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_CF)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_CF)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_CF)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_CF)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_CF)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_CF)+'</pre>',parse_mode='HTML')
def TD(update, context):
    new_confirmed_TD=(summary["Countries"][33]["NewConfirmed"])
    total_confirmed_TD=(summary["Countries"][33]["TotalConfirmed"])
    new_deaths_TD=(summary["Countries"][33]["NewDeaths"])
    total_deaths_TD=(summary["Countries"][33]["TotalDeaths"])
    new_recovered_TD=(summary["Countries"][33]["NewRecovered"])
    total_recovered_TD=(summary["Countries"][33]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Chad</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_TD)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_TD)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_TD)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_TD)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_TD)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_TD)+'</pre>',parse_mode='HTML')
def CL(update, context):
    new_confirmed_CL=(summary["Countries"][34]["NewConfirmed"])
    total_confirmed_CL=(summary["Countries"][34]["TotalConfirmed"])
    new_deaths_CL=(summary["Countries"][34]["NewDeaths"])
    total_deaths_CL=(summary["Countries"][34]["TotalDeaths"])
    new_recovered_CL=(summary["Countries"][34]["NewRecovered"])
    total_recovered_CL=(summary["Countries"][34]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Chile</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_CL)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_CL)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_CL)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_CL)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_CL)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_CL)+'</pre>',parse_mode='HTML')
def CN(update, context):
    new_confirmed_CN=(summary["Countries"][35]["NewConfirmed"])
    total_confirmed_CN=(summary["Countries"][35]["TotalConfirmed"])
    new_deaths_CN=(summary["Countries"][35]["NewDeaths"])
    total_deaths_CN=(summary["Countries"][35]["TotalDeaths"])
    new_recovered_CN=(summary["Countries"][35]["NewRecovered"])
    total_recovered_CN=(summary["Countries"][35]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>China</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_CN)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_CN)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_CN)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_CN)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_CN)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_CN)+'</pre>',parse_mode='HTML')
def CO(update, context):
    new_confirmed_CO=(summary["Countries"][36]["NewConfirmed"])
    total_confirmed_CO=(summary["Countries"][36]["TotalConfirmed"])
    new_deaths_CO=(summary["Countries"][36]["NewDeaths"])
    total_deaths_CO=(summary["Countries"][36]["TotalDeaths"])
    new_recovered_CO=(summary["Countries"][36]["NewRecovered"])
    total_recovered_CO=(summary["Countries"][36]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Colombia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_CO)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_CO)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_CO)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_CO)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_CO)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_CO)+'</pre>',parse_mode='HTML')
def KM(update, context):
    new_confirmed_KM=(summary["Countries"][37]["NewConfirmed"])
    total_confirmed_KM=(summary["Countries"][37]["TotalConfirmed"])
    new_deaths_KM=(summary["Countries"][37]["NewDeaths"])
    total_deaths_KM=(summary["Countries"][37]["TotalDeaths"])
    new_recovered_KM=(summary["Countries"][37]["NewRecovered"])
    total_recovered_KM=(summary["Countries"][37]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Comoros</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_KM)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_KM)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_KM)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_KM)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_KM)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_KM)+'</pre>',parse_mode='HTML')
def CG(update, context):
    new_confirmed_CG=(summary["Countries"][38]["NewConfirmed"])
    total_confirmed_CG=(summary["Countries"][38]["TotalConfirmed"])
    new_deaths_CG=(summary["Countries"][38]["NewDeaths"])
    total_deaths_CG=(summary["Countries"][38]["TotalDeaths"])
    new_recovered_CG=(summary["Countries"][38]["NewRecovered"])
    total_recovered_CG=(summary["Countries"][38]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Congo (Brazzaville)</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_CG)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_CG)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_CG)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_CG)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_CG)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_CG)+'</pre>',parse_mode='HTML')
def CD(update, context):
    new_confirmed_CD=(summary["Countries"][39]["NewConfirmed"])
    total_confirmed_CD=(summary["Countries"][39]["TotalConfirmed"])
    new_deaths_CD=(summary["Countries"][39]["NewDeaths"])
    total_deaths_CD=(summary["Countries"][39]["TotalDeaths"])
    new_recovered_CD=(summary["Countries"][39]["NewRecovered"])
    total_recovered_CD=(summary["Countries"][39]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Congo (Kinshasa)</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_CD)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_CD)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_CD)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_CD)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_CD)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_CD)+'</pre>',parse_mode='HTML')
def CR(update, context):
    new_confirmed_CR=(summary["Countries"][40]["NewConfirmed"])
    total_confirmed_CR=(summary["Countries"][40]["TotalConfirmed"])
    new_deaths_CR=(summary["Countries"][40]["NewDeaths"])
    total_deaths_CR=(summary["Countries"][40]["TotalDeaths"])
    new_recovered_CR=(summary["Countries"][40]["NewRecovered"])
    total_recovered_CR=(summary["Countries"][40]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Costa Rica</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_CR)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_CR)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_CR)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_CR)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_CR)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_CR)+'</pre>',parse_mode='HTML')
def HR(update, context):
    new_confirmed_HR=(summary["Countries"][41]["NewConfirmed"])
    total_confirmed_HR=(summary["Countries"][41]["TotalConfirmed"])
    new_deaths_HR=(summary["Countries"][41]["NewDeaths"])
    total_deaths_HR=(summary["Countries"][41]["TotalDeaths"])
    new_recovered_HR=(summary["Countries"][41]["NewRecovered"])
    total_recovered_HR=(summary["Countries"][41]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Croatia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_HR)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_HR)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_HR)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_HR)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_HR)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_HR)+'</pre>',parse_mode='HTML')
def CU(update, context):
    new_confirmed_CU=(summary["Countries"][42]["NewConfirmed"])
    total_confirmed_CU=(summary["Countries"][42]["TotalConfirmed"])
    new_deaths_CU=(summary["Countries"][42]["NewDeaths"])
    total_deaths_CU=(summary["Countries"][42]["TotalDeaths"])
    new_recovered_CU=(summary["Countries"][42]["NewRecovered"])
    total_recovered_CU=(summary["Countries"][42]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Cuba</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_CU)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_CU)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_CU)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_CU)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_CU)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_CU)+'</pre>',parse_mode='HTML')
def CY(update, context):
    new_confirmed_CY=(summary["Countries"][43]["NewConfirmed"])
    total_confirmed_CY=(summary["Countries"][43]["TotalConfirmed"])
    new_deaths_CY=(summary["Countries"][43]["NewDeaths"])
    total_deaths_CY=(summary["Countries"][43]["TotalDeaths"])
    new_recovered_CY=(summary["Countries"][43]["NewRecovered"])
    total_recovered_CY=(summary["Countries"][43]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Cyprus</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_CY)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_CY)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_CY)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_CY)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_CY)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_CY)+'</pre>',parse_mode='HTML')
def CZ(update, context):
    new_confirmed_CZ=(summary["Countries"][44]["NewConfirmed"])
    total_confirmed_CZ=(summary["Countries"][44]["TotalConfirmed"])
    new_deaths_CZ=(summary["Countries"][44]["NewDeaths"])
    total_deaths_CZ=(summary["Countries"][44]["TotalDeaths"])
    new_recovered_CZ=(summary["Countries"][44]["NewRecovered"])
    total_recovered_CZ=(summary["Countries"][44]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Czech Republic</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_CZ)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_CZ)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_CZ)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_CZ)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_CZ)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_CZ)+'</pre>',parse_mode='HTML')
def CI(update, context):
    new_confirmed_CI=(summary["Countries"][45]["NewConfirmed"])
    total_confirmed_CI=(summary["Countries"][45]["TotalConfirmed"])
    new_deaths_CI=(summary["Countries"][45]["NewDeaths"])
    total_deaths_CI=(summary["Countries"][45]["TotalDeaths"])
    new_recovered_CI=(summary["Countries"][45]["NewRecovered"])
    total_recovered_CI=(summary["Countries"][45]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Côte d'Ivoire</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_CI)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_CI)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_CI)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_CI)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_CI)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_CI)+'</pre>',parse_mode='HTML')
def DK(update, context):
    new_confirmed_DK=(summary["Countries"][46]["NewConfirmed"])
    total_confirmed_DK=(summary["Countries"][46]["TotalConfirmed"])
    new_deaths_DK=(summary["Countries"][46]["NewDeaths"])
    total_deaths_DK=(summary["Countries"][46]["TotalDeaths"])
    new_recovered_DK=(summary["Countries"][46]["NewRecovered"])
    total_recovered_DK=(summary["Countries"][46]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Denmark</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_DK)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_DK)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_DK)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_DK)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_DK)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_DK)+'</pre>',parse_mode='HTML')
def DJ(update, context):
    new_confirmed_DJ=(summary["Countries"][47]["NewConfirmed"])
    total_confirmed_DJ=(summary["Countries"][47]["TotalConfirmed"])
    new_deaths_DJ=(summary["Countries"][47]["NewDeaths"])
    total_deaths_DJ=(summary["Countries"][47]["TotalDeaths"])
    new_recovered_DJ=(summary["Countries"][47]["NewRecovered"])
    total_recovered_DJ=(summary["Countries"][47]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Djibouti</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_DJ)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_DJ)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_DJ)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_DJ)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_DJ)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_DJ)+'</pre>',parse_mode='HTML')
def DM(update, context):
    new_confirmed_DM=(summary["Countries"][48]["NewConfirmed"])
    total_confirmed_DM=(summary["Countries"][48]["TotalConfirmed"])
    new_deaths_DM=(summary["Countries"][48]["NewDeaths"])
    total_deaths_DM=(summary["Countries"][48]["TotalDeaths"])
    new_recovered_DM=(summary["Countries"][48]["NewRecovered"])
    total_recovered_DM=(summary["Countries"][48]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Dominica</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_DM)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_DM)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_DM)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_DM)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_DM)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_DM)+'</pre>',parse_mode='HTML')
def DO(update, context):
    new_confirmed_DO=(summary["Countries"][49]["NewConfirmed"])
    total_confirmed_DO=(summary["Countries"][49]["TotalConfirmed"])
    new_deaths_DO=(summary["Countries"][49]["NewDeaths"])
    total_deaths_DO=(summary["Countries"][49]["TotalDeaths"])
    new_recovered_DO=(summary["Countries"][49]["NewRecovered"])
    total_recovered_DO=(summary["Countries"][49]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Dominican Republic</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_DO)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_DO)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_DO)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_DO)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_DO)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_DO)+'</pre>',parse_mode='HTML')


def EC(update, context):
    new_confirmed_EC=(summary["Countries"][50]["NewConfirmed"])
    total_confirmed_EC=(summary["Countries"][50]["TotalConfirmed"])        
    new_deaths_EC=(summary["Countries"][50]["NewDeaths"])
    total_deaths_EC=(summary["Countries"][50]["TotalDeaths"])
    new_recovered_EC=(summary["Countries"][50]["NewRecovered"])
    total_recovered_EC=(summary["Countries"][50]["TotalRecovered"])        
    update.message.reply_text('<b>Corona Statistics:</b><pre>Ecuador</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_EC)+'</pre>'       
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_EC)+'</pre>'   
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_EC)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_EC)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_EC)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_EC)+'</pre>',parse_mode='HTML')
def EG(update, context):
    new_confirmed_EG=(summary["Countries"][51]["NewConfirmed"])
    total_confirmed_EG=(summary["Countries"][51]["TotalConfirmed"])
    new_deaths_EG=(summary["Countries"][51]["NewDeaths"])
    total_deaths_EG=(summary["Countries"][51]["TotalDeaths"])
    new_recovered_EG=(summary["Countries"][51]["NewRecovered"])
    total_recovered_EG=(summary["Countries"][51]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Egypt</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_EG)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_EG)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_EG)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_EG)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_EG)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_EG)+'</pre>',parse_mode='HTML')
def SV(update, context):
    new_confirmed_SV=(summary["Countries"][52]["NewConfirmed"])
    total_confirmed_SV=(summary["Countries"][52]["TotalConfirmed"])
    new_deaths_SV=(summary["Countries"][52]["NewDeaths"])
    total_deaths_SV=(summary["Countries"][52]["TotalDeaths"])
    new_recovered_SV=(summary["Countries"][52]["NewRecovered"])
    total_recovered_SV=(summary["Countries"][52]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>El Salvador</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_SV)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_SV)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_SV)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_SV)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_SV)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_SV)+'</pre>',parse_mode='HTML')
def GQ(update, context):
    new_confirmed_GQ=(summary["Countries"][53]["NewConfirmed"])
    total_confirmed_GQ=(summary["Countries"][53]["TotalConfirmed"])
    new_deaths_GQ=(summary["Countries"][53]["NewDeaths"])
    total_deaths_GQ=(summary["Countries"][53]["TotalDeaths"])
    new_recovered_GQ=(summary["Countries"][53]["NewRecovered"])
    total_recovered_GQ=(summary["Countries"][53]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Equatorial Guinea</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_GQ)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_GQ)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_GQ)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_GQ)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_GQ)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_GQ)+'</pre>',parse_mode='HTML')
def ER(update, context):
    new_confirmed_ER=(summary["Countries"][54]["NewConfirmed"])
    total_confirmed_ER=(summary["Countries"][54]["TotalConfirmed"])
    new_deaths_ER=(summary["Countries"][54]["NewDeaths"])
    total_deaths_ER=(summary["Countries"][54]["TotalDeaths"])
    new_recovered_ER=(summary["Countries"][54]["NewRecovered"])
    total_recovered_ER=(summary["Countries"][54]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Eritrea</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_ER)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_ER)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_ER)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_ER)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_ER)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_ER)+'</pre>',parse_mode='HTML')
def EE(update, context):
    new_confirmed_EE=(summary["Countries"][55]["NewConfirmed"])
    total_confirmed_EE=(summary["Countries"][55]["TotalConfirmed"])
    new_deaths_EE=(summary["Countries"][55]["NewDeaths"])
    total_deaths_EE=(summary["Countries"][55]["TotalDeaths"])
    new_recovered_EE=(summary["Countries"][55]["NewRecovered"])
    total_recovered_EE=(summary["Countries"][55]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Estonia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_EE)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_EE)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_EE)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_EE)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_EE)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_EE)+'</pre>',parse_mode='HTML')
def ET(update, context):
    new_confirmed_ET=(summary["Countries"][56]["NewConfirmed"])
    total_confirmed_ET=(summary["Countries"][56]["TotalConfirmed"])
    new_deaths_ET=(summary["Countries"][56]["NewDeaths"])
    total_deaths_ET=(summary["Countries"][56]["TotalDeaths"])
    new_recovered_ET=(summary["Countries"][56]["NewRecovered"])
    total_recovered_ET=(summary["Countries"][56]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Ethiopia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_ET)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_ET)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_ET)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_ET)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_ET)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_ET)+'</pre>',parse_mode='HTML')
def FJ(update, context):
    new_confirmed_FJ=(summary["Countries"][57]["NewConfirmed"])
    total_confirmed_FJ=(summary["Countries"][57]["TotalConfirmed"])
    new_deaths_FJ=(summary["Countries"][57]["NewDeaths"])
    total_deaths_FJ=(summary["Countries"][57]["TotalDeaths"])
    new_recovered_FJ=(summary["Countries"][57]["NewRecovered"])
    total_recovered_FJ=(summary["Countries"][57]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Fiji</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_FJ)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_FJ)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_FJ)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_FJ)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_FJ)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_FJ)+'</pre>',parse_mode='HTML')
def FI(update, context):
    new_confirmed_FI=(summary["Countries"][58]["NewConfirmed"])
    total_confirmed_FI=(summary["Countries"][58]["TotalConfirmed"])
    new_deaths_FI=(summary["Countries"][58]["NewDeaths"])
    total_deaths_FI=(summary["Countries"][58]["TotalDeaths"])
    new_recovered_FI=(summary["Countries"][58]["NewRecovered"])
    total_recovered_FI=(summary["Countries"][58]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Finland</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_FI)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_FI)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_FI)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_FI)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_FI)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_FI)+'</pre>',parse_mode='HTML')
def FR(update, context):
    new_confirmed_FR=(summary["Countries"][59]["NewConfirmed"])
    total_confirmed_FR=(summary["Countries"][59]["TotalConfirmed"])
    new_deaths_FR=(summary["Countries"][59]["NewDeaths"])
    total_deaths_FR=(summary["Countries"][59]["TotalDeaths"])
    new_recovered_FR=(summary["Countries"][59]["NewRecovered"])
    total_recovered_FR=(summary["Countries"][59]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>France</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_FR)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_FR)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_FR)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_FR)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_FR)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_FR)+'</pre>',parse_mode='HTML')
def GA(update, context):
    new_confirmed_GA=(summary["Countries"][60]["NewConfirmed"])
    total_confirmed_GA=(summary["Countries"][60]["TotalConfirmed"])
    new_deaths_GA=(summary["Countries"][60]["NewDeaths"])
    total_deaths_GA=(summary["Countries"][60]["TotalDeaths"])
    new_recovered_GA=(summary["Countries"][60]["NewRecovered"])
    total_recovered_GA=(summary["Countries"][60]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Gabon</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_GA)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_GA)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_GA)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_GA)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_GA)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_GA)+'</pre>',parse_mode='HTML')
def GM(update, context):
    new_confirmed_GM=(summary["Countries"][61]["NewConfirmed"])
    total_confirmed_GM=(summary["Countries"][61]["TotalConfirmed"])
    new_deaths_GM=(summary["Countries"][61]["NewDeaths"])
    total_deaths_GM=(summary["Countries"][61]["TotalDeaths"])
    new_recovered_GM=(summary["Countries"][61]["NewRecovered"])
    total_recovered_GM=(summary["Countries"][61]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Gambia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_GM)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_GM)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_GM)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_GM)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_GM)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_GM)+'</pre>',parse_mode='HTML')
def GE(update, context):
    new_confirmed_GE=(summary["Countries"][62]["NewConfirmed"])
    total_confirmed_GE=(summary["Countries"][62]["TotalConfirmed"])
    new_deaths_GE=(summary["Countries"][62]["NewDeaths"])
    total_deaths_GE=(summary["Countries"][62]["TotalDeaths"])
    new_recovered_GE=(summary["Countries"][62]["NewRecovered"])
    total_recovered_GE=(summary["Countries"][62]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Georgia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_GE)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_GE)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_GE)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_GE)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_GE)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_GE)+'</pre>',parse_mode='HTML')
def DE(update, context):
    new_confirmed_DE=(summary["Countries"][63]["NewConfirmed"])
    total_confirmed_DE=(summary["Countries"][63]["TotalConfirmed"])
    new_deaths_DE=(summary["Countries"][63]["NewDeaths"])
    total_deaths_DE=(summary["Countries"][63]["TotalDeaths"])
    new_recovered_DE=(summary["Countries"][63]["NewRecovered"])
    total_recovered_DE=(summary["Countries"][63]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Germany</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_DE)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_DE)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_DE)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_DE)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_DE)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_DE)+'</pre>',parse_mode='HTML')
def GH(update, context):
    new_confirmed_GH=(summary["Countries"][64]["NewConfirmed"])
    total_confirmed_GH=(summary["Countries"][64]["TotalConfirmed"])
    new_deaths_GH=(summary["Countries"][64]["NewDeaths"])
    total_deaths_GH=(summary["Countries"][64]["TotalDeaths"])
    new_recovered_GH=(summary["Countries"][64]["NewRecovered"])
    total_recovered_GH=(summary["Countries"][64]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Ghana</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_GH)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_GH)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_GH)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_GH)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_GH)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_GH)+'</pre>',parse_mode='HTML')
def GR(update, context):
    new_confirmed_GR=(summary["Countries"][65]["NewConfirmed"])
    total_confirmed_GR=(summary["Countries"][65]["TotalConfirmed"])
    new_deaths_GR=(summary["Countries"][65]["NewDeaths"])
    total_deaths_GR=(summary["Countries"][65]["TotalDeaths"])
    new_recovered_GR=(summary["Countries"][65]["NewRecovered"])
    total_recovered_GR=(summary["Countries"][65]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Greece</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_GR)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_GR)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_GR)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_GR)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_GR)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_GR)+'</pre>',parse_mode='HTML')
def GD(update, context):
    new_confirmed_GD=(summary["Countries"][66]["NewConfirmed"])
    total_confirmed_GD=(summary["Countries"][66]["TotalConfirmed"])
    new_deaths_GD=(summary["Countries"][66]["NewDeaths"])
    total_deaths_GD=(summary["Countries"][66]["TotalDeaths"])
    new_recovered_GD=(summary["Countries"][66]["NewRecovered"])
    total_recovered_GD=(summary["Countries"][66]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Grenada</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_GD)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_GD)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_GD)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_GD)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_GD)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_GD)+'</pre>',parse_mode='HTML')
def GT(update, context):
    new_confirmed_GT=(summary["Countries"][67]["NewConfirmed"])
    total_confirmed_GT=(summary["Countries"][67]["TotalConfirmed"])
    new_deaths_GT=(summary["Countries"][67]["NewDeaths"])
    total_deaths_GT=(summary["Countries"][67]["TotalDeaths"])
    new_recovered_GT=(summary["Countries"][67]["NewRecovered"])
    total_recovered_GT=(summary["Countries"][67]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Guatemala</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_GT)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_GT)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_GT)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_GT)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_GT)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_GT)+'</pre>',parse_mode='HTML')
def GN(update, context):
    new_confirmed_GN=(summary["Countries"][68]["NewConfirmed"])
    total_confirmed_GN=(summary["Countries"][68]["TotalConfirmed"])
    new_deaths_GN=(summary["Countries"][68]["NewDeaths"])
    total_deaths_GN=(summary["Countries"][68]["TotalDeaths"])
    new_recovered_GN=(summary["Countries"][68]["NewRecovered"])
    total_recovered_GN=(summary["Countries"][68]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Guinea</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_GN)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_GN)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_GN)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_GN)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_GN)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_GN)+'</pre>',parse_mode='HTML')
def GW(update, context):
    new_confirmed_GW=(summary["Countries"][69]["NewConfirmed"])
    total_confirmed_GW=(summary["Countries"][69]["TotalConfirmed"])
    new_deaths_GW=(summary["Countries"][69]["NewDeaths"])
    total_deaths_GW=(summary["Countries"][69]["TotalDeaths"])
    new_recovered_GW=(summary["Countries"][69]["NewRecovered"])
    total_recovered_GW=(summary["Countries"][69]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Guinea-Bissau</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_GW)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_GW)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_GW)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_GW)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_GW)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_GW)+'</pre>',parse_mode='HTML')
def GY(update, context):
    new_confirmed_GY=(summary["Countries"][70]["NewConfirmed"])
    total_confirmed_GY=(summary["Countries"][70]["TotalConfirmed"])
    new_deaths_GY=(summary["Countries"][70]["NewDeaths"])
    total_deaths_GY=(summary["Countries"][70]["TotalDeaths"])
    new_recovered_GY=(summary["Countries"][70]["NewRecovered"])
    total_recovered_GY=(summary["Countries"][70]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Guyana</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_GY)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_GY)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_GY)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_GY)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_GY)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_GY)+'</pre>',parse_mode='HTML')
def HT(update, context):
    new_confirmed_HT=(summary["Countries"][71]["NewConfirmed"])
    total_confirmed_HT=(summary["Countries"][71]["TotalConfirmed"])
    new_deaths_HT=(summary["Countries"][71]["NewDeaths"])
    total_deaths_HT=(summary["Countries"][71]["TotalDeaths"])
    new_recovered_HT=(summary["Countries"][71]["NewRecovered"])
    total_recovered_HT=(summary["Countries"][71]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Haiti</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_HT)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_HT)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_HT)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_HT)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_HT)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_HT)+'</pre>',parse_mode='HTML')
def VA(update, context):
    new_confirmed_VA=(summary["Countries"][72]["NewConfirmed"])
    total_confirmed_VA=(summary["Countries"][72]["TotalConfirmed"])
    new_deaths_VA=(summary["Countries"][72]["NewDeaths"])
    total_deaths_VA=(summary["Countries"][72]["TotalDeaths"])
    new_recovered_VA=(summary["Countries"][72]["NewRecovered"])
    total_recovered_VA=(summary["Countries"][72]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Holy See (Vatican City State)</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_VA)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_VA)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_VA)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_VA)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_VA)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_VA)+'</pre>',parse_mode='HTML')
def HN(update, context):
    new_confirmed_HN=(summary["Countries"][73]["NewConfirmed"])
    total_confirmed_HN=(summary["Countries"][73]["TotalConfirmed"])
    new_deaths_HN=(summary["Countries"][73]["NewDeaths"])
    total_deaths_HN=(summary["Countries"][73]["TotalDeaths"])
    new_recovered_HN=(summary["Countries"][73]["NewRecovered"])
    total_recovered_HN=(summary["Countries"][73]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Honduras</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_HN)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_HN)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_HN)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_HN)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_HN)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_HN)+'</pre>',parse_mode='HTML')
def HU(update, context):
    new_confirmed_HU=(summary["Countries"][74]["NewConfirmed"])
    total_confirmed_HU=(summary["Countries"][74]["TotalConfirmed"])
    new_deaths_HU=(summary["Countries"][74]["NewDeaths"])
    total_deaths_HU=(summary["Countries"][74]["TotalDeaths"])
    new_recovered_HU=(summary["Countries"][74]["NewRecovered"])
    total_recovered_HU=(summary["Countries"][74]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Hungary</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_HU)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_HU)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_HU)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_HU)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_HU)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_HU)+'</pre>',parse_mode='HTML')
def IS(update, context):
    new_confirmed_IS=(summary["Countries"][75]["NewConfirmed"])
    total_confirmed_IS=(summary["Countries"][75]["TotalConfirmed"])
    new_deaths_IS=(summary["Countries"][75]["NewDeaths"])
    total_deaths_IS=(summary["Countries"][75]["TotalDeaths"])
    new_recovered_IS=(summary["Countries"][75]["NewRecovered"])
    total_recovered_IS=(summary["Countries"][75]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Iceland</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_IS)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_IS)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_IS)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_IS)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_IS)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_IS)+'</pre>',parse_mode='HTML')
def IN(update, context):
    new_confirmed_IN=(summary["Countries"][76]["NewConfirmed"])
    total_confirmed_IN=(summary["Countries"][76]["TotalConfirmed"])
    new_deaths_IN=(summary["Countries"][76]["NewDeaths"])
    total_deaths_IN=(summary["Countries"][76]["TotalDeaths"])
    new_recovered_IN=(summary["Countries"][76]["NewRecovered"])
    total_recovered_IN=(summary["Countries"][76]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>India</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_IN)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_IN)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_IN)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_IN)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_IN)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_IN)+'</pre>',parse_mode='HTML')
def ID(update, context):
    new_confirmed_ID=(summary["Countries"][77]["NewConfirmed"])
    total_confirmed_ID=(summary["Countries"][77]["TotalConfirmed"])
    new_deaths_ID=(summary["Countries"][77]["NewDeaths"])
    total_deaths_ID=(summary["Countries"][77]["TotalDeaths"])
    new_recovered_ID=(summary["Countries"][77]["NewRecovered"])
    total_recovered_ID=(summary["Countries"][77]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Indonesia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_ID)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_ID)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_ID)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_ID)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_ID)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_ID)+'</pre>',parse_mode='HTML')
def IR(update, context):
    new_confirmed_IR=(summary["Countries"][78]["NewConfirmed"])
    total_confirmed_IR=(summary["Countries"][78]["TotalConfirmed"])
    new_deaths_IR=(summary["Countries"][78]["NewDeaths"])
    total_deaths_IR=(summary["Countries"][78]["TotalDeaths"])
    new_recovered_IR=(summary["Countries"][78]["NewRecovered"])
    total_recovered_IR=(summary["Countries"][78]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Iran, Islamic Republic of</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_IR)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_IR)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_IR)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_IR)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_IR)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_IR)+'</pre>',parse_mode='HTML')
def IQ(update, context):
    new_confirmed_IQ=(summary["Countries"][79]["NewConfirmed"])
    total_confirmed_IQ=(summary["Countries"][79]["TotalConfirmed"])
    new_deaths_IQ=(summary["Countries"][79]["NewDeaths"])
    total_deaths_IQ=(summary["Countries"][79]["TotalDeaths"])
    new_recovered_IQ=(summary["Countries"][79]["NewRecovered"])
    total_recovered_IQ=(summary["Countries"][79]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Iraq</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_IQ)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_IQ)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_IQ)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_IQ)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_IQ)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_IQ)+'</pre>',parse_mode='HTML')
def IE(update, context):
    new_confirmed_IE=(summary["Countries"][80]["NewConfirmed"])
    total_confirmed_IE=(summary["Countries"][80]["TotalConfirmed"])
    new_deaths_IE=(summary["Countries"][80]["NewDeaths"])
    total_deaths_IE=(summary["Countries"][80]["TotalDeaths"])
    new_recovered_IE=(summary["Countries"][80]["NewRecovered"])
    total_recovered_IE=(summary["Countries"][80]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Ireland</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_IE)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_IE)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_IE)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_IE)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_IE)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_IE)+'</pre>',parse_mode='HTML')
def IL(update, context):
    new_confirmed_IL=(summary["Countries"][81]["NewConfirmed"])
    total_confirmed_IL=(summary["Countries"][81]["TotalConfirmed"])
    new_deaths_IL=(summary["Countries"][81]["NewDeaths"])
    total_deaths_IL=(summary["Countries"][81]["TotalDeaths"])
    new_recovered_IL=(summary["Countries"][81]["NewRecovered"])
    total_recovered_IL=(summary["Countries"][81]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Israel</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_IL)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_IL)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_IL)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_IL)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_IL)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_IL)+'</pre>',parse_mode='HTML')
def IT(update, context):
    new_confirmed_IT=(summary["Countries"][82]["NewConfirmed"])
    total_confirmed_IT=(summary["Countries"][82]["TotalConfirmed"])
    new_deaths_IT=(summary["Countries"][82]["NewDeaths"])
    total_deaths_IT=(summary["Countries"][82]["TotalDeaths"])
    new_recovered_IT=(summary["Countries"][82]["NewRecovered"])
    total_recovered_IT=(summary["Countries"][82]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Italy</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_IT)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_IT)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_IT)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_IT)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_IT)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_IT)+'</pre>',parse_mode='HTML')
def JM(update, context):
    new_confirmed_JM=(summary["Countries"][83]["NewConfirmed"])
    total_confirmed_JM=(summary["Countries"][83]["TotalConfirmed"])
    new_deaths_JM=(summary["Countries"][83]["NewDeaths"])
    total_deaths_JM=(summary["Countries"][83]["TotalDeaths"])
    new_recovered_JM=(summary["Countries"][83]["NewRecovered"])
    total_recovered_JM=(summary["Countries"][83]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Jamaica</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_JM)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_JM)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_JM)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_JM)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_JM)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_JM)+'</pre>',parse_mode='HTML')
def JP(update, context):
    new_confirmed_JP=(summary["Countries"][84]["NewConfirmed"])
    total_confirmed_JP=(summary["Countries"][84]["TotalConfirmed"])
    new_deaths_JP=(summary["Countries"][84]["NewDeaths"])
    total_deaths_JP=(summary["Countries"][84]["TotalDeaths"])
    new_recovered_JP=(summary["Countries"][84]["NewRecovered"])
    total_recovered_JP=(summary["Countries"][84]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Japan</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_JP)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_JP)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_JP)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_JP)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_JP)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_JP)+'</pre>',parse_mode='HTML')
def JO(update, context):
    new_confirmed_JO=(summary["Countries"][85]["NewConfirmed"])
    total_confirmed_JO=(summary["Countries"][85]["TotalConfirmed"])
    new_deaths_JO=(summary["Countries"][85]["NewDeaths"])
    total_deaths_JO=(summary["Countries"][85]["TotalDeaths"])
    new_recovered_JO=(summary["Countries"][85]["NewRecovered"])
    total_recovered_JO=(summary["Countries"][85]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Jordan</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_JO)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_JO)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_JO)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_JO)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_JO)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_JO)+'</pre>',parse_mode='HTML')
def KZ(update, context):
    new_confirmed_KZ=(summary["Countries"][86]["NewConfirmed"])
    total_confirmed_KZ=(summary["Countries"][86]["TotalConfirmed"])
    new_deaths_KZ=(summary["Countries"][86]["NewDeaths"])
    total_deaths_KZ=(summary["Countries"][86]["TotalDeaths"])
    new_recovered_KZ=(summary["Countries"][86]["NewRecovered"])
    total_recovered_KZ=(summary["Countries"][86]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Kazakhstan</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_KZ)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_KZ)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_KZ)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_KZ)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_KZ)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_KZ)+'</pre>',parse_mode='HTML')
def KE(update, context):
    new_confirmed_KE=(summary["Countries"][87]["NewConfirmed"])
    total_confirmed_KE=(summary["Countries"][87]["TotalConfirmed"])
    new_deaths_KE=(summary["Countries"][87]["NewDeaths"])
    total_deaths_KE=(summary["Countries"][87]["TotalDeaths"])
    new_recovered_KE=(summary["Countries"][87]["NewRecovered"])
    total_recovered_KE=(summary["Countries"][87]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Kenya</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_KE)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_KE)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_KE)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_KE)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_KE)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_KE)+'</pre>',parse_mode='HTML')
def KR(update, context):
    new_confirmed_KR=(summary["Countries"][88]["NewConfirmed"])
    total_confirmed_KR=(summary["Countries"][88]["TotalConfirmed"])
    new_deaths_KR=(summary["Countries"][88]["NewDeaths"])
    total_deaths_KR=(summary["Countries"][88]["TotalDeaths"])
    new_recovered_KR=(summary["Countries"][88]["NewRecovered"])
    total_recovered_KR=(summary["Countries"][88]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Korea (South)</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_KR)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_KR)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_KR)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_KR)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_KR)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_KR)+'</pre>',parse_mode='HTML')
def KW(update, context):
    new_confirmed_KW=(summary["Countries"][89]["NewConfirmed"])
    total_confirmed_KW=(summary["Countries"][89]["TotalConfirmed"])
    new_deaths_KW=(summary["Countries"][89]["NewDeaths"])
    total_deaths_KW=(summary["Countries"][89]["TotalDeaths"])
    new_recovered_KW=(summary["Countries"][89]["NewRecovered"])
    total_recovered_KW=(summary["Countries"][89]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Kuwait</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_KW)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_KW)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_KW)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_KW)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_KW)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_KW)+'</pre>',parse_mode='HTML')
def KG(update, context):
    new_confirmed_KG=(summary["Countries"][90]["NewConfirmed"])
    total_confirmed_KG=(summary["Countries"][90]["TotalConfirmed"])
    new_deaths_KG=(summary["Countries"][90]["NewDeaths"])
    total_deaths_KG=(summary["Countries"][90]["TotalDeaths"])
    new_recovered_KG=(summary["Countries"][90]["NewRecovered"])
    total_recovered_KG=(summary["Countries"][90]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Kyrgyzstan</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_KG)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_KG)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_KG)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_KG)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_KG)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_KG)+'</pre>',parse_mode='HTML')
def LA(update, context):
    new_confirmed_LA=(summary["Countries"][91]["NewConfirmed"])
    total_confirmed_LA=(summary["Countries"][91]["TotalConfirmed"])
    new_deaths_LA=(summary["Countries"][91]["NewDeaths"])
    total_deaths_LA=(summary["Countries"][91]["TotalDeaths"])
    new_recovered_LA=(summary["Countries"][91]["NewRecovered"])
    total_recovered_LA=(summary["Countries"][91]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Lao PDR</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_LA)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_LA)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_LA)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_LA)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_LA)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_LA)+'</pre>',parse_mode='HTML')
def LV(update, context):
    new_confirmed_LV=(summary["Countries"][92]["NewConfirmed"])
    total_confirmed_LV=(summary["Countries"][92]["TotalConfirmed"])
    new_deaths_LV=(summary["Countries"][92]["NewDeaths"])
    total_deaths_LV=(summary["Countries"][92]["TotalDeaths"])
    new_recovered_LV=(summary["Countries"][92]["NewRecovered"])
    total_recovered_LV=(summary["Countries"][92]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Latvia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_LV)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_LV)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_LV)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_LV)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_LV)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_LV)+'</pre>',parse_mode='HTML')
def LB(update, context):
    new_confirmed_LB=(summary["Countries"][93]["NewConfirmed"])
    total_confirmed_LB=(summary["Countries"][93]["TotalConfirmed"])
    new_deaths_LB=(summary["Countries"][93]["NewDeaths"])
    total_deaths_LB=(summary["Countries"][93]["TotalDeaths"])
    new_recovered_LB=(summary["Countries"][93]["NewRecovered"])
    total_recovered_LB=(summary["Countries"][93]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Lebanon</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_LB)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_LB)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_LB)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_LB)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_LB)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_LB)+'</pre>',parse_mode='HTML')
def LS(update, context):
    new_confirmed_LS=(summary["Countries"][94]["NewConfirmed"])
    total_confirmed_LS=(summary["Countries"][94]["TotalConfirmed"])
    new_deaths_LS=(summary["Countries"][94]["NewDeaths"])
    total_deaths_LS=(summary["Countries"][94]["TotalDeaths"])
    new_recovered_LS=(summary["Countries"][94]["NewRecovered"])
    total_recovered_LS=(summary["Countries"][94]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Lesotho</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_LS)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_LS)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_LS)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_LS)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_LS)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_LS)+'</pre>',parse_mode='HTML')
def LR(update, context):
    new_confirmed_LR=(summary["Countries"][95]["NewConfirmed"])
    total_confirmed_LR=(summary["Countries"][95]["TotalConfirmed"])
    new_deaths_LR=(summary["Countries"][95]["NewDeaths"])
    total_deaths_LR=(summary["Countries"][95]["TotalDeaths"])
    new_recovered_LR=(summary["Countries"][95]["NewRecovered"])
    total_recovered_LR=(summary["Countries"][95]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Liberia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_LR)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_LR)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_LR)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_LR)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_LR)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_LR)+'</pre>',parse_mode='HTML')
def LY(update, context):
    new_confirmed_LY=(summary["Countries"][96]["NewConfirmed"])
    total_confirmed_LY=(summary["Countries"][96]["TotalConfirmed"])
    new_deaths_LY=(summary["Countries"][96]["NewDeaths"])
    total_deaths_LY=(summary["Countries"][96]["TotalDeaths"])
    new_recovered_LY=(summary["Countries"][96]["NewRecovered"])
    total_recovered_LY=(summary["Countries"][96]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Libya</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_LY)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_LY)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_LY)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_LY)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_LY)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_LY)+'</pre>',parse_mode='HTML')
def LI(update, context):
    new_confirmed_LI=(summary["Countries"][97]["NewConfirmed"])
    total_confirmed_LI=(summary["Countries"][97]["TotalConfirmed"])
    new_deaths_LI=(summary["Countries"][97]["NewDeaths"])
    total_deaths_LI=(summary["Countries"][97]["TotalDeaths"])
    new_recovered_LI=(summary["Countries"][97]["NewRecovered"])
    total_recovered_LI=(summary["Countries"][97]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Liechtenstein</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_LI)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_LI)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_LI)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_LI)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_LI)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_LI)+'</pre>',parse_mode='HTML')
def LT(update, context):
    new_confirmed_LT=(summary["Countries"][98]["NewConfirmed"])
    total_confirmed_LT=(summary["Countries"][98]["TotalConfirmed"])
    new_deaths_LT=(summary["Countries"][98]["NewDeaths"])
    total_deaths_LT=(summary["Countries"][98]["TotalDeaths"])
    new_recovered_LT=(summary["Countries"][98]["NewRecovered"])
    total_recovered_LT=(summary["Countries"][98]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Lithuania</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_LT)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_LT)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_LT)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_LT)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_LT)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_LT)+'</pre>',parse_mode='HTML')
def LU(update, context):
    new_confirmed_LU=(summary["Countries"][99]["NewConfirmed"])
    total_confirmed_LU=(summary["Countries"][99]["TotalConfirmed"])
    new_deaths_LU=(summary["Countries"][99]["NewDeaths"])
    total_deaths_LU=(summary["Countries"][99]["TotalDeaths"])
    new_recovered_LU=(summary["Countries"][99]["NewRecovered"])
    total_recovered_LU=(summary["Countries"][99]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Luxembourg</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_LU)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_LU)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_LU)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_LU)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_LU)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_LU)+'</pre>',parse_mode='HTML')

def MK(update, context):
    new_confirmed_MK=(summary["Countries"][100]["NewConfirmed"])
    total_confirmed_MK=(summary["Countries"][100]["TotalConfirmed"])
    new_deaths_MK=(summary["Countries"][100]["NewDeaths"])
    total_deaths_MK=(summary["Countries"][100]["TotalDeaths"])
    new_recovered_MK=(summary["Countries"][100]["NewRecovered"])
    total_recovered_MK=(summary["Countries"][100]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Macedonia, Republic of</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_MK)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_MK)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_MK)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_MK)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_MK)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_MK)+'</pre>',parse_mode='HTML')
def MG(update, context):
    new_confirmed_MG=(summary["Countries"][101]["NewConfirmed"])
    total_confirmed_MG=(summary["Countries"][101]["TotalConfirmed"])
    new_deaths_MG=(summary["Countries"][101]["NewDeaths"])
    total_deaths_MG=(summary["Countries"][101]["TotalDeaths"])
    new_recovered_MG=(summary["Countries"][101]["NewRecovered"])
    total_recovered_MG=(summary["Countries"][101]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Madagascar</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_MG)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_MG)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_MG)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_MG)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_MG)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_MG)+'</pre>',parse_mode='HTML')
def MW(update, context):
    new_confirmed_MW=(summary["Countries"][102]["NewConfirmed"])
    total_confirmed_MW=(summary["Countries"][102]["TotalConfirmed"])
    new_deaths_MW=(summary["Countries"][102]["NewDeaths"])
    total_deaths_MW=(summary["Countries"][102]["TotalDeaths"])
    new_recovered_MW=(summary["Countries"][102]["NewRecovered"])
    total_recovered_MW=(summary["Countries"][102]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Malawi</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_MW)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_MW)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_MW)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_MW)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_MW)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_MW)+'</pre>',parse_mode='HTML')
def MY(update, context):
    new_confirmed_MY=(summary["Countries"][103]["NewConfirmed"])
    total_confirmed_MY=(summary["Countries"][103]["TotalConfirmed"])
    new_deaths_MY=(summary["Countries"][103]["NewDeaths"])
    total_deaths_MY=(summary["Countries"][103]["TotalDeaths"])
    new_recovered_MY=(summary["Countries"][103]["NewRecovered"])
    total_recovered_MY=(summary["Countries"][103]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Malaysia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_MY)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_MY)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_MY)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_MY)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_MY)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_MY)+'</pre>',parse_mode='HTML')
def MV(update, context):
    new_confirmed_MV=(summary["Countries"][104]["NewConfirmed"])
    total_confirmed_MV=(summary["Countries"][104]["TotalConfirmed"])
    new_deaths_MV=(summary["Countries"][104]["NewDeaths"])
    total_deaths_MV=(summary["Countries"][104]["TotalDeaths"])
    new_recovered_MV=(summary["Countries"][104]["NewRecovered"])
    total_recovered_MV=(summary["Countries"][104]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Maldives</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_MV)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_MV)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_MV)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_MV)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_MV)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_MV)+'</pre>',parse_mode='HTML')
def ML(update, context):
    new_confirmed_ML=(summary["Countries"][105]["NewConfirmed"])
    total_confirmed_ML=(summary["Countries"][105]["TotalConfirmed"])
    new_deaths_ML=(summary["Countries"][105]["NewDeaths"])
    total_deaths_ML=(summary["Countries"][105]["TotalDeaths"])
    new_recovered_ML=(summary["Countries"][105]["NewRecovered"])
    total_recovered_ML=(summary["Countries"][105]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Mali</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_ML)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_ML)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_ML)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_ML)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_ML)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_ML)+'</pre>',parse_mode='HTML')
def MT(update, context):
    new_confirmed_MT=(summary["Countries"][106]["NewConfirmed"])
    total_confirmed_MT=(summary["Countries"][106]["TotalConfirmed"])
    new_deaths_MT=(summary["Countries"][106]["NewDeaths"])
    total_deaths_MT=(summary["Countries"][106]["TotalDeaths"])
    new_recovered_MT=(summary["Countries"][106]["NewRecovered"])
    total_recovered_MT=(summary["Countries"][106]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Malta</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_MT)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_MT)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_MT)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_MT)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_MT)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_MT)+'</pre>',parse_mode='HTML')
def MR(update, context):
    new_confirmed_MR=(summary["Countries"][107]["NewConfirmed"])
    total_confirmed_MR=(summary["Countries"][107]["TotalConfirmed"])
    new_deaths_MR=(summary["Countries"][107]["NewDeaths"])
    total_deaths_MR=(summary["Countries"][107]["TotalDeaths"])
    new_recovered_MR=(summary["Countries"][107]["NewRecovered"])
    total_recovered_MR=(summary["Countries"][107]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Mauritania</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_MR)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_MR)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_MR)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_MR)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_MR)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_MR)+'</pre>',parse_mode='HTML')
def MU(update, context):
    new_confirmed_MU=(summary["Countries"][108]["NewConfirmed"])
    total_confirmed_MU=(summary["Countries"][108]["TotalConfirmed"])
    new_deaths_MU=(summary["Countries"][108]["NewDeaths"])
    total_deaths_MU=(summary["Countries"][108]["TotalDeaths"])
    new_recovered_MU=(summary["Countries"][108]["NewRecovered"])
    total_recovered_MU=(summary["Countries"][108]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Mauritius</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_MU)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_MU)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_MU)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_MU)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_MU)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_MU)+'</pre>',parse_mode='HTML')
def MX(update, context):
    new_confirmed_MX=(summary["Countries"][109]["NewConfirmed"])
    total_confirmed_MX=(summary["Countries"][109]["TotalConfirmed"])
    new_deaths_MX=(summary["Countries"][109]["NewDeaths"])
    total_deaths_MX=(summary["Countries"][109]["TotalDeaths"])
    new_recovered_MX=(summary["Countries"][109]["NewRecovered"])
    total_recovered_MX=(summary["Countries"][109]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Mexico</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_MX)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_MX)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_MX)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_MX)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_MX)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_MX)+'</pre>',parse_mode='HTML')
def MD(update, context):
    new_confirmed_MD=(summary["Countries"][110]["NewConfirmed"])
    total_confirmed_MD=(summary["Countries"][110]["TotalConfirmed"])
    new_deaths_MD=(summary["Countries"][110]["NewDeaths"])
    total_deaths_MD=(summary["Countries"][110]["TotalDeaths"])
    new_recovered_MD=(summary["Countries"][110]["NewRecovered"])
    total_recovered_MD=(summary["Countries"][110]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Moldova</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_MD)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_MD)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_MD)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_MD)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_MD)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_MD)+'</pre>',parse_mode='HTML')
def MC(update, context):
    new_confirmed_MC=(summary["Countries"][111]["NewConfirmed"])
    total_confirmed_MC=(summary["Countries"][111]["TotalConfirmed"])
    new_deaths_MC=(summary["Countries"][111]["NewDeaths"])
    total_deaths_MC=(summary["Countries"][111]["TotalDeaths"])
    new_recovered_MC=(summary["Countries"][111]["NewRecovered"])
    total_recovered_MC=(summary["Countries"][111]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Monaco</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_MC)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_MC)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_MC)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_MC)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_MC)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_MC)+'</pre>',parse_mode='HTML')
def MN(update, context):
    new_confirmed_MN=(summary["Countries"][112]["NewConfirmed"])
    total_confirmed_MN=(summary["Countries"][112]["TotalConfirmed"])
    new_deaths_MN=(summary["Countries"][112]["NewDeaths"])
    total_deaths_MN=(summary["Countries"][112]["TotalDeaths"])
    new_recovered_MN=(summary["Countries"][112]["NewRecovered"])
    total_recovered_MN=(summary["Countries"][112]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Mongolia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_MN)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_MN)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_MN)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_MN)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_MN)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_MN)+'</pre>',parse_mode='HTML')
def ME(update, context):
    new_confirmed_ME=(summary["Countries"][113]["NewConfirmed"])
    total_confirmed_ME=(summary["Countries"][113]["TotalConfirmed"])
    new_deaths_ME=(summary["Countries"][113]["NewDeaths"])
    total_deaths_ME=(summary["Countries"][113]["TotalDeaths"])
    new_recovered_ME=(summary["Countries"][113]["NewRecovered"])
    total_recovered_ME=(summary["Countries"][113]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Montenegro</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_ME)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_ME)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_ME)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_ME)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_ME)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_ME)+'</pre>',parse_mode='HTML')
def MA(update, context):
    new_confirmed_MA=(summary["Countries"][114]["NewConfirmed"])
    total_confirmed_MA=(summary["Countries"][114]["TotalConfirmed"])
    new_deaths_MA=(summary["Countries"][114]["NewDeaths"])
    total_deaths_MA=(summary["Countries"][114]["TotalDeaths"])
    new_recovered_MA=(summary["Countries"][114]["NewRecovered"])
    total_recovered_MA=(summary["Countries"][114]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Morocco</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_MA)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_MA)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_MA)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_MA)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_MA)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_MA)+'</pre>',parse_mode='HTML')
def MZ(update, context):
    new_confirmed_MZ=(summary["Countries"][115]["NewConfirmed"])
    total_confirmed_MZ=(summary["Countries"][115]["TotalConfirmed"])
    new_deaths_MZ=(summary["Countries"][115]["NewDeaths"])
    total_deaths_MZ=(summary["Countries"][115]["TotalDeaths"])
    new_recovered_MZ=(summary["Countries"][115]["NewRecovered"])
    total_recovered_MZ=(summary["Countries"][115]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Mozambique</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_MZ)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_MZ)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_MZ)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_MZ)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_MZ)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_MZ)+'</pre>',parse_mode='HTML')
def MM(update, context):
    new_confirmed_MM=(summary["Countries"][116]["NewConfirmed"])
    total_confirmed_MM=(summary["Countries"][116]["TotalConfirmed"])
    new_deaths_MM=(summary["Countries"][116]["NewDeaths"])
    total_deaths_MM=(summary["Countries"][116]["TotalDeaths"])
    new_recovered_MM=(summary["Countries"][116]["NewRecovered"])
    total_recovered_MM=(summary["Countries"][116]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Myanmar</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_MM)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_MM)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_MM)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_MM)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_MM)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_MM)+'</pre>',parse_mode='HTML')
def NA(update, context):
    new_confirmed_NA=(summary["Countries"][117]["NewConfirmed"])
    total_confirmed_NA=(summary["Countries"][117]["TotalConfirmed"])
    new_deaths_NA=(summary["Countries"][117]["NewDeaths"])
    total_deaths_NA=(summary["Countries"][117]["TotalDeaths"])
    new_recovered_NA=(summary["Countries"][117]["NewRecovered"])
    total_recovered_NA=(summary["Countries"][117]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Namibia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_NA)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_NA)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_NA)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_NA)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_NA)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_NA)+'</pre>',parse_mode='HTML')
def NP(update, context):
    new_confirmed_NP=(summary["Countries"][118]["NewConfirmed"])
    total_confirmed_NP=(summary["Countries"][118]["TotalConfirmed"])
    new_deaths_NP=(summary["Countries"][118]["NewDeaths"])
    total_deaths_NP=(summary["Countries"][118]["TotalDeaths"])
    new_recovered_NP=(summary["Countries"][118]["NewRecovered"])
    total_recovered_NP=(summary["Countries"][118]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Nepal</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_NP)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_NP)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_NP)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_NP)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_NP)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_NP)+'</pre>',parse_mode='HTML')
def NL(update, context):
    new_confirmed_NL=(summary["Countries"][119]["NewConfirmed"])
    total_confirmed_NL=(summary["Countries"][119]["TotalConfirmed"])
    new_deaths_NL=(summary["Countries"][119]["NewDeaths"])
    total_deaths_NL=(summary["Countries"][119]["TotalDeaths"])
    new_recovered_NL=(summary["Countries"][119]["NewRecovered"])
    total_recovered_NL=(summary["Countries"][119]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Netherlands</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_NL)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_NL)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_NL)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_NL)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_NL)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_NL)+'</pre>',parse_mode='HTML')
def NZ(update, context):
    new_confirmed_NZ=(summary["Countries"][120]["NewConfirmed"])
    total_confirmed_NZ=(summary["Countries"][120]["TotalConfirmed"])
    new_deaths_NZ=(summary["Countries"][120]["NewDeaths"])
    total_deaths_NZ=(summary["Countries"][120]["TotalDeaths"])
    new_recovered_NZ=(summary["Countries"][120]["NewRecovered"])
    total_recovered_NZ=(summary["Countries"][120]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>New Zealand</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_NZ)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_NZ)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_NZ)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_NZ)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_NZ)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_NZ)+'</pre>',parse_mode='HTML')
def NI(update, context):
    new_confirmed_NI=(summary["Countries"][121]["NewConfirmed"])
    total_confirmed_NI=(summary["Countries"][121]["TotalConfirmed"])
    new_deaths_NI=(summary["Countries"][121]["NewDeaths"])
    total_deaths_NI=(summary["Countries"][121]["TotalDeaths"])
    new_recovered_NI=(summary["Countries"][121]["NewRecovered"])
    total_recovered_NI=(summary["Countries"][121]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Nicaragua</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_NI)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_NI)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_NI)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_NI)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_NI)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_NI)+'</pre>',parse_mode='HTML')
def NE(update, context):
    new_confirmed_NE=(summary["Countries"][122]["NewConfirmed"])
    total_confirmed_NE=(summary["Countries"][122]["TotalConfirmed"])
    new_deaths_NE=(summary["Countries"][122]["NewDeaths"])
    total_deaths_NE=(summary["Countries"][122]["TotalDeaths"])
    new_recovered_NE=(summary["Countries"][122]["NewRecovered"])
    total_recovered_NE=(summary["Countries"][122]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Niger</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_NE)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_NE)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_NE)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_NE)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_NE)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_NE)+'</pre>',parse_mode='HTML')
def NG(update, context):
    new_confirmed_NG=(summary["Countries"][123]["NewConfirmed"])
    total_confirmed_NG=(summary["Countries"][123]["TotalConfirmed"])
    new_deaths_NG=(summary["Countries"][123]["NewDeaths"])
    total_deaths_NG=(summary["Countries"][123]["TotalDeaths"])
    new_recovered_NG=(summary["Countries"][123]["NewRecovered"])
    total_recovered_NG=(summary["Countries"][123]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Nigeria</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_NG)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_NG)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_NG)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_NG)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_NG)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_NG)+'</pre>',parse_mode='HTML')
def NO(update, context):
    new_confirmed_NO=(summary["Countries"][124]["NewConfirmed"])
    total_confirmed_NO=(summary["Countries"][124]["TotalConfirmed"])
    new_deaths_NO=(summary["Countries"][124]["NewDeaths"])
    total_deaths_NO=(summary["Countries"][124]["TotalDeaths"])
    new_recovered_NO=(summary["Countries"][124]["NewRecovered"])
    total_recovered_NO=(summary["Countries"][124]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Norway</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_NO)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_NO)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_NO)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_NO)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_NO)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_NO)+'</pre>',parse_mode='HTML')
def OM(update, context):
    new_confirmed_OM=(summary["Countries"][125]["NewConfirmed"])
    total_confirmed_OM=(summary["Countries"][125]["TotalConfirmed"])
    new_deaths_OM=(summary["Countries"][125]["NewDeaths"])
    total_deaths_OM=(summary["Countries"][125]["TotalDeaths"])
    new_recovered_OM=(summary["Countries"][125]["NewRecovered"])
    total_recovered_OM=(summary["Countries"][125]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Oman</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_OM)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_OM)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_OM)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_OM)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_OM)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_OM)+'</pre>',parse_mode='HTML')
def PK(update, context):
    new_confirmed_PK=(summary["Countries"][126]["NewConfirmed"])
    total_confirmed_PK=(summary["Countries"][126]["TotalConfirmed"])
    new_deaths_PK=(summary["Countries"][126]["NewDeaths"])
    total_deaths_PK=(summary["Countries"][126]["TotalDeaths"])
    new_recovered_PK=(summary["Countries"][126]["NewRecovered"])
    total_recovered_PK=(summary["Countries"][126]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Pakistan</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_PK)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_PK)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_PK)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_PK)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_PK)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_PK)+'</pre>',parse_mode='HTML')
def PS(update, context):
    new_confirmed_PS=(summary["Countries"][127]["NewConfirmed"])
    total_confirmed_PS=(summary["Countries"][127]["TotalConfirmed"])
    new_deaths_PS=(summary["Countries"][127]["NewDeaths"])
    total_deaths_PS=(summary["Countries"][127]["TotalDeaths"])
    new_recovered_PS=(summary["Countries"][127]["NewRecovered"])
    total_recovered_PS=(summary["Countries"][127]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Palestinian Territory</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_PS)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_PS)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_PS)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_PS)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_PS)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_PS)+'</pre>',parse_mode='HTML')
def PA(update, context):
    new_confirmed_PA=(summary["Countries"][128]["NewConfirmed"])
    total_confirmed_PA=(summary["Countries"][128]["TotalConfirmed"])
    new_deaths_PA=(summary["Countries"][128]["NewDeaths"])
    total_deaths_PA=(summary["Countries"][128]["TotalDeaths"])
    new_recovered_PA=(summary["Countries"][128]["NewRecovered"])
    total_recovered_PA=(summary["Countries"][128]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Panama</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_PA)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_PA)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_PA)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_PA)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_PA)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_PA)+'</pre>',parse_mode='HTML')
def PG(update, context):
    new_confirmed_PG=(summary["Countries"][129]["NewConfirmed"])
    total_confirmed_PG=(summary["Countries"][129]["TotalConfirmed"])
    new_deaths_PG=(summary["Countries"][129]["NewDeaths"])
    total_deaths_PG=(summary["Countries"][129]["TotalDeaths"])
    new_recovered_PG=(summary["Countries"][129]["NewRecovered"])
    total_recovered_PG=(summary["Countries"][129]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Papua New Guinea</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_PG)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_PG)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_PG)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_PG)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_PG)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_PG)+'</pre>',parse_mode='HTML')
def PY(update, context):
    new_confirmed_PY=(summary["Countries"][130]["NewConfirmed"])
    total_confirmed_PY=(summary["Countries"][130]["TotalConfirmed"])
    new_deaths_PY=(summary["Countries"][130]["NewDeaths"])
    total_deaths_PY=(summary["Countries"][130]["TotalDeaths"])
    new_recovered_PY=(summary["Countries"][130]["NewRecovered"])
    total_recovered_PY=(summary["Countries"][130]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Paraguay</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_PY)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_PY)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_PY)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_PY)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_PY)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_PY)+'</pre>',parse_mode='HTML')
def PE(update, context):
    new_confirmed_PE=(summary["Countries"][131]["NewConfirmed"])
    total_confirmed_PE=(summary["Countries"][131]["TotalConfirmed"])
    new_deaths_PE=(summary["Countries"][131]["NewDeaths"])
    total_deaths_PE=(summary["Countries"][131]["TotalDeaths"])
    new_recovered_PE=(summary["Countries"][131]["NewRecovered"])
    total_recovered_PE=(summary["Countries"][131]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Peru</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_PE)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_PE)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_PE)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_PE)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_PE)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_PE)+'</pre>',parse_mode='HTML')
def PH(update, context):
    new_confirmed_PH=(summary["Countries"][132]["NewConfirmed"])
    total_confirmed_PH=(summary["Countries"][132]["TotalConfirmed"])
    new_deaths_PH=(summary["Countries"][132]["NewDeaths"])
    total_deaths_PH=(summary["Countries"][132]["TotalDeaths"])
    new_recovered_PH=(summary["Countries"][132]["NewRecovered"])
    total_recovered_PH=(summary["Countries"][132]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Philippines</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_PH)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_PH)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_PH)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_PH)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_PH)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_PH)+'</pre>',parse_mode='HTML')
def PL(update, context):
    new_confirmed_PL=(summary["Countries"][133]["NewConfirmed"])
    total_confirmed_PL=(summary["Countries"][133]["TotalConfirmed"])
    new_deaths_PL=(summary["Countries"][133]["NewDeaths"])
    total_deaths_PL=(summary["Countries"][133]["TotalDeaths"])
    new_recovered_PL=(summary["Countries"][133]["NewRecovered"])
    total_recovered_PL=(summary["Countries"][133]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Poland</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_PL)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_PL)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_PL)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_PL)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_PL)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_PL)+'</pre>',parse_mode='HTML')
def PT(update, context):
    new_confirmed_PT=(summary["Countries"][134]["NewConfirmed"])
    total_confirmed_PT=(summary["Countries"][134]["TotalConfirmed"])
    new_deaths_PT=(summary["Countries"][134]["NewDeaths"])
    total_deaths_PT=(summary["Countries"][134]["TotalDeaths"])
    new_recovered_PT=(summary["Countries"][134]["NewRecovered"])
    total_recovered_PT=(summary["Countries"][134]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Portugal</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_PT)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_PT)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_PT)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_PT)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_PT)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_PT)+'</pre>',parse_mode='HTML')
def QA(update, context):
    new_confirmed_QA=(summary["Countries"][135]["NewConfirmed"])
    total_confirmed_QA=(summary["Countries"][135]["TotalConfirmed"])
    new_deaths_QA=(summary["Countries"][135]["NewDeaths"])
    total_deaths_QA=(summary["Countries"][135]["TotalDeaths"])
    new_recovered_QA=(summary["Countries"][135]["NewRecovered"])
    total_recovered_QA=(summary["Countries"][135]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Qatar</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_QA)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_QA)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_QA)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_QA)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_QA)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_QA)+'</pre>',parse_mode='HTML')
def XK(update, context):
    new_confirmed_XK=(summary["Countries"][136]["NewConfirmed"])
    total_confirmed_XK=(summary["Countries"][136]["TotalConfirmed"])
    new_deaths_XK=(summary["Countries"][136]["NewDeaths"])
    total_deaths_XK=(summary["Countries"][136]["TotalDeaths"])
    new_recovered_XK=(summary["Countries"][136]["NewRecovered"])
    total_recovered_XK=(summary["Countries"][136]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Republic of Kosovo</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_XK)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_XK)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_XK)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_XK)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_XK)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_XK)+'</pre>',parse_mode='HTML')
def RO(update, context):
    new_confirmed_RO=(summary["Countries"][137]["NewConfirmed"])
    total_confirmed_RO=(summary["Countries"][137]["TotalConfirmed"])
    new_deaths_RO=(summary["Countries"][137]["NewDeaths"])
    total_deaths_RO=(summary["Countries"][137]["TotalDeaths"])
    new_recovered_RO=(summary["Countries"][137]["NewRecovered"])
    total_recovered_RO=(summary["Countries"][137]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Romania</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_RO)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_RO)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_RO)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_RO)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_RO)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_RO)+'</pre>',parse_mode='HTML')
def RU(update, context):
    new_confirmed_RU=(summary["Countries"][138]["NewConfirmed"])
    total_confirmed_RU=(summary["Countries"][138]["TotalConfirmed"])
    new_deaths_RU=(summary["Countries"][138]["NewDeaths"])
    total_deaths_RU=(summary["Countries"][138]["TotalDeaths"])
    new_recovered_RU=(summary["Countries"][138]["NewRecovered"])
    total_recovered_RU=(summary["Countries"][138]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Russian Federation</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_RU)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_RU)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_RU)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_RU)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_RU)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_RU)+'</pre>',parse_mode='HTML')
def RW(update, context):
    new_confirmed_RW=(summary["Countries"][139]["NewConfirmed"])
    total_confirmed_RW=(summary["Countries"][139]["TotalConfirmed"])
    new_deaths_RW=(summary["Countries"][139]["NewDeaths"])
    total_deaths_RW=(summary["Countries"][139]["TotalDeaths"])
    new_recovered_RW=(summary["Countries"][139]["NewRecovered"])
    total_recovered_RW=(summary["Countries"][139]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Rwanda</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_RW)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_RW)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_RW)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_RW)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_RW)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_RW)+'</pre>',parse_mode='HTML')
def KN(update, context):
    new_confirmed_KN=(summary["Countries"][140]["NewConfirmed"])
    total_confirmed_KN=(summary["Countries"][140]["TotalConfirmed"])
    new_deaths_KN=(summary["Countries"][140]["NewDeaths"])
    total_deaths_KN=(summary["Countries"][140]["TotalDeaths"])
    new_recovered_KN=(summary["Countries"][140]["NewRecovered"])
    total_recovered_KN=(summary["Countries"][140]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Saint Kitts and Nevis</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_KN)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_KN)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_KN)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_KN)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_KN)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_KN)+'</pre>',parse_mode='HTML')
def LC(update, context):
    new_confirmed_LC=(summary["Countries"][141]["NewConfirmed"])
    total_confirmed_LC=(summary["Countries"][141]["TotalConfirmed"])
    new_deaths_LC=(summary["Countries"][141]["NewDeaths"])
    total_deaths_LC=(summary["Countries"][141]["TotalDeaths"])
    new_recovered_LC=(summary["Countries"][141]["NewRecovered"])
    total_recovered_LC=(summary["Countries"][141]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Saint Lucia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_LC)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_LC)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_LC)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_LC)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_LC)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_LC)+'</pre>',parse_mode='HTML')
def VC(update, context):
    new_confirmed_VC=(summary["Countries"][142]["NewConfirmed"])
    total_confirmed_VC=(summary["Countries"][142]["TotalConfirmed"])
    new_deaths_VC=(summary["Countries"][142]["NewDeaths"])
    total_deaths_VC=(summary["Countries"][142]["TotalDeaths"])
    new_recovered_VC=(summary["Countries"][142]["NewRecovered"])
    total_recovered_VC=(summary["Countries"][142]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Saint Vincent and Grenadines</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_VC)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_VC)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_VC)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_VC)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_VC)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_VC)+'</pre>',parse_mode='HTML')
def SM(update, context):
    new_confirmed_SM=(summary["Countries"][143]["NewConfirmed"])
    total_confirmed_SM=(summary["Countries"][143]["TotalConfirmed"])
    new_deaths_SM=(summary["Countries"][143]["NewDeaths"])
    total_deaths_SM=(summary["Countries"][143]["TotalDeaths"])
    new_recovered_SM=(summary["Countries"][143]["NewRecovered"])
    total_recovered_SM=(summary["Countries"][143]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>San Marino</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_SM)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_SM)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_SM)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_SM)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_SM)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_SM)+'</pre>',parse_mode='HTML')
def ST(update, context):
    new_confirmed_ST=(summary["Countries"][144]["NewConfirmed"])
    total_confirmed_ST=(summary["Countries"][144]["TotalConfirmed"])
    new_deaths_ST=(summary["Countries"][144]["NewDeaths"])
    total_deaths_ST=(summary["Countries"][144]["TotalDeaths"])
    new_recovered_ST=(summary["Countries"][144]["NewRecovered"])
    total_recovered_ST=(summary["Countries"][144]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Sao Tome and Principe</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_ST)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_ST)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_ST)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_ST)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_ST)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_ST)+'</pre>',parse_mode='HTML')
def SA(update, context):
    new_confirmed_SA=(summary["Countries"][145]["NewConfirmed"])
    total_confirmed_SA=(summary["Countries"][145]["TotalConfirmed"])
    new_deaths_SA=(summary["Countries"][145]["NewDeaths"])
    total_deaths_SA=(summary["Countries"][145]["TotalDeaths"])
    new_recovered_SA=(summary["Countries"][145]["NewRecovered"])
    total_recovered_SA=(summary["Countries"][145]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Saudi Arabia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_SA)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_SA)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_SA)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_SA)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_SA)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_SA)+'</pre>',parse_mode='HTML')
def SN(update, context):
    new_confirmed_SN=(summary["Countries"][146]["NewConfirmed"])
    total_confirmed_SN=(summary["Countries"][146]["TotalConfirmed"])
    new_deaths_SN=(summary["Countries"][146]["NewDeaths"])
    total_deaths_SN=(summary["Countries"][146]["TotalDeaths"])
    new_recovered_SN=(summary["Countries"][146]["NewRecovered"])
    total_recovered_SN=(summary["Countries"][146]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Senegal</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_SN)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_SN)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_SN)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_SN)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_SN)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_SN)+'</pre>',parse_mode='HTML')
def RS(update, context):
    new_confirmed_RS=(summary["Countries"][147]["NewConfirmed"])
    total_confirmed_RS=(summary["Countries"][147]["TotalConfirmed"])
    new_deaths_RS=(summary["Countries"][147]["NewDeaths"])
    total_deaths_RS=(summary["Countries"][147]["TotalDeaths"])
    new_recovered_RS=(summary["Countries"][147]["NewRecovered"])
    total_recovered_RS=(summary["Countries"][147]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Serbia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_RS)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_RS)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_RS)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_RS)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_RS)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_RS)+'</pre>',parse_mode='HTML')
def SC(update, context):
    new_confirmed_SC=(summary["Countries"][148]["NewConfirmed"])
    total_confirmed_SC=(summary["Countries"][148]["TotalConfirmed"])
    new_deaths_SC=(summary["Countries"][148]["NewDeaths"])
    total_deaths_SC=(summary["Countries"][148]["TotalDeaths"])
    new_recovered_SC=(summary["Countries"][148]["NewRecovered"])
    total_recovered_SC=(summary["Countries"][148]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Seychelles</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_SC)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_SC)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_SC)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_SC)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_SC)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_SC)+'</pre>',parse_mode='HTML')
def SL(update, context):
    new_confirmed_SL=(summary["Countries"][149]["NewConfirmed"])
    total_confirmed_SL=(summary["Countries"][149]["TotalConfirmed"])
    new_deaths_SL=(summary["Countries"][149]["NewDeaths"])
    total_deaths_SL=(summary["Countries"][149]["TotalDeaths"])
    new_recovered_SL=(summary["Countries"][149]["NewRecovered"])
    total_recovered_SL=(summary["Countries"][149]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Sierra Leone</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_SL)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_SL)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_SL)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_SL)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_SL)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_SL)+'</pre>',parse_mode='HTML')

def SG(update, context):
    new_confirmed_SG=(summary["Countries"][150]["NewConfirmed"])
    total_confirmed_SG=(summary["Countries"][150]["TotalConfirmed"])
    new_deaths_SG=(summary["Countries"][150]["NewDeaths"])
    total_deaths_SG=(summary["Countries"][150]["TotalDeaths"])
    new_recovered_SG=(summary["Countries"][150]["NewRecovered"])
    total_recovered_SG=(summary["Countries"][150]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Singapore</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_SG)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_SG)+'</pre>'     
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_SG)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_SG)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_SG)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_SG)+'</pre>',parse_mode='HTML')
def SK(update, context):
    new_confirmed_SK=(summary["Countries"][151]["NewConfirmed"])
    total_confirmed_SK=(summary["Countries"][151]["TotalConfirmed"])
    new_deaths_SK=(summary["Countries"][151]["NewDeaths"])
    total_deaths_SK=(summary["Countries"][151]["TotalDeaths"])
    new_recovered_SK=(summary["Countries"][151]["NewRecovered"])
    total_recovered_SK=(summary["Countries"][151]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Slovakia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_SK)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_SK)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_SK)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_SK)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_SK)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_SK)+'</pre>',parse_mode='HTML')
def SI(update, context):
    new_confirmed_SI=(summary["Countries"][152]["NewConfirmed"])
    total_confirmed_SI=(summary["Countries"][152]["TotalConfirmed"])
    new_deaths_SI=(summary["Countries"][152]["NewDeaths"])
    total_deaths_SI=(summary["Countries"][152]["TotalDeaths"])
    new_recovered_SI=(summary["Countries"][152]["NewRecovered"])
    total_recovered_SI=(summary["Countries"][152]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Slovenia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_SI)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_SI)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_SI)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_SI)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_SI)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_SI)+'</pre>',parse_mode='HTML')
def SO(update, context):
    new_confirmed_SO=(summary["Countries"][153]["NewConfirmed"])
    total_confirmed_SO=(summary["Countries"][153]["TotalConfirmed"])
    new_deaths_SO=(summary["Countries"][153]["NewDeaths"])
    total_deaths_SO=(summary["Countries"][153]["TotalDeaths"])
    new_recovered_SO=(summary["Countries"][153]["NewRecovered"])
    total_recovered_SO=(summary["Countries"][153]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Somalia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_SO)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_SO)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_SO)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_SO)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_SO)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_SO)+'</pre>',parse_mode='HTML')
def ZA(update, context):
    new_confirmed_ZA=(summary["Countries"][154]["NewConfirmed"])
    total_confirmed_ZA=(summary["Countries"][154]["TotalConfirmed"])
    new_deaths_ZA=(summary["Countries"][154]["NewDeaths"])
    total_deaths_ZA=(summary["Countries"][154]["TotalDeaths"])
    new_recovered_ZA=(summary["Countries"][154]["NewRecovered"])
    total_recovered_ZA=(summary["Countries"][154]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>South Africa</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_ZA)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_ZA)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_ZA)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_ZA)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_ZA)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_ZA)+'</pre>',parse_mode='HTML')
def SS(update, context):
    new_confirmed_SS=(summary["Countries"][155]["NewConfirmed"])
    total_confirmed_SS=(summary["Countries"][155]["TotalConfirmed"])
    new_deaths_SS=(summary["Countries"][155]["NewDeaths"])
    total_deaths_SS=(summary["Countries"][155]["TotalDeaths"])
    new_recovered_SS=(summary["Countries"][155]["NewRecovered"])
    total_recovered_SS=(summary["Countries"][155]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>South Sudan</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_SS)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_SS)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_SS)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_SS)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_SS)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_SS)+'</pre>',parse_mode='HTML')
def ES(update, context):
    new_confirmed_ES=(summary["Countries"][156]["NewConfirmed"])
    total_confirmed_ES=(summary["Countries"][156]["TotalConfirmed"])
    new_deaths_ES=(summary["Countries"][156]["NewDeaths"])
    total_deaths_ES=(summary["Countries"][156]["TotalDeaths"])
    new_recovered_ES=(summary["Countries"][156]["NewRecovered"])
    total_recovered_ES=(summary["Countries"][156]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Spain</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_ES)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_ES)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_ES)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_ES)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_ES)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_ES)+'</pre>',parse_mode='HTML')
def LK(update, context):
    new_confirmed_LK=(summary["Countries"][157]["NewConfirmed"])
    total_confirmed_LK=(summary["Countries"][157]["TotalConfirmed"])
    new_deaths_LK=(summary["Countries"][157]["NewDeaths"])
    total_deaths_LK=(summary["Countries"][157]["TotalDeaths"])
    new_recovered_LK=(summary["Countries"][157]["NewRecovered"])
    total_recovered_LK=(summary["Countries"][157]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Sri Lanka</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_LK)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_LK)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_LK)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_LK)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_LK)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_LK)+'</pre>',parse_mode='HTML')
def SD(update, context):
    new_confirmed_SD=(summary["Countries"][158]["NewConfirmed"])
    total_confirmed_SD=(summary["Countries"][158]["TotalConfirmed"])
    new_deaths_SD=(summary["Countries"][158]["NewDeaths"])
    total_deaths_SD=(summary["Countries"][158]["TotalDeaths"])
    new_recovered_SD=(summary["Countries"][158]["NewRecovered"])
    total_recovered_SD=(summary["Countries"][158]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Sudan</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_SD)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_SD)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_SD)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_SD)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_SD)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_SD)+'</pre>',parse_mode='HTML')
def SR(update, context):
    new_confirmed_SR=(summary["Countries"][159]["NewConfirmed"])
    total_confirmed_SR=(summary["Countries"][159]["TotalConfirmed"])
    new_deaths_SR=(summary["Countries"][159]["NewDeaths"])
    total_deaths_SR=(summary["Countries"][159]["TotalDeaths"])
    new_recovered_SR=(summary["Countries"][159]["NewRecovered"])
    total_recovered_SR=(summary["Countries"][159]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Suriname</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_SR)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_SR)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_SR)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_SR)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_SR)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_SR)+'</pre>',parse_mode='HTML')
def SZ(update, context):
    new_confirmed_SZ=(summary["Countries"][160]["NewConfirmed"])
    total_confirmed_SZ=(summary["Countries"][160]["TotalConfirmed"])
    new_deaths_SZ=(summary["Countries"][160]["NewDeaths"])
    total_deaths_SZ=(summary["Countries"][160]["TotalDeaths"])
    new_recovered_SZ=(summary["Countries"][160]["NewRecovered"])
    total_recovered_SZ=(summary["Countries"][160]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Swaziland</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_SZ)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_SZ)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_SZ)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_SZ)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_SZ)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_SZ)+'</pre>',parse_mode='HTML')
def SE(update, context):
    new_confirmed_SE=(summary["Countries"][161]["NewConfirmed"])
    total_confirmed_SE=(summary["Countries"][161]["TotalConfirmed"])
    new_deaths_SE=(summary["Countries"][161]["NewDeaths"])
    total_deaths_SE=(summary["Countries"][161]["TotalDeaths"])
    new_recovered_SE=(summary["Countries"][161]["NewRecovered"])
    total_recovered_SE=(summary["Countries"][161]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Sweden</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_SE)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_SE)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_SE)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_SE)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_SE)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_SE)+'</pre>',parse_mode='HTML')
def CH(update, context):
    new_confirmed_CH=(summary["Countries"][162]["NewConfirmed"])
    total_confirmed_CH=(summary["Countries"][162]["TotalConfirmed"])
    new_deaths_CH=(summary["Countries"][162]["NewDeaths"])
    total_deaths_CH=(summary["Countries"][162]["TotalDeaths"])
    new_recovered_CH=(summary["Countries"][162]["NewRecovered"])
    total_recovered_CH=(summary["Countries"][162]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Switzerland</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_CH)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_CH)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_CH)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_CH)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_CH)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_CH)+'</pre>',parse_mode='HTML')
def SY(update, context):
    new_confirmed_SY=(summary["Countries"][163]["NewConfirmed"])
    total_confirmed_SY=(summary["Countries"][163]["TotalConfirmed"])
    new_deaths_SY=(summary["Countries"][163]["NewDeaths"])
    total_deaths_SY=(summary["Countries"][163]["TotalDeaths"])
    new_recovered_SY=(summary["Countries"][163]["NewRecovered"])
    total_recovered_SY=(summary["Countries"][163]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Syrian Arab Republic (Syria)</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_SY)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_SY)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_SY)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_SY)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_SY)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_SY)+'</pre>',parse_mode='HTML')
def TW(update, context):
    new_confirmed_TW=(summary["Countries"][164]["NewConfirmed"])
    total_confirmed_TW=(summary["Countries"][164]["TotalConfirmed"])
    new_deaths_TW=(summary["Countries"][164]["NewDeaths"])
    total_deaths_TW=(summary["Countries"][164]["TotalDeaths"])
    new_recovered_TW=(summary["Countries"][164]["NewRecovered"])
    total_recovered_TW=(summary["Countries"][164]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Taiwan, Republic of China</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_TW)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_TW)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_TW)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_TW)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_TW)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_TW)+'</pre>',parse_mode='HTML')
def TJ(update, context):
    new_confirmed_TJ=(summary["Countries"][165]["NewConfirmed"])
    total_confirmed_TJ=(summary["Countries"][165]["TotalConfirmed"])
    new_deaths_TJ=(summary["Countries"][165]["NewDeaths"])
    total_deaths_TJ=(summary["Countries"][165]["TotalDeaths"])
    new_recovered_TJ=(summary["Countries"][165]["NewRecovered"])
    total_recovered_TJ=(summary["Countries"][165]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Tajikistan</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_TJ)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_TJ)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_TJ)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_TJ)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_TJ)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_TJ)+'</pre>',parse_mode='HTML')
def TZ(update, context):
    new_confirmed_TZ=(summary["Countries"][166]["NewConfirmed"])
    total_confirmed_TZ=(summary["Countries"][166]["TotalConfirmed"])
    new_deaths_TZ=(summary["Countries"][166]["NewDeaths"])
    total_deaths_TZ=(summary["Countries"][166]["TotalDeaths"])
    new_recovered_TZ=(summary["Countries"][166]["NewRecovered"])
    total_recovered_TZ=(summary["Countries"][166]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Tanzania, United Republic of</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_TZ)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_TZ)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_TZ)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_TZ)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_TZ)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_TZ)+'</pre>',parse_mode='HTML')
def TH(update, context):
    new_confirmed_TH=(summary["Countries"][167]["NewConfirmed"])
    total_confirmed_TH=(summary["Countries"][167]["TotalConfirmed"])
    new_deaths_TH=(summary["Countries"][167]["NewDeaths"])
    total_deaths_TH=(summary["Countries"][167]["TotalDeaths"])
    new_recovered_TH=(summary["Countries"][167]["NewRecovered"])
    total_recovered_TH=(summary["Countries"][167]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Thailand</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_TH)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_TH)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_TH)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_TH)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_TH)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_TH)+'</pre>',parse_mode='HTML')
def TL(update, context):
    new_confirmed_TL=(summary["Countries"][168]["NewConfirmed"])
    total_confirmed_TL=(summary["Countries"][168]["TotalConfirmed"])
    new_deaths_TL=(summary["Countries"][168]["NewDeaths"])
    total_deaths_TL=(summary["Countries"][168]["TotalDeaths"])
    new_recovered_TL=(summary["Countries"][168]["NewRecovered"])
    total_recovered_TL=(summary["Countries"][168]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Timor-Leste</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_TL)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_TL)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_TL)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_TL)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_TL)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_TL)+'</pre>',parse_mode='HTML')
def TG(update, context):
    new_confirmed_TG=(summary["Countries"][169]["NewConfirmed"])
    total_confirmed_TG=(summary["Countries"][169]["TotalConfirmed"])
    new_deaths_TG=(summary["Countries"][169]["NewDeaths"])
    total_deaths_TG=(summary["Countries"][169]["TotalDeaths"])
    new_recovered_TG=(summary["Countries"][169]["NewRecovered"])
    total_recovered_TG=(summary["Countries"][169]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Togo</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_TG)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_TG)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_TG)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_TG)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_TG)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_TG)+'</pre>',parse_mode='HTML')
def TT(update, context):
    new_confirmed_TT=(summary["Countries"][170]["NewConfirmed"])
    total_confirmed_TT=(summary["Countries"][170]["TotalConfirmed"])
    new_deaths_TT=(summary["Countries"][170]["NewDeaths"])
    total_deaths_TT=(summary["Countries"][170]["TotalDeaths"])
    new_recovered_TT=(summary["Countries"][170]["NewRecovered"])
    total_recovered_TT=(summary["Countries"][170]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Trinidad and Tobago</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_TT)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_TT)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_TT)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_TT)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_TT)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_TT)+'</pre>',parse_mode='HTML')
def TN(update, context):
    new_confirmed_TN=(summary["Countries"][171]["NewConfirmed"])
    total_confirmed_TN=(summary["Countries"][171]["TotalConfirmed"])
    new_deaths_TN=(summary["Countries"][171]["NewDeaths"])
    total_deaths_TN=(summary["Countries"][171]["TotalDeaths"])
    new_recovered_TN=(summary["Countries"][171]["NewRecovered"])
    total_recovered_TN=(summary["Countries"][171]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Tunisia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_TN)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_TN)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_TN)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_TN)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_TN)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_TN)+'</pre>',parse_mode='HTML')
def TR(update, context):
    new_confirmed_TR=(summary["Countries"][172]["NewConfirmed"])
    total_confirmed_TR=(summary["Countries"][172]["TotalConfirmed"])
    new_deaths_TR=(summary["Countries"][172]["NewDeaths"])
    total_deaths_TR=(summary["Countries"][172]["TotalDeaths"])
    new_recovered_TR=(summary["Countries"][172]["NewRecovered"])
    total_recovered_TR=(summary["Countries"][172]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Turkey</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_TR)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_TR)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_TR)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_TR)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_TR)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_TR)+'</pre>',parse_mode='HTML')
def UG(update, context):
    new_confirmed_UG=(summary["Countries"][173]["NewConfirmed"])
    total_confirmed_UG=(summary["Countries"][173]["TotalConfirmed"])
    new_deaths_UG=(summary["Countries"][173]["NewDeaths"])
    total_deaths_UG=(summary["Countries"][173]["TotalDeaths"])
    new_recovered_UG=(summary["Countries"][173]["NewRecovered"])
    total_recovered_UG=(summary["Countries"][173]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Uganda</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_UG)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_UG)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_UG)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_UG)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_UG)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_UG)+'</pre>',parse_mode='HTML')
def UA(update, context):
    new_confirmed_UA=(summary["Countries"][174]["NewConfirmed"])
    total_confirmed_UA=(summary["Countries"][174]["TotalConfirmed"])
    new_deaths_UA=(summary["Countries"][174]["NewDeaths"])
    total_deaths_UA=(summary["Countries"][174]["TotalDeaths"])
    new_recovered_UA=(summary["Countries"][174]["NewRecovered"])
    total_recovered_UA=(summary["Countries"][174]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Ukraine</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_UA)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_UA)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_UA)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_UA)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_UA)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_UA)+'</pre>',parse_mode='HTML')
def AE(update, context):
    new_confirmed_AE=(summary["Countries"][175]["NewConfirmed"])
    total_confirmed_AE=(summary["Countries"][175]["TotalConfirmed"])
    new_deaths_AE=(summary["Countries"][175]["NewDeaths"])
    total_deaths_AE=(summary["Countries"][175]["TotalDeaths"])
    new_recovered_AE=(summary["Countries"][175]["NewRecovered"])
    total_recovered_AE=(summary["Countries"][175]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>United Arab Emirates</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_AE)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_AE)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_AE)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_AE)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_AE)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_AE)+'</pre>',parse_mode='HTML')
def GB(update, context):
    new_confirmed_GB=(summary["Countries"][176]["NewConfirmed"])
    total_confirmed_GB=(summary["Countries"][176]["TotalConfirmed"])
    new_deaths_GB=(summary["Countries"][176]["NewDeaths"])
    total_deaths_GB=(summary["Countries"][176]["TotalDeaths"])
    new_recovered_GB=(summary["Countries"][176]["NewRecovered"])
    total_recovered_GB=(summary["Countries"][176]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>United Kingdom</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_GB)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_GB)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_GB)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_GB)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_GB)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_GB)+'</pre>',parse_mode='HTML')
def US(update, context):
    new_confirmed_US=(summary["Countries"][177]["NewConfirmed"])
    total_confirmed_US=(summary["Countries"][177]["TotalConfirmed"])
    new_deaths_US=(summary["Countries"][177]["NewDeaths"])
    total_deaths_US=(summary["Countries"][177]["TotalDeaths"])
    new_recovered_US=(summary["Countries"][177]["NewRecovered"])
    total_recovered_US=(summary["Countries"][177]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>United States of America</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_US)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_US)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_US)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_US)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_US)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_US)+'</pre>',parse_mode='HTML')
def UY(update, context):
    new_confirmed_UY=(summary["Countries"][178]["NewConfirmed"])
    total_confirmed_UY=(summary["Countries"][178]["TotalConfirmed"])
    new_deaths_UY=(summary["Countries"][178]["NewDeaths"])
    total_deaths_UY=(summary["Countries"][178]["TotalDeaths"])
    new_recovered_UY=(summary["Countries"][178]["NewRecovered"])
    total_recovered_UY=(summary["Countries"][178]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Uruguay</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_UY)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_UY)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_UY)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_UY)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_UY)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_UY)+'</pre>',parse_mode='HTML')
def UZ(update, context):
    new_confirmed_UZ=(summary["Countries"][179]["NewConfirmed"])
    total_confirmed_UZ=(summary["Countries"][179]["TotalConfirmed"])
    new_deaths_UZ=(summary["Countries"][179]["NewDeaths"])
    total_deaths_UZ=(summary["Countries"][179]["TotalDeaths"])
    new_recovered_UZ=(summary["Countries"][179]["NewRecovered"])
    total_recovered_UZ=(summary["Countries"][179]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Uzbekistan</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_UZ)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_UZ)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_UZ)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_UZ)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_UZ)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_UZ)+'</pre>',parse_mode='HTML')
def VE(update, context):
    new_confirmed_VE=(summary["Countries"][180]["NewConfirmed"])
    total_confirmed_VE=(summary["Countries"][180]["TotalConfirmed"])
    new_deaths_VE=(summary["Countries"][180]["NewDeaths"])
    total_deaths_VE=(summary["Countries"][180]["TotalDeaths"])
    new_recovered_VE=(summary["Countries"][180]["NewRecovered"])
    total_recovered_VE=(summary["Countries"][180]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Venezuela (Bolivarian Republic)</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_VE)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_VE)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_VE)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_VE)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_VE)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_VE)+'</pre>',parse_mode='HTML')
def VN(update, context):
    new_confirmed_VN=(summary["Countries"][181]["NewConfirmed"])
    total_confirmed_VN=(summary["Countries"][181]["TotalConfirmed"])
    new_deaths_VN=(summary["Countries"][181]["NewDeaths"])
    total_deaths_VN=(summary["Countries"][181]["TotalDeaths"])
    new_recovered_VN=(summary["Countries"][181]["NewRecovered"])
    total_recovered_VN=(summary["Countries"][181]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Viet Nam</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_VN)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_VN)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_VN)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_VN)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_VN)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_VN)+'</pre>',parse_mode='HTML')
def EH(update, context):
    new_confirmed_EH=(summary["Countries"][182]["NewConfirmed"])
    total_confirmed_EH=(summary["Countries"][182]["TotalConfirmed"])
    new_deaths_EH=(summary["Countries"][182]["NewDeaths"])
    total_deaths_EH=(summary["Countries"][182]["TotalDeaths"])
    new_recovered_EH=(summary["Countries"][182]["NewRecovered"])
    total_recovered_EH=(summary["Countries"][182]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Western Sahara</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_EH)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_EH)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_EH)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_EH)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_EH)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_EH)+'</pre>',parse_mode='HTML')
def YE(update, context):
    new_confirmed_YE=(summary["Countries"][183]["NewConfirmed"])
    total_confirmed_YE=(summary["Countries"][183]["TotalConfirmed"])
    new_deaths_YE=(summary["Countries"][183]["NewDeaths"])
    total_deaths_YE=(summary["Countries"][183]["TotalDeaths"])
    new_recovered_YE=(summary["Countries"][183]["NewRecovered"])
    total_recovered_YE=(summary["Countries"][183]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Yemen</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_YE)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_YE)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_YE)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_YE)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_YE)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_YE)+'</pre>',parse_mode='HTML')
def ZM(update, context):
    new_confirmed_ZM=(summary["Countries"][184]["NewConfirmed"])
    total_confirmed_ZM=(summary["Countries"][184]["TotalConfirmed"])
    new_deaths_ZM=(summary["Countries"][184]["NewDeaths"])
    total_deaths_ZM=(summary["Countries"][184]["TotalDeaths"])
    new_recovered_ZM=(summary["Countries"][184]["NewRecovered"])
    total_recovered_ZM=(summary["Countries"][184]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Zambia</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_ZM)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_ZM)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_ZM)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_ZM)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_ZM)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_ZM)+'</pre>',parse_mode='HTML')
def ZW(update, context):
    new_confirmed_ZW=(summary["Countries"][185]["NewConfirmed"])
    total_confirmed_ZW=(summary["Countries"][185]["TotalConfirmed"])
    new_deaths_ZW=(summary["Countries"][185]["NewDeaths"])
    total_deaths_ZW=(summary["Countries"][185]["TotalDeaths"])
    new_recovered_ZW=(summary["Countries"][185]["NewRecovered"])
    total_recovered_ZW=(summary["Countries"][185]["TotalRecovered"])
    update.message.reply_text('<b>Corona Statistics:</b><pre>Zimbabwe</pre>'
   '\n<b>New Confirmed :</b> ''<pre>'+str(new_confirmed_ZW)+'</pre>'
   '\n<b>Total Confirmed :</b> ''<pre>'+str(total_confirmed_ZW)+'</pre>'
   '\n<b>New Deaths :</b> ''<pre>'+str(new_deaths_ZW)+'</pre>'
   '\n<b>Total Deaths :</b> ''<pre>'+str(total_deaths_ZW)+'</pre>'
   '\n<b>New Recovered :</b> ''<pre>'+str(new_recovered_ZW)+'</pre>'
   '\n<b>Total Recovered :</b> ''<pre>'+str(total_recovered_ZW)+'</pre>',parse_mode='HTML')


def help(update, context):
    update.message.reply_text("Hi! , I\'m Corona Chan!\nSo what I basically do is, I give you\nCorona Statistics.\nTo know Global Stats do /global\nTo know the stats of a specific country, do /<country code>\nWondering where to find country codes?\nDon\'t Worry! We got you covered .\nSimply do /countrycodes\nA message with all country codes will pop up.\nUse those country codes to gt the statistics of a country .\nI hope you guys will enjoy this Bot.\nArigatou!") 

def about(update, context):
    keyboard = [[InlineKeyboardButton('GitHub',url ="https://github.com/adenosinetp10"),InlineKeyboardButton('Paypal',url='https://paypal.me/adenosinetp10')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Corona Chan will get you Corona Statistics from all around the world.\nDeveloper : @iLEWDloli\nDeveloped in Python using python-telegram-bot\nMade possible due to Coronavirus COVID19 API\nIf you liked this Bot and want to support me\n Then donate me.",reply_markup=reply_markup)

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
