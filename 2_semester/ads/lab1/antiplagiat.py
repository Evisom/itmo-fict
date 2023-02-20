import wikipedia
import pypandoc
from KnuthMorrisPratt import KnuthMorrisPrattSearch

wikipedia.set_lang("ru")

origin = wikipedia.page("Рентгеновское излучение").content.lower()
essay = pypandoc.convert_file('essay.docx', 'plain').lower()
l_e = len(essay)
symbols = ',.-=!:()—[];'

for i in symbols:
    origin = origin.replace(i, '')
    essay = essay.replace(i, '')
essay = essay.split()

i = 0
s = 0
while i < len(essay) - 2:
    l = 0
    fragment = essay[i]
    for q in range(i+1, len(essay)):
        fragment += ' ' + essay[q]
        if fragment in origin:
            l+=1
        elif l >= 3:
            s+=len(fragment)
            i = q
            break 
        else:
            i = q
            break

print(s/l_e)

# print(c/l_e)
