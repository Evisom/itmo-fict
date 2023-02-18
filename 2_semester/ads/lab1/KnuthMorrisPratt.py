def prefix(string):
    a = [0] * len(string)
    k = 0

    for q in range(2, len(string) + 1):
        while k > 0 and string[k] != string[q - 1]:
            k = a[k - 1]
        if string[k] == string[q - 1]:
            k += 1
        a[q - 1] = k

    return a


def KnuthMorrisPrattSearch(string, substring):
    indexes = []
    substring_prefix = prefix(substring)

    j = 0
    for i in range(len(string)):
        while j > 0 and string[i] != substring[j]:
            j = substring_prefix[j - 1]
        if string[i] == substring[j]: j += 1
        if j == len(substring): 
            indexes.append(i - (j - 1))
            j = substring_prefix[j - 1]
            
    
    return indexes