import wikipedia
import pypandoc
from KnuthMorrisPratt import KnuthMorrisPrattSearch

wikipedia.set_lang("ru")

origin = wikipedia.page("Рентгеновское излучение").content.lower()
essay = pypandoc.convert_file('essay.docx', 'plain').lower()

symbols = ',.-=!:()—[];'

for i in symbols:
    origin = origin.replace(i, '')
    essay = essay.replace(i, '')

essay = essay.split()

c = ''
for i in essay:
    if KnuthMorrisPrattSearch(origin, i):
        c+='1'
    else:
        c+=' '

c = c.split()

total = 0
for i in c:
    if len(i) >= 3:
        total+=len(i)

print(total/len(essay) * 100 , '%')


# print(origin)

# print(essay)