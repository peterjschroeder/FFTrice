from fftcg_parser import *
import re

a = loadJson('https://fftcg.square-enix-games.com/getcards')

b = []

for x in a:
    b.append(x['Set'])

with open('cards.xml', 'a+', encoding='utf8') as myfile:
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

        card_type = str('      <type>' + prettyTrice(x['Type_EN']) + ' - '+ prettyTrice(x['Category_1']) + ' - ' + prettyTrice(x['Job_EN']) + '</type>\n')
        card_type = card_type.replace(' - ' + u"\u2015" + '</type>', '</type>')
        card_type = card_type.replace(' - </type>', '</type>')
        card_power = x['Power']
        card_power = card_power.replace(u"\uFF0D", '')
        card_power = card_power.replace(u"\u2015", "")
        card_code = x['Code']

        if re.search(r'\d\-\d{3}[a-zA-Z]/', x['Code']):
            b = card_code.replace('(' ,'').replace(')', '').split('/')

            for y in b:
                myfile.write('    <card>\n')
                myfile.write('      <set picURL="' + getimageURL(x['Code']) + '">' + x['Set'] + '</set>\n')
                myfile.write('      <name>' + card_name + ' (' + str(y[:-1]) + ')' + '</name>\n')
                myfile.write('      <pt>' + card_power + '</pt>\n')
                myfile.write('      <text>' + prettyTrice(x['Text_EN']) + '</text>\n')
                myfile.write(card_type)
                myfile.write('      <color>' + prettyTrice(x['Element']) + '</color>\n')
                myfile.write('      <manacost>' + prettyTrice(x['Cost']) + '</manacost>\n')
                myfile.write('    </card>\n')

        else:
            myfile.write('    <card>\n')
            myfile.write('      <set picURL="' + getimageURL(x['Code']) + '">' + x['Set'] + '</set>\n')
            myfile.write('      <name>' + card_name + ' (' + x['Code'][:-1] + ')' + '</name>\n')
            myfile.write('      <pt>' + card_power + '</pt>\n')
            myfile.write('      <text>' + prettyTrice(x['Text_EN']) + '</text>\n')
            myfile.write(card_type)
            myfile.write('      <color>' + prettyTrice(x['Element']) + '</color>\n')
            myfile.write('      <manacost>' + prettyTrice(x['Cost']) + '</manacost>\n')
            myfile.write('    </card>\n')

    myfile.write('  </cards>\n')
    myfile.write('</cockatrice_carddatabase>')