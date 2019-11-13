import json,sys
a,b = json.load(open(sys.argv[1]))
m=[2,0]
n=[4,2]
o=[2,1]
b.sort()
for i,j,k in zip(m,n,o):
	for x in range(k):
		b.insert(i+j-x,b.pop(i-x))
json.dump(dict(zip(sorted(a),b)),open(sys.argv[2],'w'),indent=2)
