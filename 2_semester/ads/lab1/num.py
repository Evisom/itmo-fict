from bruteforce import bruteforceSearch
from BoyerMoore import BoyerMooreSearch
from KnuthMorrisPratt import KnuthMorrisPrattSearch
from RabinKarp import RabinKarpSearch

def sieve(n):
    a = []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)
    return(a)

string = ''
prime_numbers = sieve(500)
for i in prime_numbers:
    string+=str(i)

print(string)

bf_r = dict()
bm_r = dict()
rk_r = dict()
kmp_r = dict()

for i in range(10, 100):
    bf = bruteforceSearch(string, str(i)) or []
    bm = BoyerMooreSearch(string, str(i)) or []
    rk = RabinKarpSearch(string, str(i)) or []
    kmp = KnuthMorrisPrattSearch(string, str(i)) or []
    bf_r[i] = len(bf)
    bm_r[i] = len(bm)
    rk_r[i] = len(rk)
    kmp_r[i] = len(kmp)

print(bf_r == bm_r == rk_r == kmp_r)
print({k: v for k, v in sorted(bf_r.items(), key=lambda item: item[1], reverse=True)})