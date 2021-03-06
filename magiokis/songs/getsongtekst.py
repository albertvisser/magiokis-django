"""getsongtekst.py

read/update songtekst from external (XML) storage
"""
import pathlib
import shutil
import xml.etree.ElementTree as et
ROOT = pathlib.Path("/home/albert/magiokis/data/zing")


def gettekst(name):
    """read songtekst from XML file
    """
    file = ROOT / name  # os.path.join(ROOT.encode('utf-8'), name.encode('utf-8'))
    if not file.exists():
        return [file, ""]
    tree = et.ElementTree(file=str(file))
    rt = tree.getroot()
    titel = tekst = ""
    for element in list(rt):
        if element.tag == "titel":
            titel = element.text
        elif element.tag == "couplet":
            tekst += "\n"
            for subel in list(element):
                if subel.tag == "regel":
                    tekst += subel.text + "\n"
    return titel, tekst


def updatetekst(name, titel, tekst):
    """write songtekst back to XML file
    """
    file = str(ROOT / name)
    tree = et.ElementTree(file=file)
    root = et.Element('songtekst')
    new = et.SubElement(root, 'titel')
    new.text = titel
    regels = tekst.split('\n')
    if regels[0].strip() != '':
        cpl = et.SubElement(root, 'couplet')
    if regels[-1].strip() == '':
        regels = regels[:-1]
    for inp in regels:
        inp = inp.strip()
        if inp == '':
            cpl = et.SubElement(root, 'couplet')
        else:
            rgl = et.SubElement(cpl, 'regel')
            rgl.text = inp
    tree = et.ElementTree(root)
    ## try:
    shutil.copyfile(file, file + '.old')
    ## except IOError:
        ## pass
    tree.write(file)

if __name__ == "__main__":
    titel, tekst = gettekst('Solid body.xml')
    print('>>>{}<<<'.format(titel))
    for x in tekst.split('\n'):
        print('>>>{}<<<'.format(x))
