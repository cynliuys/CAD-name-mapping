import json,sys
a,b = json.load(open(sys.argv[1]))
m=[2,0]
n=[1,1]
b.sort()
for i,j in zip(m,n):
    b.insert(i+j,b.pop(i))
json.dump(dict(zip(sorted(a),b)),open(sys.argv[2],'w'),indent=2)
