from fftcg_parser import *
import re


def addcard(theset, name, code,  pt, text, card_type, color, cost, file):
    file.write('    <card>\n')
    file.write('      <set picURL="' + getimageURL(code) + '">' + theset + '</set>\n')
    file.write('      <name>' + name + ' (' + code[:-1] + ')' + '</name>\n')
    file.write('      <pt>' + pt + '</pt>\n')
    file.write('      <text>' + prettyTrice(text) + '</text>\n')
    file.write(card_type)
    file.write('      <color>' + prettyTrice(color) + '</color>\n')
    file.write('      <manacost>' + prettyTrice(cost) + '</manacost>\n')
    file.write('    </card>\n')


def addset(theset, file):
    file.write('    <set>\n')
    file.write('      <name>' + theset + '</name>\n')
    file.write('      <longname>' + theset + '</longname>\n')
    file.write('      <settype>Custom</settype>\n')
    file.write('    </set>\n')


a = loadJson('https://fftcg.square-enix-games.com/getcards')
b = []

for x in a:
    b.append(x['Set'])

with open('cards.xml', 'a+', encoding='utf8') as myfile:
    myfile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    myfile.write('<cockatrice_carddatabase version="3">\n')
    myfile.write('  <sets>\n')

    for x in set(b):
        addset(x, myfile)

    myfile.write('  </sets>\n')
    myfile.write('  <cards>\n')

    for x in a:
        card_name = x['Name_EN']
        card_name = card_name.replace(u"\u00FA", "u")  # Addresses u Cuchulainn, the Impure 2-133R

        card_type = str('      <type>' + prettyTrice(x['Type_EN']) + ' - '+ prettyTrice(x['Category_1']) + ' - ' + prettyTrice(x['Job_EN']) + '</type>\n')
        card_type = card_type.replace(' - ' + u"\u2015" + '</type>', '</type>')
        card_type = card_type.replace(' - </type>', '</type>')

        card_power = x['Power']
        card_power = card_power.replace(u"\uFF0D", "")
        card_power = card_power.replace(u"\u2015", "")

        card_code = x['Code']

        card_cost = x['Cost']

        card_text = x['Text_EN']

        card_element = x['Element']

        card_set = x['Set']

        if re.search(r'\d-\d{3}[a-zA-Z]/', card_code):
            b = card_code.replace('(' ,'').replace(')', '').split('/')

            # As of Opus 8, reprints in the JSON appear as original printing, and the reprint with both codes
            # so far this is consistent and nothing has been reprint more than once below may not work if they change
            # things up may need for loop to iterate over split codes

            # [btawa@backdoor ~]$ curl -s https://fftcg.square-enix-games.com/getcards | jq . |grep 1-011
            #      "Code": "1-011C",
            #      "Code": "6-006C/1-011C",

            addcard(card_set, card_name, str(b[0]), card_power, card_text, card_type, card_element, card_cost, myfile)

        else:
            addcard(card_set, card_name, card_code, card_power, card_text, card_type, card_element, card_cost, myfile)

    myfile.write('  </cards>\n')
    myfile.write('</cockatrice_carddatabase>')


