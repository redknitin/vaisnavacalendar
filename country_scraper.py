__author__ = 'nitinr'


from bs4 import BeautifulSoup
from urllib import request, response
from unidecode import unidecode
import xml.etree.ElementTree as ET


def runme():
    home_markup = request.urlopen('http://www.vaisnavacalendar.com/').read()
    #home_markup = str(home_markup, 'iso-8859-1')
    soup = BeautifulSoup(home_markup)

    rootEl = ET.Element('countries')

    for iter in soup.find(id='CIID').find_all('option'):
        iteroption = ET.SubElement(rootEl, 'country', {'value': iter['value'], 'text': unidecode(iter.string).capitalize()})
        #dont use .text of iteroption - that will make it the innerText

    tree = ET.ElementTree(rootEl)
    tree.write('countrySel.xml')

if __name__ == '__main__':
    runme()