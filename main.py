from fftcg_parser import *

a = loadJson('https://fftcg.square-enix-games.com/getcards')

with open('cards.txt' , 'a+') as myfile:
    for x in a:
        myfile.write('    <card>\n')
        myfile.write('      <set picURL="' + getimageURL(x['Code']) + '">' + x['Set'] + '</set>\n')
        myfile.write('      <name>' + x['Name_EN'] + ' (' + x['Code'] + ')' + '</name>\n')
        myfile.write('    </card>\n')