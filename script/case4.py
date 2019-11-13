import json,sys
a,b = json.load(open(sys.argv[1]))
m=[13,13,3,3,3,3]
n=[322,323,324,325,326,327]
b.sort()
for i,j in zip(m,n):
    b.insert(j,b.pop(i+j))
json.dump(dict(zip(sorted(a),b)),open(sys.argv[2],'w'),indent=2)
