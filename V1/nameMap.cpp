#include <iostream>
#include <sstream>
#include <fstream>
#include "nameMap.h"

using namespace std;


bool 
NameMap::creatNameMap(const char* file){
	ifstream ifs;
	ifs.open(file);
	if (!ifs.is_open()){
		cerr << "Error: cannot open file \"" << file << "\"!"<<endl;
		return false;
	}

	string line = "";
	if(!getline(ifs, line, '\n')){
		cerr << "Error: the format is not correct"<<endl;
		return false;
	}
	if(line[0] != '{'){
		cerr << "Error: the format is not correct"<<endl;
		return false;
	}
	while(getline(ifs, line, '\n')){
		if(line[0] == '}') break;
		istringstream ss(line);
		string str1 = "";
		string str2 = "";
		getline(ss, str1, '"');
		getline(ss, str1, '"');
		getline(ss, str2, '"');
		getline(ss, str2, '"');
		NamePair * ptr = new NamePair(str1, str2);
		_nameList.push_back(ptr);
	}
	return true;
}

void
NameMap::grouping(){
	for(size_t i=0 ; i<_nameList.size() ; ++i){
		_nameList[i]->setComSubstr();
		if(!findGroup(_nameList[i])){
    		vector<NamePair *> tempVec;
    		tempVec.push_back(_nameList[i]);
    		_groupList.push_back(tempVec);
		}
	}
}

bool
NameMap::findGroup(NamePair * targetPrt){
	for(size_t i=0 ; i<_groupList.size() ; ++i){
		NamePair * grpPrt = _groupList[i][0];
		if(grpPrt->_comSubstr.size() != targetPrt->_comSubstr.size()) continue;
		for(size_t j=0 ; j<grpPrt->_comSubstr.size() ; ++j){
			if(grpPrt->_comSubstr[i] != targetPrt->_comSubstr[i]) break;
			else if(j==grpPrt->_comSubstr.size()-1){
				_groupList[i].push_back(targetPrt);
				return true;
			}
		}

	}
	return false;
}