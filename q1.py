import re

def reg(input_string, pattern, dot):
    "Given an input string , pattern and dot or star matching rule returns all the matches found"
    if dot:
        res = re.findall(pattern+'.', input_string)
    else:
        res = re.findall(pattern + '*', input_string)
    return res


test1 = reg('boomboomboom', 'boom', dot = True)
print(test1)

test2 = reg('boomboomboom', 'boom', dot = False)
print(test2)

