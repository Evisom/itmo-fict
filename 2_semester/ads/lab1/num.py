from bruteforce import bruteforceSearch
from BoyerMoore import BoyerMooreSearch
from KnuthMorrisPratt import KnuthMorrisPrattSearch
from RabinKarp import RabinKarpSearch
import timeit


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
prime_numbers = sieve(3572)
for i in prime_numbers:
    string+=str(i)

# print(string)

bf_r = dict()
bm_r = dict()
rk_r = dict()
kmp_r = dict()

# for i in range(10, 100):
#     bf = bruteforceSearch(string, str(i)) or []
#     bm = BoyerMooreSearch(string, str(i)) or []
#     rk = RabinKarpSearch(string, str(i)) or []
#     kmp = KnuthMorrisPrattSearch(string, str(i)) or []
#     bf_r[i] = len(bf)
#     bm_r[i] = len(bm)
#     rk_r[i] = len(rk)
#     kmp_r[i] = len(kmp)

# print(bf_r == bm_r == rk_r == kmp_r)

# timeit.timeit("KnuthMorrisPrattSearch(i[0], i[1])", globals=globals(), number=n)/n

def z1():
    for i in range(10, 100):
        bf = bruteforceSearch(string, str(i)) or []
        bf_r[i] = len(bf)

def z2():
    for i in range(10, 100):
        bm = BoyerMooreSearch(string, str(i)) or []
        bm_r[i] = len(bm)

def z3():
    for i in range(10, 100):
        rk = RabinKarpSearch(string, str(i)) or []
        rk_r[i] = len(rk)

def z4():
    for i in range(10, 100):
        kmp = KnuthMorrisPrattSearch(string, str(i)) or []
        kmp_r[i] = len(kmp)

n = 100
t1 = (timeit.timeit("z1()", globals=globals(), number=n)/n)
t2 = (timeit.timeit("z2()", globals=globals(), number=n)/n)
t3 = (timeit.timeit("z3()", globals=globals(), number=n)/n)
t4 = (timeit.timeit("z4()", globals=globals(), number=n)/n)


r1 = {k: v for k, v in sorted(bf_r.items(), key=lambda item: item[1], reverse=True)}
r2 = {k: v for k, v in sorted(bm_r.items(), key=lambda item: item[1], reverse=True)}
r3 = {k: v for k, v in sorted(rk_r.items(), key=lambda item: item[1], reverse=True)}
r4 = {k: v for k, v in sorted(kmp_r.items(), key=lambda item: item[1], reverse=True)}

print(list(r1.keys())[0], r1[list(r1.keys())[0]], 'Bruteforce', t1, 's')
print(list(r2.keys())[0], r2[list(r2.keys())[0]], 'Boyer-Moore', t2, 's')
print(list(r3.keys())[0], r3[list(r3.keys())[0]], 'Rabin-Karp', t3, 's')
print(list(r4.keys())[0], r4[list(r4.keys())[0]], 'Knuth-Morris-Pratt', t4, 's')