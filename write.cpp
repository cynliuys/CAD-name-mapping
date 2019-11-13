#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <list>
#include "nameMap.h"
using namespace std;

void NameMap::writePy(const char* file) {
	ofstream ofs;
	ofs.open(file);

	ofs << "import json,sys" << endl; // explicitly import built-in Python libraries

	// command: ./nmpgen <map_in.json> <python_script.py>

	// open <map_in.json>, insert the two lists of elements into a and b
	ofs << "a,b = json.load(open(sys.argv[1]))" << endl; 

	// print private member vector<pair<unsigned, unsigned> >  _movement;
	if(_movement.size()!=0){
		ofs << "m=[";
		for (vector<pair<unsigned, unsigned> >::iterator it = _movement.begin(); it < _movement.end() - 1; it++ ) {
			ofs << it->first << ",";
		}
		ofs << _movement.back().first << "]" << endl;
		ofs << "n=[";
		for (vector<pair<unsigned, unsigned> >::iterator it = _movement.begin(); it < _movement.end() - 1; it++ ) {
			ofs << it->second << ",";
		}
		ofs << _movement.back().second << "]" << endl;
	}

	ofs << "b.sort()" << endl; // Python sort() sort by ASCII as well as C++
	if(_movement.size()!=0){
		// zip() makes an iterator that aggregates elements from each of the iterables
		ofs << "for i,j in zip(m,n):" << endl;
		// remember indentation in loop (4 spaces)
		// list: insert(pos, elmnt) adds an element at the specified position
		// list: pop(pos) removes the element at the specified position
      if(_reverse) {
		   ofs << "    b.insert(i+j,b.pop(i))" << endl; 
      }
      else {
		   ofs << "    b.insert(j,b.pop(i+j))" << endl; 
      }
	}


	// write a file called <python_script.py>
	// sorted() returns a new sorted list from the items in iterable
	ofs << "json.dump(dict(zip(sorted(a),b)),open(sys.argv[2],'w'),indent=2)" << endl;

	ofs.close();
}

void NameMap::writePy_block(const char* file) {
	ofstream ofs;
	ofs.open(file);

	// command: ./nmpgen <map_in.json> <python_script.py>
	ofs << "import json,sys" << endl;
	ofs << "a,b = json.load(open(sys.argv[1]))" << endl; 

	if(_blockMovement.size()!=0){
		ofs << "m=[";
		for (vector<Triple>::iterator it=_blockMovement.begin(); it<_blockMovement.end()-1; it++ ) {
			ofs << it->first << ",";
		}
		ofs << _blockMovement.back().first << "]" << endl;
		ofs << "n=[";
		for (vector<Triple>::iterator it=_blockMovement.begin(); it<_blockMovement.end() - 1; it++ ) {
			ofs << it->second << ",";
		}
		ofs << _blockMovement.back().second << "]" << endl;
		ofs << "o=[";
		for (vector<Triple>::iterator it=_blockMovement.begin(); it<_blockMovement.end() - 1; it++ ) {
			ofs << it->third << ",";
		}
		ofs << _blockMovement.back().third << "]" << endl;
	}

	ofs << "b.sort()" << endl;
	if(_blockMovement.size()!=0){
		ofs << "for i,j,k in zip(m,n,o):" << endl;
		ofs << "	for x in range(k):" << endl;
		if(_blockReverse) {
			ofs << "		b.insert(i+j-x,b.pop(i-x))" << endl; 
		}
		else{
			ofs << "		b.insert(j+x,b.pop(i+j+x))" << endl; 
		}
	}
	ofs << "json.dump(dict(zip(sorted(a),b)),open(sys.argv[2],'w'),indent=2)" << endl;

	ofs.close();
}
