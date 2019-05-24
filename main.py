from fftcg_parser import *

a = loadJson('https://fftcg.square-enix-games.com/getcards')

b = []

for x in a:
    b.append(x['Set'])

with open('cards.xml' , 'a+') as myfile:
    myfile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    myfile.write('<cockatrice_carddatabase version="3">\n')
    myfile.write('  <sets>\n')

    for x in set(b):
        myfile.write('    <set>\n')
        myfile.write('      <name>' + x + '</name>\n')
        myfile.write('      <longname>' + x + '</longname>\n')
        myfile.write('      <settype>Custom</settype>\n')
        myfile.write('    </set>\n')

    myfile.write('  </sets>\n')
    myfile.write('  <cards>\n')

    for x in a:
        card_name = x['Name_EN']

        card_name = card_name.replace(u"\u00FA", "u")  # Addresses u Cuchulainn, the Impure 2-133R

        myfile.write('    <card>\n')
        myfile.write('      <set picURL="' + getimageURL(x['Code']) + '">' + x['Set'] + '</set>\n')
        myfile.write('      <name>' + card_name + ' (' + x['Code'][:-1] + ')' + '</name>\n')
        myfile.write('      <pt>' + x['Power'] + '</pt>\n')
        myfile.write('      <text>' + prettyTrice(x['Text_EN']) + '</text>\n')
        myfile.write('      <type>' + prettyTrice(x['Type_EN']) + ' - '+ prettyTrice(x['Category_1']) + ' - ' + prettyTrice(x['Job_EN']) + '</type>\n')
        myfile.write('      <color>' + prettyTrice(x['Element']) + '</color>\n')
        myfile.write('      <manacost>' + prettyTrice(x['Cost']) + '</manacost>\n')
        myfile.write('    </card>\n')

    myfile.write('  </cards>\n')
    myfile.write('</cockatrice_carddatabase>')