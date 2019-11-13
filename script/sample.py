# this is a sample for our python script
import json,sys
a,b=json.load(open(sys.argv[1]))
# our movements
m,n=[],[]
b.sort()
for i,j in zip(m,n):
    b.insert(j,b.pop(m))
json.dump(dict(zip(sorted(a),b)),open(sys.argv[2],'w'))
