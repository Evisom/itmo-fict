def BoyerMooreSearch(string, substring):
    indexes = []
    i = 0
    while i <= len(string) -len(substring):
        correct = True
        for q in range(i, i+len(substring)):
            if string[q] != substring[q-i]:
                correct = False 
                break 
        if correct:
            indexes.append(i)
            i+=1
        else:
            exist = False 
            for q in range(i+len(substring)-1, i, -1):
                if string[q] == substring[0]:
                    exist = True 
                    i = q 
                    break 
            if not(exist):
                i += len(substring)
    return( indexes)

# BoyerMoore('ЭТОИЭТОТ', 'ТОТ')