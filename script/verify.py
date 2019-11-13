# only supprot python 2 !!
import json, sys
a = dict(json.load(open(sys.argv[1])))
b = dict(json.load(open(sys.argv[2])))
# 0 for equal
def test(x, y):
    if len(x) != len(y):
        return False
    for k in x:
        if x[k] != y[k]:
            return False
    return True

if test(a, b):
    print("Success!")
else:
    print("Fail!")
