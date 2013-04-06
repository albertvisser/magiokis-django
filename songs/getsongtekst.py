# getsongtekst.py
import os
import xml.etree.ElementTree as et

def gettekst(name):
    file = os.path.join("songs/zing",name)
    if not os.path.exists(file):
        return 
    tree = et.ElementTree(file=file)
    rt = tree.getroot()
    titel = tekst = ""
    for element in list(rt):
        if element.tag == "titel":
            titel = element.text
        elif element.tag == "couplet":
            tekst += "<br/>"
            for subel in list(element):
                if subel.tag == "regel":
                    tekst += subel.text + "<br/>"
    return titel, tekst                    


