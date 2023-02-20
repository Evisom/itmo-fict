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

l = 0
c = 0
for i in range(0, len(essay)):
    r = KnuthMorrisPrattSearch(origin, essay[i])
    if len(r) > 0:
        l+=1
        if l >= 3:
            c+=len(essay[i])
    else:
        l = 0

print(c/l_e)
