from bruteforce import bruteforceSearch
from BoyerMoore import BoyerMooreSearch
from KnuthMorrisPratt import KnuthMorrisPrattSearch
from RabinKarp import RabinKarpSearch
import timeit

testfile = open('test.txt').readline()
tests = [
    [testfile, 'ab']
    # ['ЭТОИЭТОТ', 'ТОТ'],
    # ['aaabab', 'b'],
    # ['aefdgaabadfgagdgdab', 'ab'],
    # ['asfgdshgrtsfdgfasshtdsasf', 'as'],
    # ['fdsgsndhtryegfd', 'dsf'],
    # ['sdfghjhkfuyjthdgfgnmhfkyturytesfdgfbgshrg','y']
]

for i in tests:
    n = 100
    print('Average time for 100 iterations')
    print('String length - ', len(testfile), 'symbols')
    print('bruteforce: ', timeit.timeit("bruteforceSearch(i[0], i[1])", globals=globals(), number=n)/n)
    print('Boyer-Moore: ', timeit.timeit("BoyerMooreSearch(i[0], i[1])", globals=globals(), number=n)/n)
    print('Rabin-Karp: ', timeit.timeit("RabinKarpSearch(i[0], i[1])", globals=globals(), number=n)/n)
    print('Knuth-Morris-Pratt: ', timeit.timeit("KnuthMorrisPrattSearch(i[0], i[1])", globals=globals(), number=n)/n)
    