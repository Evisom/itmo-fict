from bruteforce import bruteforceSearch
from BoyerMoore import BoyerMooreSearch
from KnuthMorrisPratt import KnuthMorrisPrattSearch
from RabinKarp import RabinKarpSearch

tests = [
    ['ЭТОИЭТОТ', 'ТОТ'],
    ['aaabab', 'b'],
    ['aefdgaabadfgagdgdab', 'ab'],
    ['asfgdshgrtsfdgfasshtdsasf', 'as'],
    ['fdsgsndhtryegfd', 'dsf'],
    ['sdfghjhkfuyjthdgfgnmhfkyturytesfdgfbgshrg','y']
]

for i in tests:
    if ( bruteforceSearch(i[0], i[1]) == BoyerMooreSearch(i[0], i[1]) and BoyerMooreSearch(i[0], i[1]) == RabinKarpSearch(i[0], i[1]) and RabinKarpSearch(i[0], i[1]) ==  KnuthMorrisPrattSearch(i[0], i[1])):
        print('✅', KnuthMorrisPrattSearch(i[0], i[1]))
    else: 
        print('❌')
    print()