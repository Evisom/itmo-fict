def getAlp(string):
    alp = []
    for i in string:
        if not(i in alp):
            alp.append(i)
    return alp 

def hash(string, alp):
    hash_sum = 0
    alp_l = len(alp)
    for i in range(len(string)-1, -1, -1):
        hash_sum += alp.index(string[i]) * alp_l**(i)
    return hash_sum

def RabinKarpSearch(string, substring):
    alp = getAlp(string)
    substring_hash = hash(substring, alp)
    indexes = []
    for i in range(0, len(string)-len(substring)+1):
        fragment = string[i:i+len(substring)]
        fragment_hash = hash(fragment, alp)
        if fragment_hash==substring_hash:
            indexes.append(i)

    return indexes       

