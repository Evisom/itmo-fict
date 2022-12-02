tests = [
    '()()()', # OK
    '((()))', # OK
    '()(())', # OK
    '()()(())((()))', # OK
    '()()()()(()())()', # OK

    ')(',
    '()()()((',
    '()()(()))',
    '((())))',
    '((()))(',
    '()))((())))'
]

def isCorrect(s):
    depth = 0
    for i in range(len(s)):
        if s[i] == '(':
            depth+=1
        if s[i] == ')':
            depth-=1
        if depth < 0:
            return i
    if depth != 0:
        return len(s) - i
    return True 


for i in tests:
    print(isCorrect(i))