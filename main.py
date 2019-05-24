from fftcg_parser import *

a = loadJson('https://fftcg.square-enix-games.com/getcards')

b = []

for x in a:
    b.append(x['Set'])

b = set(b)

with open('cards.txt' , 'a+') as myfile:
    myfile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    myfile.write('<cockatrice_carddatabase version="3">\n')
    myfile.write('  <sets>\n')

    for x in b:
        myfile.write('    <set>\n')
        myfile.write('      <name>' + x + '</name>\n')
        myfile.write('      <longname>' + x + '</longname>\n')
        myfile.write('      <settype>Custom</settype>\n')
        myfile.write('    </set>\n')

    myfile.write('  </sets>\n')
    myfile.write('  <cards>\n')

    for x in a:
        myfile.write('    <card>\n')
        myfile.write('      <set picURL="' + getimageURL(x['Code']) + '">' + x['Set'] + '</set>\n')
        myfile.write('      <name>' + x['Name_EN'] + ' (' + x['Code'] + ')' + '</name>\n')
        myfile.write('    </card>\n')
    myfile.write('  </cards>\n')
    myfile.write('</cockatrice_carddatabase>')