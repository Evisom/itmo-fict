def bruteforceSearch(string, substring):
    indexes = []
    for i in range(0, len(string)-len(substring)+1):
        if string[i:i+len(substring)] == substring:
            indexes.append(i)
    
    return indexes
