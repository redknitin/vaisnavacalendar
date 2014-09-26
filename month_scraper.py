__author__ = 'nitinr'


from bs4 import BeautifulSoup
from urllib import request, response
import xml.etree.ElementTree as ET


url = 'http://www.vaisnavacalendar.com/vcal.php?month=08&year=2014&lang=en&CIID=477'
month_vedic_days = ['Pratipat', 'Dvitiya', 'Tritiya', 'Caturthi', 'Pancami', 'Sasti', 'Saptami', 'Astami', 'Navami', 'Dasami', 'Ekadasi', 'Suddha Ekadasi', 'Dvadasi', 'Trayodasi', 'Caturdasi', 'Purnima', 'Amavasya']
month_week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
zodiac_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']


def runme():
    #global url
    month_markup = request.urlopen(url).read()
    soup = BeautifulSoup(month_markup)
    #return soup.find_all('table')[4].find_all('td')
    month_text = soup.find_all('table')[3].get_text()
    outfile = open('mon_txt.txt', 'w')
    outfile.write(month_text)

    arr = process_txt(month_text)

    rootEl = ET.Element('month')

    for key, value in arr.items():
        iter = ET.SubElement(rootEl, 'day', {'weekday': str(key), 'description': value})

    tree = ET.ElementTree(rootEl)
    tree.write('month.xml')


def process_txt(month_text):
    month_text = month_text.strip()
    curr_date = 0
    blank_count = 0
    month_arr = {}
    for i in month_text.split('\n'):
        if len(i.strip()) == 0:
            blank_count += 1
            continue
        else:
            blank_count = 0

        if i.isdigit():
            curr_date = int(i)
            month_arr[curr_date] = ''
            continue
        if i == 0: continue
        if i in month_vedic_days: continue
        if i in month_week_days: continue
        if i in zodiac_signs: continue

        month_arr[curr_date] += i
    return month_arr


if __name__ == '__main__':
    runme()
