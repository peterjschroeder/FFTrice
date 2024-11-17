from fftcg_parser import *
import re


def addcard(theset, name, code,  pt, text, card_type, color, cost, file):

    code_for_image = code

    if re.search('pr', code.lower()):
        code = code
    else:
        code = code

    file.write('    <card>\n')
    file.write('      <name>' + name + ' (' + code + ')' + '</name>\n')
    file.write('      <text>' + prettyTrice(text) + '</text>\n')
    file.write('      <prop>\n')
    file.write(card_type)
    file.write('        <manacost>' + prettyTrice(cost) + '</manacost>\n')
    file.write('        <colors>' + prettyTrice(color) + '</colors>\n')
    if int(pt) > 0:
        file.write('        <pt>' + pt + '</pt>\n')
    file.write('      </prop>\n')
    file.write('      <set picurl="' + getimageURL(code_for_image) + '">' + theset + '</set>\n')
    file.write('      <tablerow>%s</tablerow>\n' % ('0' if 'Backup' in card_type 
        else '2' if 'Forward' in card_type else '3' if re.search(r'\bSummon\b', card_type) else '1'))
    file.write('    </card>\n')


def addset(theset, file):
    file.write('    <set>\n')
    file.write('      <name>' + theset + '</name>\n')
    file.write('      <longname>' + theset + '</longname>\n')
    file.write('      <settype>Custom</settype>\n')
    file.write('      <releasedate></releasedate>\n')
    file.write('    </set>\n')


a = loadJson('https://fftcg.square-enix-games.com/en/get-cards', {"language":"en","text":""})
b = []

for x in a:
    b.append(x['set'][0])

with open('cards.xml', 'w', encoding='utf8') as myfile:
    myfile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    myfile.write('<cockatrice_carddatabase version="4">\n')
    myfile.write('  <sets>\n')

    for x in set(b):
        addset(x, myfile)

    myfile.write('  </sets>\n')
    myfile.write('  <cards>\n')

    for x in a:
        card_name = x['name_en']
        card_name = card_name.replace(u"\u00FA", "u")  # Addresses u Cuchulainn, the Impure 2-133R

        # FIXME: Some entries are missing category_1
        try:
            card_type = str('        <type>' + prettyTrice(x['type_en']) + ' - '+ prettyTrice(x['category_1']) + ' - ' + prettyTrice(x['job_en']) + '</type>\n')
        except:
            card_type = str('        <type>' + prettyTrice(x['type_en']) + ' - ' + prettyTrice(x['job_en']) + '</type>\n')
        card_type = card_type.replace(' - ' + u"\u2015" + '</type>', '</type>')
        card_type = card_type.replace(' - </type>', '</type>')

        card_power = x['power']
        card_power = card_power.replace(u"\uFF0D", "")
        card_power = card_power.replace(u"\u2015", "")

        card_code = x['code']

        card_cost = x['cost']

        card_text = x['text_en']

        # FIXME: Some entries are missing element
        try:
            card_element = x['element'][0]
        except:
            card_element = ""

        card_set = x['set'][0]

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


