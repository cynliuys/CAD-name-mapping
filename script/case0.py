import json,sys
a,b = json.load(open(sys.argv[1]))
b.sort()
json.dump(dict(zip(sorted(a),b)),open(sys.argv[2],'w'),indent=2)
