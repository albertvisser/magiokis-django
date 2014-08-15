import os
## import xml.etree.ElementTree as et
import lxml.etree as et

root = et.Element('django-objects',version="1.0")
tree = et.ElementTree(file="verhalen.xml")
verhalen = tree.getroot()
verhaal_lijst = []

x = verhalen.find("path")
base_path = x.text
cats = verhalen.find("categorieen")
cat_dict = {}
hoofdstuk_id = 0
for x in list(cats):
    cat_id = x.get("id")
    cat_naam = x.get("naam")
    y = et.SubElement(root,"object",pk=cat_id,model="vertel.bundel")
    z1 = et.SubElement(y,'field',type="CharField",name="titel")
    z1.text = cat_naam
    z2 = et.SubElement(y,'field',type="TextField",name="beschrijving")
    z3 = et.SubElement(y,'field',to="vertel.verhaal",name="inhoud",rel="ManyToManyRel")
    cat_dict[cat_id] = z3
for x in verhalen.findall("verhaal"):
    cat_id = x.get("categorie")
    verhaal_id = x.get("id")
    verhaal_titel = x.get("titel")
    verhaal_data = base_path + x.find('url').text
    y = et.SubElement(root,"object",pk=verhaal_id,model="vertel.verhaal")
    z1 = et.SubElement(y,"field",type="CharField",name="titel")
    z1.text = verhaal_titel
    z2 = et.SubElement(y,"field",to="vertel.verteller",name="schrijver",rel="ManyToOneRel")
    z2.text = "1"
    z3 = et.SubElement(y,"field",type="DateTimeField",name="datum_begonnen")
    z3.text = "2000-01-01 00:00:00"
    z4 = et.SubElement(y,"field",type="DateTimeField",name="datum_afgemaakt")
    z5 = et.SubElement(z4,"None")
    et.SubElement(cat_dict[cat_id],"object",pk=verhaal_id)
    if os.path.splitext(verhaal_data)[1] != '.xml':
        print 'niet geparsed:',verhaal_data
        continue
    verhaal_tree = et.ElementTree(file=verhaal_data)
    verhaal = verhaal_tree.getroot()
    t = verhaal.find('titel')
    t = t.text if t.text is not None else ''
    if t.upper() != verhaal_titel.upper():
        print "\n  ".join(("titel in verhaal ongelijk aan titel in index:",t.encode('iso-8859-1').join(('"','"')),verhaal_titel.encode('iso-8859-1').join(('"','"'))))
    for y in verhaal.findall('hoofdstuk'):
        hoofdstuk_id += 1
        z = et.SubElement(root,"object",pk=str(hoofdstuk_id),model="vertel.hoofdstuk")
        z1 = et.SubElement(z,'field',to="vertel.verhaal",name="verhaal",rel="ManyToOneRel")
        z1.text = verhaal_id
        z2 = et.SubElement(z,'field',type="CharField",name="titel")
        t2 = y.find('titel2')
        z2.text = t2.text if t2 is not None else ''
        z3 = et.SubElement(z,'field',type="TextField",name="inhoud")
        z3.text = '\n'.join([q.text if q.text is not None else '' for q in y.findall('alinea')])
et.ElementTree(root).write('verhaal.xml')
