#include <iostream>
#include <sstream>
#include <fstream>
#include "namePair.h"

using namespace std;

void 
NamePair::setComSubstr(){
	size_t minStrLen = (_first._string.size()<_second._string.size()) ? _first._string.size() : _second._string.size();
	for(size_t i=0 ; i<minStrLen ; ++i){
		if(_first._string[i] == _second._string[i]) _comSubstr.push_back(_first._string[i]);
		else break;
	}
}
