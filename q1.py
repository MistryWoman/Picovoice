import re

def reg(input_string, pattern, dot):
    "Given an input string , pattern and dot or star matching rule returns all the matches found"
    if dot:
        res = re.match(pattern+'.', input_string)
    else:
        res = re.match('(' + pattern + ')*', input_string)
    return res


test1 = reg('boomboom', 'boom', dot = True)
print(test1)

test2 = reg('boomboom', 'boom', dot = False)
print(test2)